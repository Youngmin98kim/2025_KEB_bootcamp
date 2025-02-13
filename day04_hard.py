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

#@time_decorator
def factorial_repitition(n) -> int:
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result

number = int(input())
ft = time_decorator(factorial_repitition)
print(f"{number}! = {ft(number)}")
number = int(input())
print(f"{number}! = {factorial_repitition(number)}")
# decorator
def description(f):  # closure
    def inner(*args):
        print(f.__name__)
        print(f.__doc__)
        r = f(*args) #함수 실행 가변매개변수를 인자로 받는다
        return r

    return inner


def squares(n):
    """
    제곱 함수
    """
    return n * n

@description
def power(b, e):
    """
    거듭제곱 함수
    """
    result = 1
    for _ in range(e):
        result = result * b
    return result

print(squares(7))
f1 = description(squares)
print(f1(9))
print(power(2, 10))


# f2 = description(power)
# print(f2(2, 10))

# print(squares(7))
# print(squares.__doc__)

# def my_range(first=0, last=5, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# r = my_range()
# print(r, type(r))
#
# for x in r:
#     print(x)
# for x in r:
#     print(x)
