# infinite loop

print 1 to 10
i = 1

while i <= 10: 
    print("Hello world" , i)
    i +=1
print("after loop, count = ", i)



# reverse 1 to 5
i = 5

while i >= 1:
    print(i)
    i-=1



# print 0 to 4
i = 0
while ( i < 5):
    print(i)
    i+=1


#  Multiplication table of any number
table = int(input("Enter the number :"))
i = 1

while ( i <= 10):
    print(table,"X",i,"=",table * i )
    i+=1
  



# use break Keyword 


i = 1
while( i <= 10):
    if(i % 6 == 0):
        break
    print(i)
    i+=1  # update

print("Outside Loop Now .......")


# use continue Keyword to ship only 3

i = 1
while( i <= 5):
    if(i % 3 == 0):
        i+=1
        continue
    print(i)
    i+=1

print("Outside Loop now .....")


i = 0

while( i < 10):
    i+=1
    if(i % 2 == 0):
        continue
    print(i)