"""Models for my nameless app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Volunteer(db.Model):
    """ A volunteer """

    __tablename__ = 'volunteers'

    volunteer_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    v_email = db.Column(db.String(70), unique=True, nullable=False)
    v_password = db.Column(db.String(15), nullable=False)
    v_city = db.Column(db.String(60), nullable=False)
    v_state = db.Column(db.String(60), nullable=False)
    v_pic = db.Column(db.String, nullable=True)

    favorites = db.relationship("Institution", secondary="favorites", backref="volunteers")  #
    events = db.relationship("Event", secondary="volunteer_evt", backref="volunteers")   
    comments = db.relationship("VolunteerComment", back_populates="volunteer")
    skills = db.relationship("Skill", secondary="volunteer_skill", backref="volunteers")

    def __repr__(self):
        return f'<< Volunteer volunteer_id={self.volunteer_id} fname={self.fname} lname={self.lname} v_email={self.v_email} v_password={self.v_password} v_city={self.v_city} v_state={self.v_state} v_pic={self.v_pic} >>'


class Favorite(db.Model):
    """ Association table - 'My favorites' section """

    __tablename__ = 'favorites'

    fav_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.volunteer_id'))
    inst_id = db.Column(db.Integer, db.ForeignKey('institutions.inst_id'))
     

    def __repr__(self):
        return f'<< Favorite fav_id={self.fav_id} volunteer_id={self.volunteer_id} inst_id={self.inst.id} >>'


class Cause(db.Model):
    """ A cause """

    __tablename__ = 'causes'

    cause_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    cause_name = db.Column(db.String(100), nullable=False)
    cause_title = db.Column(db.String(50), nullable=False)
    cause_icon = db.Column(db.String(100))

    insts = db.relationship("Institution", back_populates="cause")
 

    def __repr__(self):
        return f'<< Cause cause_id={self.cause_id} cause_name={self.cause_name} cause_title={self.cause_title} cause_icon={self.cause_icon} >>'


class Institution(db.Model):
    """ A institution """

    __tablename__ = 'institutions'

    inst_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    inst_name = db.Column(db.String(100), unique=True, nullable=False)
    inst_email = db.Column(db.String(60), unique=True, nullable=False)
    inst_password = db.Column(db.String(15), nullable=False)
    inst_address = db.Column(db.String(500), nullable=False)
    inst_city = db.Column(db.String(60), nullable=False)
    inst_state = db.Column(db.String(60), nullable=False)
    inst_lat = db.Column(db.Float)
    inst_lng = db.Column(db.Float)
    inst_pic = db.Column(db.String, nullable=True)
    cause_id = db.Column(db.Integer, db.ForeignKey('causes.cause_id'))

 
    events = db.relationship("Event", back_populates="inst")
    #free at. volunteers
    cause = db.relationship("Cause", back_populates="insts")
    comments = db.relationship("VolunteerComment", back_populates="inst")

    def __repr__(self):
        return f'<< Institution inst_id={self.inst_id} inst_name={self.inst_name} inst_email={self.inst_email} inst_password={self.inst_password} inst_address={self.inst_address} inst_city={self.inst_city} inst_state={self.inst_state} inst_lat={self.inst_lat} inst_lng={self.inst_lng} inst_pic={self.inst_pic} cause_id={self.cause_id} >>'
 

class VolunteerEvt(db.Model):
    """ Association Table - Event of specific Volunteer. """

    __tablename__ = 'volunteer_evt'

    vol_evt_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.volunteer_id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))

    # volunteer_evt = db.relationship("Event", secondary="volunteer_evt", backref="volunteers")


    def __repr__(self):
        return f'<< VolunteerEvt vol_evt_id={self.vol_evt_id} volunteer_id={self.volunteer_id} event_id={self.event_id} >>'


class Event(db.Model):
    """ An Event """

    __tablename__ = 'events'

    event_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    evt_title = db.Column(db.String(100), nullable=False)
    evt_date = db.Column(db.String)
    evt_start_time = db.Column(db.String)
    evt_end_time = db.Column(db.String)
    evt_address = db.Column(db.String, nullable=False)
    evt_city = db.Column(db.String(60), nullable=False)
    evt_state = db.Column(db.String(60), nullable=False)
    evt_lat = db.Column(db.Float)
    evt_lng = db.Column(db.Float)
    evt_description = db.Column(db.Text)
    inst_id = db.Column(db.Integer, db.ForeignKey('institutions.inst_id'))
    
    skills = db.relationship("Skill", secondary="event_skill", backref="events")
    inst = db.relationship("Institution", back_populates="events")
    # volunteers for free  
    


    def __repr__(self):
        return f'<< Event event_id={self.event_id} evt_title={self.evt_title} evt_date={self.evt_date} evt_start_time={self.evt_start_time} evt_end_time={self.evt_end_time} evt_address={self.evt_address} evt_city={self.evt_city} evt_state={self.evt_state} evt_lat={self.evt_lat} evt_long={self.evt_lng} evt_description={self.evt_description} inst_id={self.inst_id} >>'


class VolunteerComment(db.Model):
    """ Volunteer comment """

    __tablename__ = 'volunteer_comments'

    comment_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    comment = db.Column(db.Text)
    review = db.Column(db.Integer)
    inst_id = db.Column(db.Integer, db.ForeignKey('institutions.inst_id'))
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.volunteer_id'), nullable=False)


    inst = db.relationship("Institution", back_populates="comments")
    volunteer = db.relationship("Volunteer", back_populates="comments")

    def __repr__(self):
        return f'<< VolunteerComment comment_id={self.comment_id} comment={self.comment} rate={self.review} inst_id={self.inst_id} volunteer_id={self.volunteer_id} >>'


class Skill(db.Model):
    """ A Skill """

    __tablename__ = 'skills'

    skill_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    skill_name = db.Column(db.String(30), nullable=False)
    skill_title = db.Column(db.String(100), nullable=False)

    #volunteers for free:
    #skills = db.relationship("Skill", secondary="volunteer_skill", backref="volunteers")
    #events for free:
    #skills = db.relationship("Skill", secondary="event_skill", backref="events")

    def __repr__(self):
        return f'<< Skill skill_id={self.skill_id} skill_name={self.skill_name} skill_title={self.skill_title} >>'


class VolunteerSkill(db.Model):
    """ a volunteer skill """

    __tablename__ = 'volunteer_skill'

    volunteer_skill_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.volunteer_id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.skill_id'))

    def __repr__(self):
        return f'<< VolunteerSkill volunteer_skill_id={self.volunteer_skill_id} volunteer_id={self.volunteer_id} skill_id={self.skill_id} >>'



class EventSkill(db.Model):
    """ A Event Skill """

    __tablename__ = 'event_skill'

    event_skill_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.skill_id'))

    def __repr__(self):
        return f'<< EventSkill event_skill_id={self.event_skill_id} event_id={self.event_id} skill_id={self.skill_id} >>'



def connect_to_db(flask_app, db_uri="postgresql:///project", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    
    connect_to_db(app)
    db.create_all()