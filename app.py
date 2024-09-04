import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from datetime import datetime
import re

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("MONGO_SECRET_KEY")

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    form_id = request.form.get('form_id')

    if form_id == 'sign-up':
        if request.method == 'POST':

            existing_user = mongo.db.users.find_one({'username': request.form.get('username','').lower()})

            #check if username exists in the database   
            if existing_user:
                flash('Username already exists. Please try again.', 'error')
                return redirect(url_for('index'))
            
            #insert new user into the database
            new_user = {
                    'username': request.form.get('username'),
                    'password': generate_password_hash(request.form.get('password')),
                    'role': 'user'
                    }
            mongo.db.users.insert_one(new_user)

            flash('Registration successful! You can now log in.', 'success')
            return render_template('index.html')
            
    elif form_id == 'login':
        if request.method == 'POST':
            existing_user = mongo.db.users.find_one({'username': request.form.get('username','').lower()})

            if existing_user:
                role = existing_user.get('role')
  
                if role == "user":
                    #ensure hashed password is correct
                    if check_password_hash (existing_user['password'], request.form.get('password')):
                        # put the new user into 'session' cookie
                        session["user"] = request.form.get('username').lower()
                        flash('Login successful! You are now log in.', 'success')
                        return redirect(url_for("account", username=session["user"])) 
                    else:
                        #invalid password match
                        flash("Incorrect Username and/or Password")
                        return redirect(url_for(index))
            else:
                # username doesn't exist
                flash("Incorrect Username and/or Password", "error")
                return redirect(url_for('index'))          
    return render_template('index.html')