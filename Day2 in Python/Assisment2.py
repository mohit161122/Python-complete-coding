# Even number

a = int(input("Enter the starting range :"))
b = int(input("Enter the Ending range :"))

def Even(a,b):
    if (a % 2  != 0):
        a += 1
    for i in range(a , b+1,2):
        print(i)


Even(a,b)


#odd number

a = int(input("Enter the starting range :"))
b = int(input("Enter the Ending range :"))

def Even(a,b):
    if (a % 3  != 0):
        a += 1
    for i in range(a , b+1,2):
        print(i)


Even(a,b)

   