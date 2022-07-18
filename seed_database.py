"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
from model import db, connect_to_db
import server

os.system("dropdb project")
os.system("createdb project")

connect_to_db(server.app)
db.create_all()

# --------------------- causes --------------------

advocacy = crud.create_cause("humans", "Advocacy and Human Rights", "/static/images/iconlaw.png")
animals = crud.create_cause("animals", "Animals", "/static/images/animals.png")
art = crud.create_cause("arts", "Arts and Culture", "/static/images/arts.png")
children = crud.create_cause("child", "Children and Youth", "/static/images/children.png")
education = crud.create_cause("education", "Education", "/static/images/education.png")
environment = crud.create_cause("enviromnent", "Environment", "/static/images/environment.png")
homeless = crud.create_cause("homeless", "Homeless and Housing", "/static/images/homeless.png")
health = crud.create_cause("health", "Health", "")
hunger = crud.create_cause("hunger", "Hunger", "/static/images/hunger.png")
immigrants = crud.create_cause("immigrants", "Immigrants and Refugees", "/static/images/immigrants.png")
lgbtq = crud.create_cause("lgbqt", "LGBTQ+", "/static/images/lgbqt.png")
race = crud.create_cause("race", "Race and Ethnicity", "/static/images/race.png")
women = crud.create_cause("women", "Women", "/static/images/women.png")
other = crud.create_cause("other", "Others", "/static/images/other.png")

db.session.add_all([advocacy, animals, art, children, education, environment, homeless, health, hunger, immigrants, lgbtq, race, women, other])
db.session.commit()


# ------------------ skills ------------------


ani = crud.create_skill("animal_care", "Animal & Envr. - Animal Care / Handling")
agr = crud.create_skill("agronomy", "Animal & Envr. - Agronomy")
bot = crud.create_skill("botany", "Animal & Envr. - Botany")
gar = crud.create_skill("gardening", "Animal & Envr. - Gardening")
vet = crud.create_skill("vet", "Animal & Envr. - Veterinary")

dan = crud.create_skill("dance", "Arts - Dance")
dra = crud.create_skill("drawing", "Arts - Drawing")
mus = crud.create_skill("music", "Arts - Music")
pho = crud.create_skill("photography", "Arts - Photography")


acc = crud.create_skill("accounting", "Business - Accounting")
bus = crud.create_skill("business", "Business - Business Development & Management")

adu = crud.create_skill("adult_education", "Education - Adult Education")
ame = crud.create_skill("asl", "Education - American Sign Language")
cro = crud.create_skill("comunication", "Education - Cross-Cultural Communication")
tea = crud.create_skill("teach", "Education - Teaching / Instruction")

chic = crud.create_skill("child_care", "Healthcare - Child Care")
chid = crud.create_skill("child_develop", "Healthcare - Child Development")
den = crud.create_skill("dental", "Healthcare - Dental Care")
eld = crud.create_skill("elder", "Healthcare - Elder Care")

cons = crud.create_skill("construction", "Housing - Construction")
ele = crud.create_skill("electrical", "Housing - Electrical")
hom = crud.create_skill("home", "Housing - Home Repair")
lan = crud.create_skill("landscape", "Housing - Landscaping")
plu = crud.create_skill("plumbing", "Housing - Plumbing")
woo = crud.create_skill("wood", "Housing - Woodworking")



foo = crud.create_skill("food", "Food - Food Service")
coo = crud.create_skill("cooking", "Food - Cooking / Catering")
nut = crud.create_skill("nutrition", "Food - Nutrition")



adv = crud.create_skill("advocacy","Legal - Advocacy")
chia = crud.create_skill("child_adv", "Legal - Child Advocacy")   
con = crud.create_skill("conflit", "Legal - Conflit Resolution")



db.session.add_all([ani, agr, bot, gar,vet,dan,dra, mus, pho, acc, bus, adu, ame,cro, tea, chic, chid, den, eld, cons,  ele, hom, lan, plu, woo, foo, coo, nut, adv, chia, con,])
db.session.commit()



# -------------- institution -----------------

# ------------------- volunteer -------------------


# --------------------- comments --------------------

# test1 = crud.create_inst_comment("I loved to work with this institution!", 5, 2, 1)
# test2 = crud.create_inst_comment("I hated to work with this institution!!!!!", 1, 2, 1)

# db.session.add_all([test1, test2])
# db.session.commit()



