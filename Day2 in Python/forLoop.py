string = "hello"
for var in string:
    print(var)

string = "hello"
if "m" in string:
    print("e exists")

for i in range(1,5+1,1):
    print("Hello world")


word = "artificial intelligence"
count = 0

for ch in word:
    if(ch == "i"):
        count+=1

print("count of i =",count)


for ch in word:
     if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
        count +=1

print("Vowel are = ", count)


for i in range(1,11,2):
    print(i)

n = int(input("Enter the number :"))
sum = 0

for i in range(1,n+1):
    sum+=i
print("sum of :",sum)


