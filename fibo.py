from math import sqrt

def fibo(n):
    sqrt5 = sqrt(5)
    return int((((1 + sqrt5) ** n - (1 - sqrt5) **n) / (2 ** n * sqrt5)))

print(fibo(5))
