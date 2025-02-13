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
# decorator
def description(f):  # closure
    def inner(*args):
        print(f.__name__) #__ __ 를 magic method라고 함.
        print(f.__doc__)
        r = f(*args) #함수 실행 가변매개변수를 인자로 받는다
        return r

    return inner

@time_decorator
@description
def factorial_repitition(n) -> int:
    """
    팩토리얼 함수
    :return: results of factorial operation
    """
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result

#int(description(factorial_repitition(int(input())))) : 함수를 감싸는 것이 아니라 반환값을 감싸게 되어 오류
#@description만 씌운 상태에서 time_decorator를 씌우려면 : dec = time_decorator(factorial_repititions())
number = int(input())
print(f'{number} = {factorial_repitition(number)}')
def squares(n):
    """
    제곱 함수
    """
    return n * n

