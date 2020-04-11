## **Routes**

 Post /new_patient

    {"name": str, "id":int, "age", int}

 Post /add_test

    {"id":int, "test_name": str, "test_result", int}

Get /get_results/<patient_id>

## **Database**

A list of dictionaries, with each dictionary as follows:

    {
    "name": str, "id": int, "age": int,
    "tests": list of tuples of (test_name: str, test_result: int)
    }