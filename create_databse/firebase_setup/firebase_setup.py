# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import darak_db
import shah_db
import jain_db

try:
    app = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate('facultyanalysis-firebase-adminsdk-igxdd-a0b84ac544.json')
    
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://facultyanalysis.firebaseio.com/'
    })
    

darak_data=darak_db.create_db()
shah_data=shah_db.create_db()
jain_data=jain_db.create_db()


with open("darak_data.json", "w") as outfile: 
    outfile.write(json.dumps(darak_data))
    
with open("shah_data.json", "w") as outfile: 
    outfile.write(json.dumps(shah_data))

with open("jain_data.json", "w") as outfile: 
    outfile.write(json.dumps(jain_data))

ref = db.reference('/')

# ref.set(darak_data)
# ref.set(str(shah_data))
# ref.set(jain_data)



