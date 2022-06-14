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
    v_email = db.Column(db.String(60), unique=True, nullable=False)
    v_password = db.Column(db.String(15), nullable=False)
    v_address = db.Column(db.String(100))

    favorites = db.relationship("Institution", secondary="favorites", backref="volunteers")  #
    events = db.relationship("Event", secondary="volunteer_evt", backref="volunteers")   #FOR THE ASSOCIATION TABLE?
    # events = db.relationship("Event", back_populates="volunteers")
    comments = db.relationship("VolunteerComment", back_populates="volunteer")

    def __repr__(self):
        return f'<< Volunteer volunteer_id={self.volunteer_id} fname={self.fname} lname={self.lname} v_email={self.v_email} v_password={self.v_password} v_address={self.v_address} >>'


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


class Institution(db.Model):
    """ A institution """

    __tablename__ = 'institutions'

    inst_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    inst_name = db.Column(db.String(100), unique=True, nullable=False)
    inst_email = db.Column(db.String(60), unique=True, nullable=False)
    inst_password = db.Column(db.String(15), nullable=False)
    inst_address = db.Column(db.String(500))
 
    events = db.relationship("Event", back_populates="inst")
    #free at. volunteers
  

    def __repr__(self):
        return f'<< Institution inst_id={self.inst_id} inst_name={self.inst_name} inst_email={self.inst_email} inst_password={self.inst_password} inst_address={self.inst_address} >>'


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
    evt_title = db.Column(db.String(200), nullable=False)
    evt_date = db.Column(db.Date)
    evt_location = db.Column(db.String(200), nullable=False)
    inst_id = db.Column(db.Integer, db.ForeignKey('institutions.inst_id'))
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.volunteer_id'))

    inst = db.relationship("Institution", back_populates="events")
    # volunteers for free  
    comments = db.relationship("VolunteerComment", back_populates="event")


    def __repr__(self):
        return f'<< Event event_id={self.event_id} evt_title={self.evt_title} evt_date={self.evt_date} evt_location={self.evt_location} inst_id={self.inst_id} volunteer_id={self.volunteer_id} >>'


class VolunteerComment(db.Model):
    """ Volunteer comment """

    __tablename__ = 'volunteer_comments'

    comment_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    comment = db.Column(db.Text)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.volunteer_id'))


    event = db.relationship("Event", back_populates="comments")
    volunteer = db.relationship("Volunteer", back_populates="comments")

    def __repr__(self):
        return f'<< VolunteerComment comment_id={self.comment_id} comment={self.comment} event_id={self.event_id} volunteer_id={self.volunteer_id} >>'






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