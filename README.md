# [CINEVAULT](https://cinevault-f47e66547791.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/patrickaod/CineVault)](https://github.com/patrickaod/CineVault/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/patrickaod/CineVault)](https://github.com/patrickaod/CineVault/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/patrickaod/CineVault)](https://github.com/patrickaod/CineVault)
---
![amIresponsive: CineVault](documentation/screenshots/amIresponsive.png)

# Project Overview: CineVault 

Your Personalized Movie Collection and Management Application. CineVault is a web-based application designed to allow users to create, manage, and explore their own personalised movie collections. The application provides functionality for user registration, login, adding, editing, and deleting movies. The interface dynamically adjusts to display appropriate UI elements based on the users screen size or to what movies they have in their collection.
The application also supports role-based and session-based access control to ensure secure appropriate access within the platform.

## UX

There are countless ideas to consider when starting a CRUD application, but a movie management system stands out for several reasons. It allows for the organisation of movies into collections, updating of their details, and managing them in various states, such as a watchlist. This project naturally involves interacting with a database, providing hands-on experience with querying, updating, and managing records, not just for movies but also for users. Implementing user login and personalized movie management introduces invaluable authorisation concepts, adding additional layers of complexity to the application.

While more intricate ideas, like e-commerce platforms or social networking sites, offer greater complexity, they can also be overwhelming for a project focused on mastering CRUD operations. A movie management system offers the perfect balance between complexity and feasibility, making it an ideal choice for effectively demonstrating CRUD functionality.

### Colour Scheme

The online movie industry often chooses darker themes to create a more immersive environment, but the benefits go beyond simply focusing the viewer's attention. While content is at the heart of these platforms, maximizing watch time is crucial, and dark backgrounds help achieve this by reducing eye strain, allowing users to engage for longer periods. Additionally, dark themes align with the tradition of cinema and enhance the perception of a sleek, luxurious aesthetic, which sets the tone and mood—something platforms like Netflix have mastered.

**1. Dark Background (`#121212` or `#1C1C1C`):**
These deep, near-black shades are reminiscent of a dark movie theater, helping to create an immersive environment that draws users into the content, similar to how dim lighting enhances the experience in a cinema.

**2. Accent Color (Gold/Amber - `#FFC107`):**
Gold and amber tones evoke the allure and excitement of the film industry. These colors suggest luxury, success, and the golden age of cinema.

**3. Accent Color (Crimson Red/Ruby - `#D32F2F`):**
Red is often associated with emotions, drama, and passion, which are central to the storytelling aspect of movies. This color adds depth and intensity to the design, evoking the red carpets of film premieres or the curtains in classic theaters.

**4. Text Color (White or Very Light Gray - `#E0E0E0`):**
White or light gray text on a dark background ensures maximum readability, which is crucial for user experience. This choice keeps the text clear and easy to read without causing eye strain, which is particularly important for longer reading sessions.

![Colour Theme by Coolors](documentation/screenshots/coolorTheme.png)


### Typography

For this project, I selected a combination of Google Fonts that balances readability, modern aesthetics, and strong visual hierarchy to complement the dark, cinematic theme of the site.

**Heading Typography:**

- **H1 ([Montserrat Subrayada](https://fonts.google.com/specimen/Montserrat+Subrayada?query=mon)):**

I chose Montserrat Subrayada for the primary headings (H1) due to its bold, distinct style with an underline feature that draws attention and creates emphasis. This font captures the modern and cinematic feel, ensuring the main titles stand out while adding a subtle sense of sophistication, perfect for a movie-centric platform.

- **Subheadings (H2-H6: [Oswald](https://fonts.google.com/specimen/Oswald?query=oswald)):**

 I used Oswald because it provides a clean and structured look, giving the site a professional and organized feel. Oswald's strong lines and compact style offer great emphasis across various element sizes, ensuring the subheadings stand out clearly without overpowering the overall design. 

**Body Text ([Roboto](https://fonts.google.com/specimen/Roboto)):**

For the body text, I used Roboto, a versatile and popular sans-serif font. Roboto is highly legible even at smaller sizes, making it ideal for the main text of the website.

**Fallback Font: (Sans-serif):**

In case the primary fonts fail to load, I’ve set a fallback to sans-serif. This ensures that the text remains clean and readable across all devices.

**Icons ([Materialize](https://materializecss.com/icons.html)):**

Using the Materialize framework streamlines the development process by providing pre-built components and responsive design elements. I incorporated various icons from its library to enhance the visual appeal of the application, making the interface more intuitive and engaging for users.

**Favicon ([favicon.io](https://favicon.io/emoji-favicons/cinema)):**

A favicon enhances the user experience by providing a small, recognizable icon that appears in the browser tab, bookmarks, and history, helping users quickly identify and navigate back to your website. It also adds a professional touch and strengthens brand identity.

## User Stories

### New Site Users

- As a new site user, I would like to collate my favorite movies, so that I can enjoy them at a later date.
- As a new site user, I would like to review movies I add, so that can remind myself how I felt.
- As a new site user, I would like to create a watchlist of things I want to see, so that it speeds up the process of me looking for something later.
- As a new site user, I would like an easily searchable list of movies, so that I can find something to watch quickly.
- As a new site user, I would like my movies to be seperated by genre, so that I can different collections of movies.

### Returning Site Users

- As a returning site user, I would like everything to be save, so that I don't have the hassle of re-uploading anything.
- As a returning site user, I would like to easily manageable, so that I can add or remove movies at will.
- As a returning site user, I would like to know when something was last updated, so that I can keep track of my collection.
- As a returning site user, I would like to user-friendly features, so that I can back out of a decision if I want.
- As a returning site user, I would like to know my collection is safe, so that I can have piece of mind.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Index
  - ![screenshot](documentation/wireframes/mobilewireframeIndex.png)

Account
  - ![screenshot](documentation/wireframes/mobilewireframeAccount1.png)

</details>

### Tablet Wireframes

<details>
<summary> Click here to see the Tablet Wireframes </summary>

Index
  - ![screenshot](documentation/wireframes/tabletwireframeIndex.png)

Account
  - ![screenshot](documentation/wireframes/tabletwireframeAccount.png)

</details>

### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

Index
  - ![screenshot](documentation/wireframes/webwireframeIndex.png)

Account
  - ![screenshot](documentation/wireframes/webwireframeAccount.png)

</details>

## Features

### Existing Features

- **Animated Header and Form Fields**

    - The animation provides a smooth, enticing, responsive introduction to the website.

![Header and Form Animation](documentation/screenRecordings/headerAnimation.gif)

- **Minimalist Homepage**

    - The minimalist homepage focuses user attention only leaving room for the essentials: the logo, logout, add, and search functions.

![Minimalist Homepage](documentation/screenshots/minimalistHomepage.jpeg)

- **Grey Scale Background**

    - The dark background maintains the theme while adding vibrant elements to capture and retain user attention.

![Grey Scale Background](static/images/theater.jpg)

- **Frosted Glass Navigation Bar**

    - The frosted glass navigation bar enhances the theme with a sleek, modern look while keeping the focus on key navigation elements.

![Frosted Glass Navigation Bar](documentation/screenshots/frostedNavBar.jpeg)

- **Side Navigation**

    - The side navigation menu offers a convient navigation tool to mobile users. 

![Side Navigation](documentation/screenshots/sideNav.jpeg)

- **Logout**

    - The logout feature gives users a quick and easy way to exit their accounts should they wish to log in again as alternative users. 

![Logout](documentation/screenshots/logout.jpeg)

- **Flash Messages**

    - Flash messages provide real-time feedback to users by displaying temporary notifications, such as success or error messages, that automatically disappear after a set period.

![Flash Messages](documentation/screenshots/flashmessages.png)

- **Search Bar**

    - A search bar allows users to quickly find content by entering keywords such as "title", "genre", or "watchlist", enhancing navigation and usability.

![Search Bar](documentation/screenshots/search.jpeg)

- **Dynamic Add Button**

    - The add button dynamically appears based on whether movies are displayed on the screen, preventing overlap and ensuring a clean layout. 

![Middle Add Button](documentation/screenshots/midAddButton.jpeg)
![Bottom Add Button](documentation/screenshots/bottomAddButton.jpeg)

- **Movie Add Form**

    - The movie add form directs user focus by blurring and disabling the background. It turns green upon successful input, providing positive feedback.

![Movie Add Form](documentation/screenshots/movieAddForm.jpeg)

- **Movie Card**

    - The movie card delivers clear, straightforward billing of user input and updates dynamically as changes are made.

![Movie Card](documentation/screenshots/shinningMovieCard.jpeg)

- **Side Scrolling**

    - As the movie list expands, items stack to the right and eventually transition to a scrollable view, similar to platforms like Netflix.

![Side Scrolling](documentation/screenshots/sideScrolling.jpeg)

- **Edit Delete Button**

    - The edit and delete buttons are displayed on each card for easy management, while remaining unobtrusive to maintain a clean page layout.

![Edit Delete Button](documentation/screenshots/editAndDelete.jpeg)

- **Delete Confirmation**

    - The delete confirmation prompts users to verify their choice before finalising, preventing accidental deletions and ensuring deliberate actions.

![Delete Confirmation](documentation/screenshots/deleteConfirm.jpeg)

- **User Authentication**

    - User authorization ensures secure access by verifying credentials and managing permissions. The role-based system assigns a session token for accessing personal data, keeping the experience both seamless and protected.

![User Authentication](documentation/screenshots/userAuth.jpeg)

- **Session Token Usage**

    - Statements like the example below always verify the current user before displaying any content or routing, ensuring high security.

![Session Token Usage](documentation/screenshots/sessionUseage.jpeg)

- **Session Token Error Handling**

    - To prevent brute force attacks, try and except blocks handle errors and redirect unauthorized users back to the index page. 

![Session Token Error Handling](documentation/screenshots/tryExceptCase.jpeg)



### Future Features

- Friends List:
    - Enables users to follow friends and share movie recommendations, similar to IMDb.
- Intergrated Watchlist:
  - Link movie cards to a dedicated list of watchable movies, with each entry featuring direct links for easy access.
- Movie Card:
  - Upload images to create your own movie titles.
  - Enable the cards to flip between the movie title and the information on the back. 
- Role based - Admin Privileges:
    - User Permissions 
    - Content Management 
    - Theme settings 
    - Component / widget injection (special offers / events)


## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![VSCode](https://img.shields.io/badge/VSCode-grey?logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com) used as my local IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Materialize](https://img.shields.io/badge/Materialize-grey?logo=materialdesign&logoColor=F5A5A8)](https://materializecss.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Flask](https://img.shields.io/badge/Flask-grey?logo=flask&logoColor=000000)](https://flask.palletsprojects.com) used as the Python framework for the site.
- [![MongoDB](https://img.shields.io/badge/MongoDB-grey?logo=mongodb&logoColor=47A248)](https://www.mongodb.com) used as the non-relational database management with Flask.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.
- [![Coolors](https://img.shields.io/badge/Coolors-grey?)](https://coolors.co/) used for colour scheme.
- [![ClipChamp](https://img.shields.io/badge/ClipChamp-grey?)](https://clipchamp.com/en/) used for Gif creation.

## Database Design

My project uses a non-relational database with MongoDB, and therefore the database architecture doesn't have actual relationships like a relational database would.

My database is called **project3**.

It contains 2 collections:

- **users**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | username | String | |
    | password | String | uses Secure Hash Algorithm (scrypt) |
    | role | String | 

- **movies**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | title | String |  |
    | genre | String | |
    | rating | String | |
    | watchlist | String | |
    | created_by | String | selected from the *users* collection |
    | created_on | Date |  |
    | updated_on | Date |  |

