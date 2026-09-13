import json


json_str = '{"name":"Alice", "age": 25,}'   

py_obj = json.loads(json_str)

print(type(json_str))