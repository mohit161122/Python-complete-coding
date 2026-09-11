def hello(n):
    digital = []
    while n > 0:
        digital.append(n % 10)
        n //= 10
    for d in digital:
        print(d)

hello(321)