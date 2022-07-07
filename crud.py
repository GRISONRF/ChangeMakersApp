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

    return Institution.query.filter(Institution.cause_id==cause_id).all() #all insts by that cause



def get_inst_by_event(event_id):
    """ Return institutions by event_id """


 
    # institution = Institution.query.join(Event).filter_by(event_id=event_id).all()
    # return institution



    institutions = Institution.query.all() #[<< Institution inst_id=1 inst_name=blabla....>> <<Institution inst_id=2 ....>>]
    
    for inst in institutions: #<< Institution inst_id=1 inst_name=blabla....>>
        for event in inst.events:          
            if event.event_id == event_id:
                return inst.inst_id



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
def create_event(evt_title, evt_date, evt_start_time, evt_end_time, evt_address, evt_city, evt_state, evt_lat, evt_lng, inst_id, evt_description):
    """ Create and return an event """

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
        evt_description=evt_description
        )
    return new_event


def get_all_events():
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
    print(institutions)

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



    # Getting the events_id:
    # events_id = [] #[1, 3, 5]
    # for event in events:
    #     events_id.append(event.event_id)
    # # print("\n" * 5)
    # # print("************events_id:******************")
    # # print(events_id)
    # # print("\n" * 5)

    # # Find the skills for the events
    # event_skills_id = [] #[1, 2, 4, 3, 7, 5, 8, 10]

    # for id in events_id:
    #     skills = Skill.query.join(EventSkill).filter_by(event_id=id).all()
    #     for skill in skills:
    #         if skill.skill_id not in event_skills_id:
    #             event_skills_id.append(skill.skill_id)

    # # print("\n" * 5)
    # # print("************event_skills_id2:******************")
    # # print(event_skills_id) 
    # # print("\n" * 5)
    # # print("************volunteer_skill_id:******************")
    # # Check if volunteer skills matches event skill

    # # Find volunteer skills:
    # volunteer = Skill.query.join(VolunteerSkill).filter_by(volunteer_id=volunteer_id).all()
    # # print('VOLUNTEER:')
    # # print(volunteer)
    # # print('VOLUNTEER')
    # #getting volunteer skills_id:
    # volunteer_skills_id = [] # [1, 2, 4]
    # for v_skill in volunteer:
    #     # print(v_skill)
    #     # print('***** v_skill_id*****')
    #     volunteer_skills_id.append(v_skill.skill_id)

    # # print(volunteer_skills_id)
    # # print("\n" * 5)

    # # print("************volunteer_skills id loop: ******************")
    # # Match event skills and volunteer skills
    # matched_skills_events = []
    # for skill in volunteer_skills_id:   #[1, 2, 4]
    #     # print(skill)
    #     # print("\n" * 5)
    #     # print("************matched skills******************")
    #     for e_skill in event_skills_id:
        
    #         if skill == e_skill: #[1, 2, 4, 3, 7, 5, 8, 10] 
    #             # Want to return events that matched the eventSkill
    #             #(return the event that has this skill_id)
    #             event_skill = Event.query.join(EventSkill).filter_by(skill_id=skill).all()
            
    #             matched_skills_events.extend(event_skill)

    # # print(set(matched_skills_events))
    # return set(matched_skills_events)


    
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


def get_cause_by_event(event_id):
    """ Return the cause of the given event_id """

    #need to access the event cause.
    institutions_events = Institution.query.join(Event).filter_by(event_id=event_id).first()
    print('\n' * 8)
    print(institutions_events.cause_id)
    return institutions_events.cause_id
 


def get_events_by_cause(cause_id):
    """ Return events by cause_name """

    # Getting the institutions by X cause
    institutions = Institution.query.filter(Institution.cause_id==cause_id).all()

    # Getting the events by X institutions
    events = []
    for inst in institutions:
        events.append(inst.events)
    return events 


def get_cause_by_cause_id(cause_id):
    """ Return the cause by the cause_id """

    return Cause.query.get(cause_id)


# ----------------------- location functions ----------------------



def get_city_by_vol(volunteer_id):
    """ Return the city of volunteer by volunteer_id """

    volunteer = Volunteer.query.filter_by(volunteer_id=volunteer_id).first()
    return volunteer.v_city


def get_state_by_vol(volunteer_id):
    """ Return the state of volunteer by volunteer_id """
    
    volunteer = Volunteer.query.filter_by(volunteer_id=volunteer_id).first()
    return volunteer.v_state
