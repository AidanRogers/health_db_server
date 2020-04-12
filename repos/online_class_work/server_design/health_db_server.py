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


@app.route("/new_patient", methods = ["POST"])
def post_new_patient():
    """
    Recieve the posting json
    Verify the json contains the correct keys and data
    If data is bad, reject request with bad status to client
    If data is good, add patient to database
    return good status to client
    """
    in_dict = request.get_json()                                    #Recieve the posting json
    check_result = verify_new_patient_info(in_dict)                 #Verify the json contains the correct keys and data
    if check_result is not True:
        return check_result, 400                                    #If data is bad, reject request with bad status to client
    add_patient_to_db(in_dict["name"], in_dict["id"], in_dict["age"]) #If data is good, add patient to database
    return "Patien added", 200

        

#Function that has a dictionary that comes has the appropriate keys in it
    #{"name": str, "id":int, "age", int} = in_dict.keys
def verify_new_patient_info(in_dict):
    expected_keys = ("name", "id", "age")
    expected_types = (str, int, int)
    for i, key in enumerate(expected_keys):
        if key not in in_dict.keys():
            return "{} key not found".format(key)
        if type(in_dict[key]) is not expected_types[i]:
            return "{} value not correct type".format(key)
    return True



if __name__ == '__main__':
    init_database() #starts code with intial patient data before server
    app.run()

