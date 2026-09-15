
# # json convert into PY_STR
# import json


# json_str = '{"name": "mohit" , "isTeacher": null}'

# py_obj = json.loads(json_str)

# print(type(py_obj) , py_obj)




## PY_obj convert into JSON

# import json

# py_Obj = {
#     "name":"mohit",
#     "isTeacher": True
# }

# json_str = json.dumps(py_Obj)
# print(type(json_str) , json_str)


# import json

# with open("data.json", "r") as f:
#     py_obj = json.load(f)
#     print( type(py_obj)  ,py_obj)


import json

data = {
    "name": "mohit",
    "age": 27,
    "isTeacher": True
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4,sort_keys=True)`1`