<img src="static/images/applogotest.png" width="60">

**ChangeMakers** has been designed to make it easier for people to find volunteer opportunities near them, and for institutions to find qualified volunteers for upcoming events.

:office: Institutions can create events/opportunities and set up the skills they need for each particular one. 

:standing_man: Volunteers can select up to 3 skills for themselves and sign up for events/opportunities. They can search the events based on their location, the Institution cause or/and the matching skills. They can also leave a comment and rate the Institution they worked with.

## Table of contents
* 🤖 [Technologies](#technologies-used)
* ⭐ [Features](#features)
* 📖 [Set Up](#set-up)
* 🌸 [About Me](#about-me)

## Technologies Used
* Backend: Python, Flask, SQL, PostgreSQL, SQLAlchemy.
* Frontend: Javascript, React JS, HTML, CSS, Bootstrap, AJAX, JSON, Jinja2.
* APIs: Geolocation API, Google Maps API.

## Features

## Set Up


## About Me

To run this project, first clone or fork this repo:
```
git clone https://github.com/GRISONRF/final-project-hackbright.git
```
Create and activate a virtual environment inside your directory
```
virtualenv env
source env/bin/activate
```
Install the dependencies:
```
pip install -r requirements.txt
```
Sign up to obtain key for GoogleMaps 
Save your Mapbox API key in a file called `secrets.sh` using this format:
```
export APP_KEY="YOUR_KEY_GOES_HERE"
```
Source your key into your virtual environment:
```
source secrets.sh
```
Set up the database:
```
python3 seed_database.py
```
Run the app:
```
python3 server.py
```
You can now navigate to 'localhost:5000/' to access the travel app
