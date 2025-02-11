def indivijual_serial(todo)-> dict:
    return {
        "id": str(todo["_id"])  ,
        "Work":todo["Work"],
         "need":todo["need"],
         "complete":todo["complete"]
    }

def list_indivijual_serial(todos)->list:
    return [indivijual_serial(todo) for todo in todos]



