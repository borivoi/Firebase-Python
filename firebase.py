# importing the module
import json
import pyrebase

# reading the data from the file
with open('config.txt') as f:
    data = f.read()

# reconstructing the data as a dictionary
config = json.loads(data)

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
database = firebase.database()

''' #set
database.child("DB Object name")
data = {"Key1": "Value1", "Key2": "Value2"}
database.set(data)
'''

''' #update
database.child("DB Object Name").update({"Key": "Value"})
'''

''' #get
accidents = database.child("DB Object Name").get()
data = accidents.val()
'''
