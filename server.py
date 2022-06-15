"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
import crud
from model import connect_to_db, db
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


#HOMEPAGE
@app.route('/')
def homepage():
    """view homepage"""

    return render_template('homepage.html')



# REGISTER PAGE
@app.route('/register')
def register_users():
    """ Return page for user to chose how to register """

    return render_template('register.html')

# REGISTER AS INSTITUTION
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


# REGISTER AS VOLUNTEER
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
        user = crud.create_volunteer(vfname, vlname, volu_email, volu_password)
        db.session.add(user)    
        db.session.commit()
        flash('Account created! Please, log in.')
        # return render_template('login.html')
        return redirect('/login_page')

    return redirect('/volu_register')


#LOGIN PAGE
@app.route('/login_page')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    """ Show logged in page """

    volu_email = request.form.get("vemail")
    volu_password = request.form.get("vpassword")

    inst_email = request.form.get("iemail")
    inst_password = request.form.get("ipassword")

    volu_info = crud.Volunteer.query.filter_by(v_email=volu_email).first()
    inst_info = crud.Institution.query.filter_by(inst_email=inst_email).first()

    # volunteer
    if volu_info and volu_info.v_password == volu_password:
        session['volunteer'] = volu_info.volunteer_id # SHOULD I USE THE ID OR THE USER NAME?
        return redirect('/vol_profile')

    else:
        flash("User email or password don't match. Try again.")


    # institution
    if inst_info and inst_info.inst_password == inst_password:
        session['inst'] = inst_info.inst_id
        return redirect('/inst_profile')

    else:
        flash("User email or password don't match. Try again.")

# INSTITUTION PROFILE
@app.route('/inst_profile/')
def inst_profile():
    """ Institution profile page """

    if "inst" in session:
        inst_id = session["inst"]

    inst = crud.get_inst_by_id(inst_id)
    return render_template('inst_profile.html')







if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
