def is_prime(num: int) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num < 2:  # 2 미만의 숫자는 소수가 아님
        return False

    for i in range(2, int(num ** 0.5) + 1):  # 2부터 √num까지 확인
        if num % i == 0:
            return False  # 약수가 있으면 소수 아님

    return True  # 위 조건을 통과하면 소수


# main
#help(abs)
help(is_prime) #설명해주는 애 햐ㅎ
n = int(input("Input number: "))

if is_prime(n):  # function call
    print(f"{n} is a prime number")
else:
    print(f"{n} is NOT a prime number!")


univ = "Inha university"
print(univ)
print(univ[5])
univ[5] ='U' #immutable 문자열
print(univ) #
subjects = ['python','c++','Linux','data structure','data base']
subjects[3] = 'data structure and algorithm' #mutable

print(0.1)
print(1e-1)  #0.1
print(21_000) #21000
print(0.3141592e3) #314.1592


