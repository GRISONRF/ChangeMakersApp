"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
from model import db, connect_to_db
import server

os.system("dropdb project")
os.system('createdb project')

connect_to_db(server.app)
db.create_all()


advocacy = crud.create_cause("Advocacy and Human Rights", "static/images/humansrights.png")
animals = crud.create_cause("Animals", "static/images/animals.png")
art = crud.create_cause("Arts and Culture", "static/images/arts.png")
children = crud.create_cause("Children and Youth", "static/images/children.png")
education = crud.create_cause("Education", "static/images/education.png")
environment = crud.create_cause("Environment", "static/images/environment.png")
hunger = crud.create_cause("Hunger", "static/images/hunger.png")
homeless = crud.create_cause("Homeless and Housing", "static/images/homeless.png")
immigrants = crud.create_cause("Immigrants and Refugees", "static/images/immigrants.png")
lgbtq = crud.create_cause("LGBTQ+", "static/images/lgbqt.png")
race = crud.create_cause("Race and Ethnicity", "static/images/race.png")
women = crud.create_cause("Women", "static/images/women.png")

db.session.add_all([advocacy, animals, art, children, education, hunger, homeless, immigrants, lgbtq, race, women])

db.session.commit()