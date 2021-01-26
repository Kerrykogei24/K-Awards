# ~~K Awards~~.
# Author
[kerry](https://github.com/Kerrykogei24/K-Awards)

# Description
An application for rating and reviewing websites 

# Setup Instructions:
Requirements
# 1. Clone the repository
* Clone the the repository by running

* git clone https://github.com/Kerrykogei24/K-Awards
or download a zip file of the project from github

* Navigate to the project directory

* cd K-Awards
# 2. Create a virtual environment
* Install Virtualenv
 pip install virtualenv
 
* To create a virtual environment named virtual, run
virtualenv virtual

* To activate the virtual environment we just created, run
source virtual/bin/activate

# 3. Create a database
* You'll need to create a new postgress database, Type the following command to access postgress

 * $ psql
  * Then run the following query to create a new database named awards

# 4.create database instagram
# 5.Install dependencies
* To install the requirements from requirements.txt file,

  * pip install -r requirements.txt
# 6.Create Database migrations
* Making migrations on postgres using django

* python3 manage.py makemigrations gram
* then run the command below;

* python3 manage.py migrate
# 7.Run the app
* To run the application on your development machine,

* python3 manage.py runserver
# Running Tests
To run tests;
python3 manage.py test

# Technologies Used
This project was generated with
  * [Python](https://www.python.org/) version 3.8.0.
  * Django
  * Bootstrap.
  * javascript.
  * PSQL database.
  * HTML,CSS
# User stories
As a user of the application I should be able to:

*  View posted projects and their details
 * Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page
*  Access data from this application using API endpoints
There are no know bugs at the moment


# License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Kerrykogei24/K-Awards)
MIT License
\_ **Kerry Komar @2019**


# Collaboration Information
Clone the repository
Make changes and write tests
Push changes to github
Create a pull request
## Support and contact details
 For any issues ,contact at https://github.com/Kerrykogei24/K-Awards <br>
 Or for any pull requests, https://github.com/Kerrykogei24/K-Awards
  Incase you need more clarification, feel free to send an email to: 
Email: kerrykomar@gmail.com

