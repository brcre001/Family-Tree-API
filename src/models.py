from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

charlotte = {
    "id": 6,
    "name": "Charlotte",
    "children": []
}

harrison = {
    "id": 5,
    "name": "Harrison",
    "children": []
}

harry = {
    "id": 4,
    "name": "Harry",
    "children": [harrison]
}

william = {
    "id" : 3,
    "name" : "William",
    "children": [charlotte]
}

charles = {
    "id": 2,
    "name": "Charles",
    "children": [william, harry]
}

elizabeth = {
    "id": 1,
    "name": "Elizabeth",
    "children": [charles]
}

new_list = []

def list_all(parent):
    # your code goes here
    for child in parent["children"]:
        new_list.append(child)
        return list_all(child)
    return new_list

def find_one(parent, id):
    print("for loop initiated with " + parent["name"])
    for child in parent["children"]:
        print("testing for " + child["name"] + " with id " + str(child["id"]) + "==" + str(id))
        if child["id"] == id:
            print("if statement initiated")
            return child
        print("Not the id that we want, moving on")
        return find_one(child, id)
        

# print(find_one(elizabeth, 6))