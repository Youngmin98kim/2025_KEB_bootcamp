def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num < 2 :
        return False


    i=2 #while문은 초기값이 필요
    while i < (int(num ** 0.5) + 1):
         if num % i == 0:
                return False
         i += 1

    return True

# 사용자 입력받기
n = int(input("숫자를 입력하세요 : "))  # 사용자 입력

# 0을 입력하면 종료, 아니면 계속 실행
while n != 0:
    if is_prime(n):
        print(f"{n}은(는) 소수입니다!")
    else:
        print(f"{n}은(는) 소수가 아닙니다!")

    # 다음 입력 받기
    n = int(input("숫자를 입력하세요 : "))


