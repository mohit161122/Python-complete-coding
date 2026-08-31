

info = {
    "name": 'Mohit',
    "cgpa": 9.2,
    "Subject": ["math","science"],
    3.14: "PI"
}

info["cgpa"] = 9.55
print(type(info))
print(info["cgpa"])

print(info.keys())
print(info.values())
print(info.items())
print(info.get(3.14))
info.update({
    "city": "Delghi",

})

print(info)