# 거듭제곱 함수
import math
def my_power(b,e) -> float:
    """
    A function that takes a base and an exponent as input, calculates the power (exponentiation),
    and returns the result as a floating-point number.
    :param b: base number
    :param e: exponent
    :return: the power result in the form of a real number
    """
    result = 1
    for k in range(e):
        result = result * b
    return result

def is_prime(num) -> bool:

    if num >= 2:
        i=2
        while i <(int(pow(num,0.5))+1):
            if num % i ==0:
                return False
            i = i+1
        return True

n = int(input("숫자를 입력하세요 : "))  # 사용자 입력

# 0을 입력하면 종료, 아니면 계속 실행
while n != 0:
    if is_prime(n):
        print(f"{n}은(는) 소수입니다!")
    else:
        print(f"{n}은(는) 소수가 아닙니다!")

    # 다음 입력 받기
    n = int(input("숫자를 입력하세요 : "))


print(my_power(2,10))

#
print(exp(1)) #error
print(math.exp(1))
print(math.e)