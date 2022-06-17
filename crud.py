"""CRUD operations."""

from model import db, Volunteer, Favorite, Institution, VolunteerEvt, Event, VolunteerComment, connect_to_db


# VOLUNTEER
def create_volunteer(fname, lname, v_email, v_password):
    """ Create and return a new user (volunteer) """

    volunteer = Volunteer(fname=fname, lname=lname, v_email=v_email, v_password=v_password)
    return volunteer


def get_volunteers():
    """ return all volunteers """

    return Volunteer.query.all()

def get_volunter_by_id(volunteer_id):
    """ return volunteer by id """

    return Volunteer.query.get(volunteer_id)

# def get_volunteer_by_fname(fname):
#     """ return volunteers by first name """

#     return Volunteer.query.filter(Volunteer.fname == fname).all()

def get_volunteer_by_email(v_email):
    """ return volunteer by email """

    return Volunteer.query.filter(Volunteer.v_email == v_email).first()


# INSTITUTION
def create_institution(inst_name, inst_email,inst_password, inst_address):
    """ create and return a new institution """

    institution = Institution(inst_name=inst_name, inst_email=inst_email,inst_password=inst_password, inst_address=inst_address)
    return institution

def get_institutions():
    """ return all institutions """
    return Institution.query.all()

def get_inst_by_id(inst_id):
    """ return institution by id """

    return Institution.query.filter(Institution.inst_id==inst_id).first()

def get_inst_by_email(inst_email):
    """ return institution by email """

    return Institution.query.filter(Institution.inst_email==inst_email).first()


# COMMENT
def create_volunteer_comment(comment, event, volunteer):
    """ create a volunteer comment """

    vlt_comment = VolunteerComment(comment=comment, event=event, volunteer=volunteer)
    return vlt_comment

# EVENT
#Do I need to add volunteer, inst and comments as parameters?
def create_event(evt_title, evt_date, evt_start_time, evt_end_time, evt_address, evt_lat, evt_long, inst_id, evt_description):
    """ create and return an event """

    new_event = Event(evt_title=evt_title, evt_date=evt_date, evt_start_time=evt_start_time, evt_end_time=evt_end_time, evt_address=evt_address, evt_lat=evt_lat, evt_long=evt_long, inst_id=inst_id, evt_description=evt_description)
    return new_event

def get_events():
    """ Get all the events """

    events = Event.query.all()
    return events

