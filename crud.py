"""CRUD operations."""

from model import db, Volunteer, Favorite, Institution, VolunteerEvt, Event, VolunteerComment, Cause, connect_to_db


# -------------- Volunteer functions ---------------
def create_volunteer(fname, lname, v_email, v_password, v_address, v_pic):
    """ Create and return a new user (volunteer) """

    volunteer = Volunteer(
        fname=fname, 
        lname=lname, 
        v_email=v_email, 
        v_password=v_password,
        v_address=v_address,
        v_pic=v_pic
        )
    return volunteer


def get_volunteers():
    """ Return all volunteers """

    return Volunteer.query.all()


def get_volunter_by_id(volunteer_id):
    """ Return volunteer by id """

    return Volunteer.query.get(volunteer_id)


def get_volunteer_by_email(v_email):
    """ Return volunteer by email """

    return Volunteer.query.filter(Volunteer.v_email == v_email).first()


# --------------- Institution functions ---------------
def create_institution(inst_name, inst_email,inst_password, inst_address, inst_pic, cause_id):
    """ Create and return a new institution """

    institution = Institution(
        inst_name=inst_name, 
        inst_email=inst_email,
        inst_password=inst_password, 
        inst_address=inst_address,
        inst_pic=inst_pic,
        cause_id=cause_id
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

def get_insts_by_cause(cause_id):
    """ Return institutions by cause_id """

    return Institution.query.filter(Institution.cause_id==cause_id).all()


# --------------- Comment functions ---------------
def create_volunteer_comment(comment, event, volunteer):
    """ Create a volunteer comment """

    vlt_comment = VolunteerComment(
        comment=comment, 
        event=event, 
        volunteer=volunteer
        )
    return vlt_comment

# --------------- Event functions ---------------

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
    """ Return event by its id """

    return Event.query.get(event_id)


def create_volunteer_evt(volunteer_id, event_id):
    """ Create and return a new event that volunteer signed up """

    volunteer_evt = VolunteerEvt(
        volunteer_id=volunteer_id,
        event_id=event_id
    )
    return volunteer_evt 


def get_events_by_volunteer_id(volunteer_id):
    """ Return events that given volunteer signed up """

    events_volunteer_id = Event.query.join(VolunteerEvt).filter_by(volunteer_id=volunteer_id).all()
    return events_volunteer_id


def event_is_saved(volunteer_id, event_id):
    """ Return true if volunteer alrady has this event signed up """

    # All the events entries by the volunteer.
    events_volunteer_id = VolunteerEvt.query.filter_by(volunteer_id=volunteer_id).all()

    for event in events_volunteer_id:
        if int(event_id) == event.event_id:
            return True
    return False

# --------------- Ulpload pictures functions ---------------

def update_profile_pic():
    pass
    

# --------------- Cause functions ---------------


def create_cause(cause_name):
    """ Create and return a cause """

    new_cause = Cause(
                    cause_name=cause_name
                    ) 
    return new_cause


def get_all_causes():
    """ Return all the causes """

    return Cause.query.all()