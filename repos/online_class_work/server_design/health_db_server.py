from flask import Flask, jsonify, request

db = [] # defined in the global section of the module

app = Flask(__name__) #class flask functions are saved to variable app


def add_patient_to_db(name, id, age):
    new_patient = {
        "name": name,
        "id": id,
        "age": age
    }
    db.append(new_patient) #patient added to DB
    return True #to check if it works

def init_database(): #to add new patients
    add_patient_to_db("Ann Ables", 101, 35)
    add_patient_to_db("Bob Boyles", 102, 40)
    # Add Code to start the logging IF WE WERE GONNA DO ANY LOGGING

if __name__ == '__main__':
    init_database() #starts code with intial patient data before code goes
    app.run()

