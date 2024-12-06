from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from bson.errors import InvalidId
from datetime import datetime
import os
import re
from flask import Flask, flash, render_template, redirect, request
from flask import session, url_for

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("MONGO_SECRET_KEY")

mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_id = request.form.get('form_id')
        if form_id == 'sign-up':

            username = request.form.get('username')
            password = request.form.get('password')

            if not username or not password:
                flash("All fields are required.", "error")
                return render_template('index.html'), 200

            existing_user = mongo.db.users.find_one(
                {'username': request.form.get('username', '').lower()})

            # check if username exists in the database
            if existing_user:
                flash('Username already exists. Please try again.', 'error')
                return redirect(url_for('index'))

            # insert new user into the database
            new_user = {
                'username': request.form.get('username'),
                'password': generate_password_hash
                (request.form.get('password')),
                'role': 'user'
            }
            mongo.db.users.insert_one(new_user)

            flash('Registration successful! You can now log in.', 'success')
            return render_template('index.html')

        elif form_id == 'login':

            username = request.form.get('username')
            password = request.form.get('password')

            if not username or not password:
                flash("All fields are required.", "error")
                return render_template('index.html'), 200

            existing_user = mongo.db.users.find_one(
                {'username': request.form.get('username', '').lower()})

            if existing_user:
                role = existing_user.get('role')

                if role == "user":
                    # ensure hashed password is correct
                    if check_password_hash(existing_user['password'], request.form.get('password')):  # noqa
                        # put the new user into 'session' cookie
                        session["user"] = request.form.get('username').lower()
                        flash('Login successful! You are now log in.', 'success')  # noqa
                        return redirect(url_for(
                            "account", username=session["user"]))
                    else:
                        # invalid password match
                        flash("Incorrect Username and/or Password")
                        return redirect(url_for("index"))
            else:
                # username doesn't exist
                flash("Incorrect Username and/or Password", "error")
                return redirect(url_for('index'))
    return render_template('index.html')


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # Safely check session
    user = session.get('user')
    if not user:
        flash("You need to log in to access your account.", "error")
        return redirect(url_for("index"))

    if request.method == 'POST':
        form_id = request.form.get('form_id')
        movie_id = request.form.get('movie_id')
        if form_id == 'movie_user_add':
            # Find the movie in the database
            try:
                # Validate and convert movie_id to ObjectId
                object_id = ObjectId(movie_id)
                movie_check = mongo.db.movies.find_one({'_id': object_id})
            except InvalidId:
                # Handle invalid ObjectId
                movie_check = False
            # Retrieve the watchlist value from the form
            watchlist = request.form.get("watchlist")

            # Set watchlist based on the value retrieved, default to "no" if not valid
            if watchlist not in {"yes", "no"}:
                watchlist = "no"

            if movie_check:
                # Update existing movie
                updated_movie = {
                    "title": request.form.get("title"),
                    "genre": request.form.get("genre"),
                    "rating": request.form.get("rating"),
                    "watchlist": watchlist,
                    'updated_on': datetime.now().strftime('%d/%m/%Y')
                }
                mongo.db.movies.update_one(
                    {'_id': movie_check['_id']}, {'$set': updated_movie})
                flash("Movie Successfully Updated", "success")
            else:
                # Add new movie
                new_movie = {
                    "title": request.form.get("title"),
                    "genre": request.form.get("genre"),
                    "rating": request.form.get("rating"),
                    "watchlist": watchlist,
                    'created_by': session['user'],
                    'created_on': datetime.now().strftime('%d/%m/%Y'),
                    'updated_on': datetime.now().strftime('%d/%m/%Y')
                }
                mongo.db.movies.insert_one(new_movie)
                flash("Movie Successfully Added", "success")

    elif request.method == 'GET':
        # Check if delete query parameter is present
        movie_id = request.args.get('delete_movie_id')

        if movie_id:
            # Delete the movie by its ID
            delete_result = mongo.db.movies.delete_one(
                {'_id': ObjectId(movie_id)})

            if delete_result.deleted_count > 0:
                flash("Movie Successfully Deleted", "success")
            else:
                flash("Failed to delete movie", "error")

    movies = mongo.db.movies.find({
        "created_by": session["user"]}).sort("created_on", 1)

    try:
        # Attempt to grab the session user's username from the database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # If the session is valid, render the account page
        return render_template(
            "account.html", username=username, movies=movies)

    except KeyError:
        # If the session does not have the "user" key, redirect to the index
        flash("You need to log in to access your account.", "error")
        return redirect(url_for("index"))

    except TypeError:
        # If the user is not found in the database, redirect to the index
        flash("You need to log in to access your account.", "error")
        return redirect(url_for("index"))


@app.route("/search_movies", methods=["POST"])
def search_movies():
    search_query = request.form.get('search_movies', '').strip()

    # Check if the input ends with a backslash or other special characters
    special_characters = [
        '\\', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '_', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<',
        '>', ',', '.', '?', '`', '~', '|'
    ]
    if search_query.endswith(tuple(special_characters)):
        flash("The search input cannot end with special characters like '\\'.", "error")  # noqa
        return redirect(url_for('account', username=session["user"]))

    if search_query:
        # Search for movies that match the search query
        movies = mongo.db.movies.find({'created_by': session["user"], '$or': [
                {'title': {'$regex': search_query, '$options': 'i'}},
                {'genre': {'$regex': search_query, '$options': 'i'}},
                {'watchlist': {'$regex': search_query, '$options': 'i'}}
            ]
        }).sort("created_on", 1)
    else:
        # If search query is empty, retrieve all movies
        movies = mongo.db.movies.find(
            {"created_by": session["user"]}).sort("created_on", 1)

    return render_template(
        "account.html", username=session["user"], movies=movies)


@app.route("/logout")
def logout():
    # remove user from state management
    session.pop('user')
    flash("You have been logged out", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
