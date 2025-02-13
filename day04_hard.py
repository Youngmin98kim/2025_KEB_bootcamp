#SOLID  open closed principle 개방 폐쇄 원칙 (확장에는 열려있고 수정에는 닫혀있음)
import time

def time_decorator(func):
    def wrapper(*args):
        s = time.time()
        r = func(*args)
        e = time.time()
        print(f'실행 시간 : {e-s}sec')
        return r
    return wrapper

@time_decorator
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
