from flask import Flask, jsonify, request

db = [] # defined in the global section of the module

app = Flask(__name__) #class flask functions are saved to variable app


def add_patient_to_db(name, id, age):
    new_patient = {
        "name": name,
        "id": id,
        "age": age,
        "tests": []
    }
    db.append(new_patient) #patient added to DB
    print("db is {}".format(db)) ## CAN BE REPLACED WITH LOGGING FILE
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
    return "Patient added", 200


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


@app.route("/add_test", methods = ["POST"])
def post_add_test():
    """
    Recieve the posting json
    Verify the json contains the correct keys and data
    Verify that the patient id exists in database
    If data is bad, reject request with bad status to client
    If data is good, add test results to indicated patient
    return good status to client
    """
    in_dict = request.get_json()                                    #Recieve the posting json
    check_result = verify_add_test_info(in_dict)                 #Verify the json contains the correct keys and data
    if check_result is not True:
        return check_result, 400                                    #If data is bad, reject request with bad status to client
    if is_patient_in_database(in_dict["id"]) is False               #Verify that the patient id exists in database
        return "Patient {} is not found on server".format(in_dict["id"]), 400
    add_result = add_test_to_patient(in_dict)
    if add_result: #if True add test results to indicated patient
        return "test added to patient id {}".format(in_dict["id"]), 200
    else:
        return "Uknown Problem", 400


def verify_add_test_info(in_dict):
   # {"id": int, "test_name": str, "test_result", int}
    expected_keys = ("name", "id", "test_result")
    expected_types = (int, str, int)
    for i, key in enumerate(expected_keys):
        if key not in in_dict.keys():
            return "{} key not found".format(key)
        if type(in_dict[key]) is not expected_types[i]:
            return "{} value not correct type".format(key)
    return True

def is_patient_in_database():
    for patient in db:
        if patient["id"] == id:
            return True
    return False #if we don't find id in database


def add_test_to_patient(in_dict):
    for patient in db:
        if patient["id"] == in_dict["id"]:
            patient["tests"].append(in_dict["test_name"],
                                     in_dict["test_result"])
            print("db is {}".format(db))
            return True
    return False

if __name__ == '__main__':
    init_database() #starts code with intial patient data before server
    app.run()
