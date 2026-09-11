# def hello():
#     for i in range(1,5+1,1):
#         print("Hello world")


# print("Hello my name is mohit")
# hello()
# hello()

# def hello(a,b):
#     sum = a + b
#     return sum


# ans = hello(10,20)
# print(ans)

# print(hello(3,4))


# def Avg(a,b,c):
#     A = (a+b+c)/3
#     return A


# print(Avg(5,10,15))


# Avg = lambda a, b, c : (a + b + c )/3
# print(Avg(4,5,7))



def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i 
        
    return fact

n = int(input("Enter n :"))
print(factorial(n))