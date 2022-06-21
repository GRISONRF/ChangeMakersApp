"""Server for movie ratings app."""

from contextlib import redirect_stderr
from flask import (Flask, render_template, request, flash, session,
                   redirect)
import crud
from model import connect_to_db, db
from jinja2 import StrictUndefined
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

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

    return render_template('i_register.html')


@app.route('/i_register', methods=['POST'])
def register_institution():
    """Create new institution"""

    inst_name = request.form.get("iname")
    inst_email = request.form.get("iemail")
    inst_password = request.form.get("ipassword")
    inst_address = request.form.get("iaddress")

    user = crud.get_inst_by_email(inst_email)

    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_institution(inst_name, inst_email, inst_password, inst_address)
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
    vlocation = request.form.get("vlocation")

    user = crud.get_volunteer_by_email(volu_email)

    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_volunteer(vfname, vlname, volu_email, volu_password, vlocation)
        db.session.add(user)    
        db.session.commit()
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
    volu_password = request.form.get("vpassword")

    inst_email = request.form.get("iemail")
    inst_password = request.form.get("ipassword")

    # Get user's password to check if the entered password is correct.
    volu_user = crud.Volunteer.query.filter_by(v_email=volu_email).first()
    inst_user = crud.Institution.query.filter_by(inst_email=inst_email).first()

    # volunteer
    if volu_user and volu_user.v_password == volu_password:
        session['volunteer'] = volu_user.volunteer_id
        return redirect('/vol_profile')

    else:
        flash("User email or password don't match. Try again.")


    # institution
    if inst_user and inst_user.inst_password == inst_password:
        session['inst'] = inst_user.inst_id

        return redirect('/inst_profile')

    else:
        flash("User email or password don't match. Try again.")
        
    return redirect('/')

# ---------------- LOGOUT ----------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
 

# ---------------- INSTITUTION PROFILE ----------------
@app.route('/inst_profile')
def inst_profile():
    """ Institution profile page """

    if "inst" in session:
        inst_id = session["inst"] 

        inst = crud.get_inst_by_id(inst_id)
        all_events = crud.get_events()

        return render_template('inst_profile.html', inst=inst, all_events=all_events)

    else: return render_template('login.html')


# ---------------- VOLUNTEER PROFILE ----------------
@app.route('/vol_profile')
def volu_profile():
    """ Volunteer profile page """

    if "volunteer" in session:
        volunteer_id = session["volunteer"]

    volunteer = crud.get_volunter_by_id(volunteer_id)
    my_events = crud.get_events_by_volunteer_id(volunteer_id)

   
    return render_template('vol_profile.html', volunteer=volunteer, my_events=my_events)
    

 
# ---------------- INSTITUTION CREATE A NEW EVENT ----------------
@app.route('/new_event', methods=['POST'])
def create_event():
    """ Save event in database and show new event card on inst_profile page """

    # Get info from the form
    evt_title = request.form.get("evt_title")
    evt_date = request.form.get("evt_date") 
    evt_start_time = request.form.get("evt_start_time")
    evt_end_time = request.form.get("evt_end_time")
    evt_address = request.form.get("evt_address") 
    evt_description = request.form.get("evt_description")

    evt_date = datetime.strptime(evt_date, '%d/%m/%Y').date()

    evt_address = Nominatim(user_agent='inst-event').geocode(evt_address).address
    evt_lat = Nominatim(user_agent='inst-event').geocode(evt_address).latitude
    evt_long = Nominatim(user_agent='inst-event').geocode(evt_address).longitude

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
        evt_lat, 
        evt_long, 
        inst_id, 
        evt_description
        )

   
    db.session.add(new_event) 
    db.session.commit()
    return redirect('/inst_profile')

# UPDATE USER PROFILE
# @app.route("/update_user")
# def update_user():
#     """ User update profile """

#     if "user" in session:
#         user_id = session["user"]

#     fullname = request.args.get('fullname')
#     address = request.args.get('address')
#     if fullname and address:
#         longitude = crud.get_longitude(address)
#         latitude = crud.get_latitude(address)
#         db.session.query(User).filter(User.user_id == user_id).update({"fullname": fullname, "address":address, "longitude":longitude, "latitude":latitude})
#         db.session.commit()
#         flash('Your profile was updated!')
#     elif fullname:
#         db.session.query(User).filter(User.user_id == user_id).update({"fullname": fullname})
#         db.session.commit()
#         flash('Your profile was updated!')
#     elif address:
#         longitude = crud.get_longitude(address)
#         latitude = crud.get_latitude(address)
#         db.session.query(User).filter(User.user_id == user_id).update({"address":address, "longitude":longitude, "latitude":latitude})
#         db.session.commit()
#         flash('Your profile was updated!')
#     else:
#         flash('Missing data!')


#     return redirect("/profile")

# ---------------- VOLUNTEER SIGN UP TO EVENTS ----------------
@app.route('/events', methods=['POST'])
def show_all_events():
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

    elif "inst" in session:
        inst_id = session["inst"]
        event = crud.get_event_by_id(event_id)

    event_is_saved = crud.event_is_saved(volunteer_id, event_id)

    return render_template("event_details.html", event=event, event_is_saved=event_is_saved)


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

    return render_template("vol_profile.html", sign_up_evt=sign_up_evt, my_events=my_events, volunteer=volunteer, event_is_saved=event_is_saved)




if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
