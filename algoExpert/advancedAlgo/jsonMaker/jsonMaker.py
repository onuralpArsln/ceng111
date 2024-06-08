import json

jhon = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("output.json" ,"w") as json_file:
    json.dump(jhon,json_file,indent=2)
    # indent for better readiblity