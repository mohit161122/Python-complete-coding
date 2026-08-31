set1 = {1,2,3,4,5}
set2 = {4,5,8,9,10}

print(type(set))
print(len(set))


set.add(5)
print(set)

set.add(5)
set.remove(1)
set.clear()


print(set)
set.pop()
print(set)

print(set1.union(set2))
print(set1.intersection(set2))
