info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]
  # Q - 1
unique_cource = set()

for tup in info:
    # print(tup[0])  #name
    unique_cource.add(tup[1])  #cource

print(unique_cource)


# Q - 2
for name,course in info:
    if(course == "English"):
        print(name)
  
  # Q-3

dict = {}

for name,course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)