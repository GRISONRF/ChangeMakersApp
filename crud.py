"""CRUD operations."""

from model import db, Volunteer, Favorite, Institution, VolunteerEvt, Event, VolunteerComment, connect_to_db


# VOLUNTEER
def create_volunteer(fname, lname, v_email, v_password):
    """ Create and return a new user (volunteer) """

    volunteer = Volunteer(
        fname=fname, 
        lname=lname, 
        v_email=v_email, 
        v_password=v_password
        )
    return volunteer


def get_volunteers():
    """ Return all volunteers """

    return Volunteer.query.all()

def get_volunter_by_id(volunteer_id):
    """ Return volunteer by id """

    return Volunteer.query.get(volunteer_id)

# def get_volunteer_by_fname(fname):
#     """ return volunteers by first name """

#     return Volunteer.query.filter(Volunteer.fname == fname).all()

def get_volunteer_by_email(v_email):
    """ Return volunteer by email """

    return Volunteer.query.filter(Volunteer.v_email == v_email).first()


# INSTITUTION
def create_institution(inst_name, inst_email,inst_password, inst_address):
    """ Create and return a new institution """

    institution = Institution(
        inst_name=inst_name, 
        inst_email=inst_email,
        inst_password=inst_password, 
        inst_address=inst_address
        )
    return institution

def get_institutions():
    """ Return all institutions """
    return Institution.query.all()

def get_inst_by_id(inst_id):
    """ Return institution by id """

    return Institution.query.filter(Institution.inst_id==inst_id).first()

def get_inst_by_email(inst_email):
    """ Return institution by email """

    return Institution.query.filter(Institution.inst_email==inst_email).first()


# COMMENT
def create_volunteer_comment(comment, event, volunteer):
    """ Create a volunteer comment """

    vlt_comment = VolunteerComment(
        comment=comment, 
        event=event, 
        volunteer=volunteer
        )
    return vlt_comment

# EVENT
#Do I need to add volunteer, inst and comments as parameters?
def create_event(evt_title, evt_date, evt_start_time, evt_end_time, evt_address, evt_lat, evt_long, inst_id, evt_description):
    """ Create and return an event """

    new_event = Event(
        evt_title=evt_title, 
        evt_date=evt_date, 
        evt_start_time=evt_start_time, 
        evt_end_time=evt_end_time, 
        evt_address=evt_address, 
        evt_lat=evt_lat, 
        evt_long=evt_long, 
        inst_id=inst_id, 
        evt_description=evt_description
        )
    return new_event

def get_events():
    """ Return all the events """

    events = Event.query.all()
    return events


def get_events_by_location(search_address):
    """ Return all the events by given location """

    return Event.query.filter(Event.evt_address==search_address).all()


def get_event_by_id(event_id):
    """ Get event by its id """

    return Event.query.get(event_id)

def create_volunteer_evt(volunteer_id, event_id):
    """ Create and return a new event that volunteer signed up """

    volunteer_evt = VolunteerEvt(
        volunteer_id=volunteer_id,
        event_id=event_id
    )
    return volunteer_evt