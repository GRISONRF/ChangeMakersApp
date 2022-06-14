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



#LOGIN PAGE
@app.route('/login', methods=["POST"])
def login_volunteer():

    vemail = request.form.get("vemail") #form email from login page
    vpassword = request.form.get("vpassword")

    user = crud.get_volunteer_by_email(vemail)

    if user and user.v_password != vpassword:
        flash('email or password does not match')
    else:
        session["user_email"] = user.v_email
        flash('Logged in')
    return redirect('/')


# REGISTER PAGE
@app.route('/register')
def login_inst():
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


    return redirect('/')


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

    return redirect('/')



# LOGIN PAGE

# @app.route('/after_login')
# def login_1page():
#     return render_template('login.html')

# @app.route('/login')
# def login_page():
#     """ Show loggged in page """

#     volu_email = request.form.get("vemail")
#     volu_password = request.form.get("vpassword")

#     inst_email = request.form.get("iemail")
#     inst_password = request.form.get("ipassword")

#     volu_info = crud.Volunteer.query.filter_by(v_email=volu_email).first()
#     inst_info = crud.Institution.query.filter_by(inst_email=inst_email).first()

#     # volunteer
#     if volu_info and volu_info.password == volu_password:
#         flash("Logged in!")
#         session['volunteer_id'] = volu_info.volunteer_id
#         return redirect('/v_profile')

#     else:
#         flash("User email or password don't match. Try again.")


#     # institution
#     if inst_info and inst_info.password == inst_password:
#         flash("Logged in!")
#         session['inst_id'] = inst_info.inst_id
#         return redirect('/i_profile')

#     else:
#         flash("User email or password don't match. Try again.")


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
