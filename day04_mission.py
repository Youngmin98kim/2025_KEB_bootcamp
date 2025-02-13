# #SOLID  open closed principle 개방 폐쇄 원칙 (확장에는 열려있고 수정에는 닫혀있음)
# import time
#
# def time_decorator(func):
#     def wrapper(*args):
#         s = time.time()
#         r = func(*args)
#         e = time.time()
#         print(f'실행 시간 : {e-s}sec')
#         return r
#     return wrapper
# # decorator
# def description(f):  # closure
#     def inner(*args):
#         print(f.__name__) #__ __ 를 magic method라고 함.
#         print(f.__doc__)
#         r = f(*args) #함수 실행 가변매개변수를 인자로 받는다
#         return r
#
#     return inner
#
# @time_decorator
# @description
# def factorial_repitition(n) -> int:
#     """
#     팩토리얼 함수
#     :return: results of factorial operation
#     """
#     result = 1
#     for i in range(2,n+1):
#         result = result * i
#     return result
#
# #description(factorial_repitition(int(input()))) : 함수를 감싸는 것이 아니라 반환값을 감싸게 되어 오류, 변수 선언을 해줘야 함.
# #@description만 씌운 상태에서 time_decorator를 씌우려면 : dec = time_decorator(factorial_repitition), input 은 분리
# number = int(input())
# t = description(time_decorator(factorial_repitition))
# print(f"{number}! = {t(number)}")

#로그를 남기는 데코레이터
def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Function Name : {func.__name__}")
        print(f"Function Arguments : {args}")
        print(f"Function Keyword Arguments : {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

## kwargs 를 사용한 데코레이터 예제
@log_decorator
def greet(name,greeting = "안녕하세요",**kwargs):
    message = f"{greeting}. {name}입니다."
    if kwargs:
        message += " 추가 정보: " + ", ".join(f"{key}: {value}" for key, value in kwargs.items())
    return message
# def greet(name,greeting = "안녕하세요",age=None):
#     return f"{greeting},{name}, age : {age}" if age else f"{greeting},{name}"

print(greet("인하"))
print(greet("James","Hello"))
print(greet("Gonzales","Hola"))
print(greet("Nakamura","Gonniziwa",age=29))



