"""CRUD operations."""

from model import db, Volunteer, Favorite, Institution, VolunteerEvt, Event, VolunteerComment, Cause, Skill, VolunteerSkill, EventSkill, connect_to_db
from geopy.geocoders import Nominatim

# -------------- Volunteer functions ---------------
def create_volunteer(fname, lname, v_email, v_password, v_city, v_state, v_pic):
    """ Create and return a new user (volunteer) """

    volunteer = Volunteer(
        fname=fname, 
        lname=lname, 
        v_email=v_email, 
        v_password=v_password,
        v_city=v_city,
        v_state=v_state,
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
def create_institution(inst_name, inst_email,inst_password, inst_address, inst_city, inst_state, inst_lat, inst_lng, inst_pic, cause_id):
    """ Create and return a new institution """

    institution = Institution(
        inst_name=inst_name, 
        inst_email=inst_email,
        inst_password=inst_password, 
        inst_address=inst_address,
        inst_city=inst_city,
        inst_state=inst_state,
        inst_lat=inst_lat,
        inst_lng=inst_lng,
        inst_pic=inst_pic,
        cause_id=cause_id
        )
    return institution


def get_all_institutions():
    """ Return all institutions """
    return Institution.query.all()


def get_inst_by_id(inst_id):
    """ Return institution by id """

    return Institution.query.filter(Institution.inst_id==inst_id).first()


def get_inst_by_email(inst_email):
    """ Return institution by email """

    return Institution.query.filter(Institution.inst_email==inst_email).first()


def get_insts_by_cause(cause_id):
    """ Return institution by cause_name """

    return Institution.query.filter(Institution.cause_id==cause_id).all() 



def get_inst_by_event(event_id):
    """ Return institutions by event_id """

    institutions = Institution.query.all() 
    
    for inst in institutions: 
        for event in inst.events:          
            if event.event_id == event_id:
                return inst.inst_id




# --------------- Event functions ---------------

#Do I need to add volunteer, inst and comments as parameters?
def create_event(evt_title, evt_date, evt_start_time, evt_end_time, evt_address, evt_city, evt_state, evt_lat, evt_lng, inst_id, evt_description, evt_pic):
    """ Create and return an event """
    evt_pic = "/static/images/backgorund/Screenshot.png"
    new_event = Event(
        evt_title=evt_title, 
        evt_date=evt_date, 
        evt_start_time=evt_start_time, 
        evt_end_time=evt_end_time, 
        evt_address=evt_address,
        evt_city=evt_city,
        evt_state=evt_state, 
        evt_lat=evt_lat, 
        evt_lng=evt_lng, 
        inst_id=inst_id, 
        evt_description=evt_description,
        evt_pic=evt_pic
        )
    return new_event


def create_volunteer_evt(volunteer_id, event_id):
    """ Create and return a new event that volunteer signed up """

    volunteer_evt = VolunteerEvt(
        volunteer_id=volunteer_id,
        event_id=event_id
    )
    return volunteer_evt 

def get_all_events():
    """ Return all the events """

    events = Event.query.all()
    return events


def get_events_by_city(city):
    """ Return all the events by given location """

    return Event.query.filter(Event.evt_city==city).all()


def get_event_by_id(event_id):
    """ Return event by its id """

    return Event.query.get(event_id)




def get_events_by_volunteer_id(volunteer_id):
    """ Return events that given volunteer signed up """

    events_volunteer_id = Event.query.join(VolunteerEvt).filter_by(volunteer_id=volunteer_id).all()
    return events_volunteer_id


def event_is_saved(volunteer_id, event_id):
    """ Return true if volunteer already has this event signed up """

    # All the events entries by the volunteer.
    events_volunteer_id = VolunteerEvt.query.filter_by(volunteer_id=volunteer_id).all()

    for event in events_volunteer_id:
        if int(event_id) == event.event_id:
            return True
    return False


def get_events_by_cause(cause_id):
    """ Return events by cause_name """

    # Getting the institutions by X cause
    institutions = Institution.query.filter(Institution.cause_id==cause_id).all()

    # Getting the events by X institutions
    events = []
    for inst in institutions:
        events.append(inst.events)
    return events 


def get_event_by_city_state(city, state):
    """ Return all the events by the city and state """

    return Event.query.filter(Event.evt_city==city, Event.evt_state == state).all()


def get_event_by_city_cause(city, state, cause_name):
    """ Return all the events by the city, state and cause_name """

    #getting cause_id by the cause_name
    cause = Cause.query.filter(Cause.cause_name==cause_name).first()

    # Getting the institutions by X cause
    institutions = Institution.query.filter(Institution.cause_id==cause.cause_id).all()

    # Getting the events by X institutions
    all_events = []
    for inst in institutions:
        for event in inst.events:        
            all_events.append(event)

    # Getting the events in specific city and state
    events = []
    for event in all_events:
        if event.evt_city == city and event.evt_state == state:
            events.append(event)

    return events


def get_events_by_city_state_skill(city, state, skill):
    """ Return all the events by the city, state and cause_name """

    events = Event.query.join(EventSkill).filter(Event.evt_city == city and Event.evt_state == state and EventSkill.skill_id.in_(skill)).all() 
   
    return events

    
def get_event_by_skill(skill_id):
    """ Return the events by given skill_id """

    events = Event.query.join(EventSkill).filter_by(skill_id=skill_id).all()




# --------------- Ulpload pictures functions ---------------

def update_profile_pic():
    pass
    

# --------------- Cause functions ---------------


def create_cause(cause_name, cause_title, cause_icon):
    """ Create and return a cause """

    cause = Cause(
                    cause_name=cause_name,
                    cause_title=cause_title,
                    cause_icon=cause_icon
                    ) 
    return cause


def get_all_causes():
    """ Return all the causes """

    return Cause.query.all()  


def get_cause_by_event(event_id):
    """ Return the cause of the given event_id """

    #need to access the event cause.
    institutions_events = Institution.query.join(Event).filter_by(event_id=event_id).first()
    return institutions_events.cause_id



def get_cause_by_cause_id(cause_id):
    """ Return the cause by the cause_id """

    return Cause.query.get(cause_id)


# ------------------------ Skill functions ----------------------------


def create_skill(skill_name, skill_title):
    """ Create and return a new skill """

    skill = Skill(
                skill_name=skill_name,
                skill_title=skill_title
                )
    return skill


def get_all_skills():
    """ Return all the skills """

    return Skill.query.all()


def create_volunteer_skill(volunteer_id, skill_id):
    """ Create and return a new skill assigned to volunteer """

    volunteer_skill = VolunteerSkill(
            volunteer_id=volunteer_id,
            skill_id=skill_id
            )
    return volunteer_skill


def get_skills_by_volunteer(volunteer_id):
    """ Return the skills by given volunteer_id """

    skills_volunteer = Skill.query.join(VolunteerSkill).filter_by(volunteer_id=volunteer_id).all()
    return skills_volunteer
    

def get_skills_id_by_skill_obj(skills):
    """ Return  a list of skill_id by a list of skills object """

    skills_id = []
    for skill in skills:
        skills_id.append(skill.skill_id)
    return skills_id


def create_event_skill(event_id, skill_id):
    """ Create and return a new skill assigned to event """

    event_skill = EventSkill(
            event_id=event_id,
            skill_id=skill_id
        )
    return event_skill

def get_skills_by_event(event_id):
    """ Return the skills by given event """

    skills_event = Skill.query.join(EventSkill).filter_by(event_id=event_id).all()
    return skills_event



# ----------------------- location functions ----------------------



def get_city_by_vol(volunteer_id):
    """ Return the city of volunteer by volunteer_id """

    volunteer = Volunteer.query.filter_by(volunteer_id=volunteer_id).first()
    return volunteer.v_city


def get_state_by_vol(volunteer_id):
    """ Return the state of volunteer by volunteer_id """
    
    volunteer = Volunteer.query.filter_by(volunteer_id=volunteer_id).first()
    return volunteer.v_state





# -------------------------- Comment and Review functions --------------------------


def create_inst_comment(comment, review, inst_id, volunteer_id):
    """ Create a comment/review in institution page by volunteer """

    new_comment = VolunteerComment(
        comment=comment, 
        review=review,
        inst_id=inst_id, 
        volunteer_id=volunteer_id
        )
    return new_comment


def get_reviews_by_inst(inst_id):
    """ Get the reviews of X institution """

    comments = VolunteerComment.query.filter(VolunteerComment.inst_id==inst_id).all()
    return comments


def get_review_by_id(comment_id):
    """ Get the review by comment_id """

    review = VolunteerComment.query.filter_by(comment_id=comment_id).first()
    return review


def delete_comment_by_id(comment_id):
    """ Delete from the db comment by comment_id """

    comment = VolunteerComment.query.get(comment_id)
    db.session.delete(comment)
    db.session.commit()