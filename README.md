<img src="static/images/applogotest.png" width="60">

**ChangeMakers** has been designed to make it easier for people to find volunteer opportunities near them, and for institutions to find qualified volunteers for upcoming events.



## Table of contents
* 🤖 [Technologies](#technologies-used)
* ⭐ [Features](#features)
* 📖 [Set Up](#set-up)
* 🌸 [About Me](#about-me)

## Technologies Used
* Backend: Python, Flask, SQL, PostgreSQL, SQLAlchemy.
* Frontend: Javascript, React JS, HTML, CSS, Bootstrap, AJAX, Jinja2.
* APIs: Geolocation API, Google Maps API, Cloudinary API.

## Features


### Homepage
* Used the Tiny-slider Javascript library to create a carousel that rotates through all of the institutions on the site. 
<img src="static/images/for-readme/homepagegif.gif">


### Institution
* Institutions can log in, and on their profile page, create new events.
* In the form, they can add all the details of the event and specify what skills they’re looking for. 
* Using Cloudinary API, the institution can change the default event picture. 
<img src="static/images/for-readme/evtgift.gif">


### Volunteer
* After the volunteer creates an account and logs in, they can change their picture, choose up to 3 skills, and start looking for opportunities.
* For the Recommended Events feature, volunteers are matched with opportunities based on their individual skills and by their location. To implement this, I had to create 2 new many-to-many relationships in my database, so I could find the events that matched the skills selected by the volunteer. And using Geopy, I could locate the coordinates of the event and the volunteer to match them by the city.

* The volunteer can also search for opportunities by the city, state and what cause they are most interested in. I used a fetch request to get the search results from the database using an SQLAlchemy query, and the results are displayed on the page using React.

* In the event’s page, I used GoogleMaps API to render the event’s location.
 
* Users can also click on the institution page to see other events they might be interested in, as well as leave a comment and rate their experience with that institution, a feature that was implemented using AJAX. 
 

<img src="static/images/for-readme/volunteergif.gif">


## Set Up

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
You can now navigate to 'localhost:5000/' to access the app

## About me
