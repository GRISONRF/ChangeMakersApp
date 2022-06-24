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


advocacy = crud.create_cause("humans", "Advocacy and Human Rights", "static/images/humansrights.png")
animals = crud.create_cause("animals", "Animals", "static/images/animals.png")
art = crud.create_cause("arts", "Arts and Culture", "static/images/arts.png")
children = crud.create_cause("child", "Children and Youth", "static/images/children.png")
education = crud.create_cause("education", "Education", "static/images/education.png")
environment = crud.create_cause("enviromnent", "Environment", "static/images/environment.png")
hunger = crud.create_cause("hunger", "Hunger", "static/images/hunger.png")
homeless = crud.create_cause("homeless", "Homeless and Housing", "static/images/homeless.png")
immigrants = crud.create_cause("immigrants", "Immigrants and Refugees", "static/images/immigrants.png")
lgbtq = crud.create_cause("lgbqt", "LGBTQ+", "static/images/lgbqt.png")
race = crud.create_cause("race", "Race and Ethnicity", "static/images/race.png")
women = crud.create_cause("women", "Women", "static/images/women.png")

db.session.add_all([advocacy, animals, art, children, education, hunger, homeless, immigrants, lgbtq, race, women])

db.session.commit()