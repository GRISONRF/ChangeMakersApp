"""Server for movie ratings app."""

from contextlib import redirect_stderr
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
import crud
from model import connect_to_db, db, Volunteer, Institution
from jinja2 import StrictUndefined
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import cloudinary.uploader
import os
from passlib.hash import argon2

CLOUDINARY_KEY= os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "dwn0hs3si"

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# ---------------- HOMEPAGE ----------------
@app.route('/')
def homepage():
    """view homepage"""

    return render_template('homepage.html')


# ---------------- REGISTER PAGE ----------------
@app.route('/register')
def register_users():
    """ Return page for user to chose how to register """

    return render_template('register.html')


# ---------------- REGISTER AS INSTITUTION ----------------
@app.route('/inst_register')
def inst_register_page():
    """ Return page for the institution to register """

    all_causes = crud.get_all_causes()
    all_skills = crud.get_all_skills()

    return render_template('i_register.html', all_causes=all_causes)


@app.route('/i_register', methods=['POST'])
def register_institution():
    """Create new institution"""

    inst_name = request.form.get("iname")
    inst_email = request.form.get("iemail")
    inst_password = request.form.get("ipassword")
    inst_address = request.form.get("iaddress")
    inst_cause = request.form.get("cause")
    inst_pic = "/static/images/inst_pic.png"
    geolocator = Nominatim(user_agent='project')
    
    # using geocode to get the address, lat and lng
    iaddress = geolocator.geocode(inst_address)
    inst_lat = iaddress.latitude
    inst_lng = iaddress.longitude
    iaddress = iaddress.address

    # using PasswordHash
    hashed_pw = argon2.hash(inst_password)

    
    # using the lat and lng to get the city and state
    location = geolocator.reverse((inst_lat,inst_lng), exactly_one=True)
    inst_city = location.raw['address'].get('city', '')
    inst_state = location.raw['address'].get('state', '')

    
    user = crud.get_inst_by_email(inst_email)

    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_institution(
            inst_name, 
            inst_email, 
            hashed_pw, 
            iaddress, 
            inst_city, 
            inst_state, 
            inst_lat,
            inst_lng, 
            inst_pic,
            inst_cause
            )

        db.session.add(user)    
        db.session.commit()
        flash('Account created! Please, log in.')
        return redirect('/login_page')

    return redirect('/inst_register')


# ---------------- REGISTER AS VOLUNTEER ----------------
@app.route('/volu_register')
def volunteer_register_page():
    """ Return page for the volunteer to register """

    return render_template('v_register.html')


@app.route('/v_register', methods=['POST'])
def register_volunteer():
    """Create new volunteer"""

    volu_email = request.form.get("vemail")
    volu_password = request.form.get("vpassword")
    vfname = request.form.get("fname")
    vlname = request.form.get("lname")
    vcity = request.form.get("vcity")
    vstate = request.form.get("vstate")
    
    user = crud.get_volunteer_by_email(volu_email)

    # Hashing password
    volu_hashed = argon2.hash(volu_password)

    if user:
        flash("User email already exists.")
    else:
        volunteer_pic = "/static/images/volunteer-icon.PNG"
        user = crud.create_volunteer(
            vfname, 
            vlname, 
            volu_email, 
            volu_hashed, 
            vcity, 
            vstate, 
            volunteer_pic
        )
        
        db.session.add(user)
        db.session.commit()    
        # volunteer_pic = "/static/images/volunteer1.png"
        # db.session.query(Volunteer).filter(Volunteer.v_mail == volu_email).update({"v_pic":volunteer_pic})
        # db.session.commit()

        flash('Account created! Please, log in.')
        return redirect('/login_page')

    return redirect('/volu_register')


# ---------------- LOGIN ----------------
@app.route('/login_page')
def login_page():

    
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    """ Login with email and password """

    # Get data from the form
    volu_email = request.form.get("vemail")
    vattemped_pw = request.form.get("vpassword")
    
    inst_email = request.form.get("iemail")
    iattemped_pw = request.form.get("ipassword")


    # Get user's email to check if the entered email is correct.
    volu_user = crud.Volunteer.query.filter_by(v_email=volu_email).first()
    inst_user = crud.Institution.query.filter_by(inst_email=inst_email).first()
    

    # volunteer
    if volu_user:
        vhashed_pw = volu_user.v_password
        if argon2.verify(vattemped_pw, vhashed_pw):

            session['volunteer'] = volu_user.volunteer_id

            return redirect('/vol_profile')


    #institution
    elif inst_user:
        ihashed_pw = inst_user.inst_password
        if argon2.verify(iattemped_pw, ihashed_pw):
            session['inst'] = inst_user.inst_id
            inst_id = session["inst"]
            inst_comments = crud.get_reviews_by_inst(inst_id)

            return redirect(f'/inst_profile/{inst_id}')
    else:
        flash("User email or password don't match. Try again.")
        
    return redirect('/login_page')


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged Out")
    return redirect('/')
 

# ---------------- INSTITUTION PROFILE ----------------
@app.route('/inst_profile/<inst_id>')
def inst_profile(inst_id):
    """ Institution profile page """

    if "inst" in session:
        inst_id = session["inst"] 

    inst = crud.get_inst_by_id(inst_id)
    all_events = crud.get_all_events()
    all_skills = crud.get_all_skills()
    all_comments = crud.get_reviews_by_inst(inst_id)

    if "volunteer" in session:
        volunteer_id = session["volunteer"]
        volunteer = crud.get_volunter_by_id(volunteer_id)
        all_comments = crud.get_reviews_by_inst(inst_id)

        return render_template('inst_profile.html', inst=inst, all_events=all_events, all_skills=all_skills, all_comments=all_comments, volunteer=volunteer)

    return render_template('inst_profile.html', inst=inst, all_events=all_events, all_skills=all_skills, all_comments=all_comments)



@app.route('/inst_profile/<inst_id>/review', methods=['POST'])
def inst_ratings(inst_id):
    """ Review and comments institution profile """

    if "volunteer" in session:
        volunteer_id = session["volunteer"]

        inst_comment = request.json.get('comment')
        inst_review = request.json.get('review')
        volunteer = crud.get_volunter_by_id(volunteer_id)
        volunteer_fname = volunteer.fname
        all_comments = crud.get_reviews_by_inst(inst_id)

        volunteer_comment = crud.create_inst_comment(
                                inst_comment, 
                                inst_review, 
                                inst_id, 
                                volunteer_id
                            )
        db.session.add(volunteer_comment)
        db.session.commit()

        inst_comment = {
            "comment": inst_comment,
            "comment_id": volunteer_comment.comment_id,
            "review" : inst_review,
            "inst_id": int(inst_id),
            "volunteer_id": volunteer_id,
            "volunteer_fname": volunteer_fname,
        }
       

        return inst_comment


@app.route('/inst_profile/<comment_id>/delete', methods=['POST'])
def delete_comment(comment_id):
    """ Delete the comment from the db """

    comment = crud.get_review_by_id(comment_id)
    volunteer_id = comment.volunteer_id
    crud.delete_comment_by_id(comment_id)


    return str(volunteer_id)


@app.route('/all_inst')
def all_institutions():
    """ Show all the institutions """

    institutions = crud.get_all_institutions()

    return render_template('all_inst.html', institutions=institutions)


# ---------------- VOLUNTEER PROFILE ----------------
@app.route('/vol_profile')
def volu_profile():
    """ Volunteer profile page """

    if "volunteer" in session:
        volunteer_id = session["volunteer"]

    volunteer = crud.get_volunter_by_id(volunteer_id)
    my_events = crud.get_events_by_volunteer_id(volunteer_id)
    all_causes = crud.get_all_causes()
    all_skills = crud.get_all_skills()
    volunteer_skills = crud.get_skills_by_volunteer(volunteer_id)
   
    return render_template('vol_profile.html', volunteer=volunteer, my_events=my_events, all_causes=all_causes, all_skills=all_skills, volunteer_skills=volunteer_skills)



@app.route('/upload', methods=["POST"])
def volu_upload_picture():
    """ Upload a new profile picture and add it to the database"""

    if "volunteer" in session:
        volunteer_id = session["volunteer"]

        volunteer_pic = request.files['volunteer-pic']
        result = cloudinary.uploader.upload(volunteer_pic,
                                            api_key=CLOUDINARY_KEY,
                                            api_secret=CLOUDINARY_SECRET,
                                            cloud_name=CLOUD_NAME)
        vpic_url = result['secure_url']

        db.session.query(Volunteer).filter(Volunteer.volunteer_id==volunteer_id).update({"v_pic":vpic_url})
        db.session.commit()
        flash('Profile picture updated!')

        return redirect("/vol_profile")
    
    elif "inst" in session:
        inst_id = session["inst"]

        inst_pic = request.files['inst-pic']
        result = cloudinary.uploader.upload(inst_pic,
                                            api_key=CLOUDINARY_KEY,
                                            api_secret=CLOUDINARY_SECRET,
                                            cloud_name=CLOUD_NAME)
        ipic_url = result['secure_url']

        db.session.query(Institution).filter(Institution.inst_id==inst_id).update({"inst_pic":ipic_url})
        db.session.commit()
        flash('Profile picture updated!')

        return redirect(f'/inst_profile/{inst_id}')


@app.route('/select_skills', methods=['POST'])
def select_skills():
    """ Save the skills the volunteer selected from form """

    if "volunteer" in session:
        volunteer_id = session["volunteer"]
        
        skill_id1 = request.form.get("skill1")
        skill_id2 = request.form.get("skill2")
        skill_id3 = request.form.get("skill3")
    
    
        skill1 = crud.create_volunteer_skill(volunteer_id, skill_id1)
        skill2 = crud.create_volunteer_skill(volunteer_id, skill_id2)
        skill3 = crud.create_volunteer_skill(volunteer_id, skill_id3)
        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(skill3)
        db.session.commit()
     
        return redirect("/vol_profile")     



# ---------------- INSTITUTION CREATE A NEW EVENT ----------------
@app.route('/new_event', methods=['POST'])
def create_event():
    """ Save event in database and show new event card on inst_profile page """

    # Get info from the form
    evt_title = request.form.get("evt_title")
    form_date = request.form.get("evt_date") 
    evt_start_time = request.form.get("evt_start_time")
    evt_end_time = request.form.get("evt_end_time")
    evt_address = request.form.get("evt_address") 
    evt_description = request.form.get("evt_description")
    
    geolocator = Nominatim(user_agent='inst-event')
    skill1 = request.form.get("skill1")
    skill2 = request.form.get("skill2")
    skill3 = request.form.get("skill3")
    
    # using geocode to get the address, lat and lng
    evt_address = geolocator.geocode(evt_address).address
    evt_lat = geolocator.geocode(evt_address).latitude
    evt_lng = geolocator.geocode(evt_address).longitude

    # using the lat and lng to get the city and state
    location = geolocator.reverse((evt_lat,evt_lng), exactly_one=True)
    evt_city = location.raw['address'].get('city', '')
    evt_state = location.raw['address'].get('state', '')

    # format the date
    edate_not_formated = datetime.strptime(form_date, '%d/%m/%Y').date()
    month = edate_not_formated.strftime("%m")
    day = edate_not_formated.strftime("%d")
    year = edate_not_formated.strftime("%Y")
    evt_date = f'{month} / {day} / {year}'

    # Still need to create an ELSE for when inst_id is NOT in session?
    if "inst" in session:
        inst_id = session["inst"]
        inst = crud.get_inst_by_id(inst_id)

        new_event = crud.create_event(
            evt_title, 
            evt_date, 
            evt_start_time, 
            evt_end_time, 
            evt_address,
            evt_city,
            evt_state, 
            evt_lat, 
            evt_lng, 
            inst_id, 
            evt_description
            )
        
        db.session.add(new_event)
        db.session.commit() 

        all_skills = crud.get_all_skills()
        event_skill1 = crud.create_event_skill(new_event.event_id, skill1)
        event_skill2 = crud.create_event_skill(new_event.event_id, skill2)
        event_skill3 = crud.create_event_skill(new_event.event_id, skill3)

        db.session.add(event_skill1)
        db.session.add(event_skill2)
        db.session.add(event_skill3) 
        db.session.commit()
        
    return redirect(f'/inst_profile/{inst_id}')



# ---------------- VOLUNTEER SIGN UP TO EVENTS ----------------
@app.route('/events', methods=['POST'])
def show_events_by_location():
    """ Display all events by given location """

    location = request.form.get("location")
    evt_location = Nominatim(user_agent='inst-event').geocode(location).address

    all_events = crud.get_events_by_location(evt_location)
 
    return render_template("events.html", all_events=all_events)


@app.route('/events/<event_id>')
def event_details(event_id):
    """ Show detais of a particular event """

    if "volunteer" in session:
        volunteer_id = session["volunteer"]

        event = crud.get_event_by_id(event_id)
        event_is_saved = crud.event_is_saved(volunteer_id, event_id)
        cause_id = crud.get_cause_by_event(event_id)
        cause = crud.get_cause_by_cause_id(cause_id)
        event_skills = crud.get_skills_by_event(event_id)
      
        
        return render_template("event_details.html", event=event, event_is_saved=event_is_saved, event_skills=event_skills, cause=cause)

    elif "inst" in session:
        inst_id = session["inst"]
        institution = crud.get_inst_by_id(inst_id)

        event = crud.get_event_by_id(event_id)
        event_skills = crud.get_skills_by_event(event_id)

        return render_template("event_details.html", event=event,event_skills=event_skills, institution=institution)


@app.route('/events/<event_id>/sign_up')
def volunteer_signup_evt(event_id):
    """ Add event to volunteer events database """

    if "volunteer" in session:
        volunteer_id = session["volunteer"]
        
        volunteer = crud.get_volunter_by_id(volunteer_id)
        sign_up_evt = crud.create_volunteer_evt(volunteer_id, event_id)
        db.session.add(sign_up_evt)
        db.session.commit()
        
        my_events = crud.get_events_by_volunteer_id(volunteer_id)
        event_is_saved = crud.event_is_saved(volunteer_id, event_id)
        all_causes = crud.get_all_causes()
        
    return redirect("/vol_profile")



@app.route('/all_events')
def show_all_events():
    """ Show all the events """

    events = crud.get_all_events()

    return render_template('all_events.html', events=events)

# ########################## REACT #############################


@app.route('/search_results.json', methods=['POST'])
def get_results():
    """ Return a JSON response with the search results """    

    city = request.json.get("city") 
    state = request.json.get("state")
    cause = request.json.get("cause")

    events_by_city_cause = crud.get_event_by_city_cause(city, state, cause)

    # what I want to display in the result card: event title, institution name, event location, institution/event cause, event date.
    search_results = []
    for event in events_by_city_cause:
        search_results.append( 
            {
            "evt_title" : event.evt_title,
            "inst_name": event.inst.inst_name,
            "evt_location" : event.evt_address,
            "cause": event.inst.cause.cause_name,
            "evt_date": event.evt_date,
            "event_id": event.event_id    
            }
        )
    return jsonify(search_results)



@app.route('/search_recommended.json', methods=['POST'])
def get_recommended_results():
    """ Return a JSON response with the recommended results """    

    if "volunteer" in session:
        volunteer_id = session["volunteer"]

        rCity = crud.get_city_by_vol(volunteer_id)
        rState = crud.get_state_by_vol(volunteer_id)
        rSkill = crud.get_skills_by_volunteer(volunteer_id) #list
        skills_id = crud.get_skills_id_by_skill_obj(rSkill)

        events_by_location_skill = crud.get_events_by_city_state_skill(rCity, rState, skills_id)

        # what I want to display in the recommendations card: event title, institution name, event location, institution/event cause, event date.

        recommendedResults = []
        for event in list(events_by_location_skill):
            recommendedResults.append(
                {
                "evt_title" : event.evt_title,
                "inst_name": event.inst.inst_name,
                "evt_location" : event.evt_address,
                "cause": event.inst.cause.cause_name,
                "evt_date": event.evt_date,
                "event_id": event.event_id  
                }
            )

        return jsonify(recommendedResults)

# ------------------------ MAP --------------------

@app.route('/instgeocoords.json')
def get_inst_coords():
    """ Setting up a queryString with inst location to pass back to db """

    #inst_id is the parameter in the queryString
    inst_id = request.args.get("inst_id")
    inst = crud.get_inst_by_id(inst_id)
    
    icoords_dict = {"lat": inst.inst_lat, "lng": inst.inst_lng}

    return jsonify(icoords_dict)


@app.route('/eventgeocoords.json')
def get_event_coords():
    """ Setting up a queryString with event location to pass back to db """

    #inst_id is the parameter in the queryString
    event_id = request.args.get("event_id")
    event = crud.get_event_by_id(event_id)

    ecoords_dict = {"lat": event.evt_lat, "lng": event.evt_lng}

    return jsonify(ecoords_dict)




if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
