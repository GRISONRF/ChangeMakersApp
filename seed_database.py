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


advocacy = crud.create_cause("Advocacy and Humans Rights")
animals = crud.create_cause("Animals and Enviroment")
art = crud.create_cause("Arts and Culture")
children = crud.create_cause("Children and Youth")
education = crud.create_cause("Education")
hunger = crud.create_cause("Hunger")
homeless = crud.create_cause("Homeless and Housing")
immigrants = crud.create_cause("Immigrants and Refugees")
lgbtq = crud.create_cause("LGBTQ+")
race = crud.create_cause("Race and Ethnicity")
women = crud.create_cause("Women")

db.session.add_all([advocacy, animals, art, children, education, hunger, homeless, immigrants, lgbtq, race, women])

db.session.commit()