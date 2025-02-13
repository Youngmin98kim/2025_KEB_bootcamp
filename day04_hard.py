#SOLID
import time

def factorial_repitition(n) -> int:
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result

number = int(input())
s = time.time()
print(f"{number}! = {factorial_repitition(number)}")
e = time.time()
print(e-s)
