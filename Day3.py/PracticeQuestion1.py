info = [
    ("Alice" , "Math"),
    ("Bob" , "Science"),
    ("Alice" , "Science"),
    ("Charlie" , "Math"),
    ("Bob" , "Math"),
    ("Alice" , "English"),
    ("Charlie" , "English"),
]

# Unique_Cources = set()


# for tup in info:
#     # print(tup[0])
#     Unique_Cources.add(tup[1])

# print(Unique_Cources)



# unique_set = set()

# for name,cource in info:
#     if(cource == "English"):
#         print(name)


dict = {}
for name,cource in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(cource)
    else:
        dict[name].add(cource)

print(dict)