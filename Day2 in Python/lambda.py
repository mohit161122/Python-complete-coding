## lambda function

Avg = lambda a,b: a+b/2 
print(Avg(4,5))


## find a factorial 
n = int(input("Enter n: "))

def Calc_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(Calc_factorial(n))
    