def factorial_repetition(n) -> int:
    '''
    반복문을 이용한 팩토리얼 함수
    :param n: 정수, int
    :return: 팩토리얼 값, int
    '''
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

#반복문 재귀함수 f(n) = n * f(n-1)
def factorial_recursion(n):
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function, int
    '''
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1)

def pibo_recursion(n) -> int:
    """
    재귀함수를 이용한 피보나치 수열
    :param n: 정수, int
    :return: function, int
    """
    if n==1:
        return 1
    else :
        return pibo_recursion(n-1) + pibo_recursion(n-2)

def pibo_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

def pibo_pf(n) -> int :
    """
    피보나치 수 계산함수(재귀함수)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    if n <= 0 :
        return 0
    elif n == 1:
        return 1
    else :
        return pibo_pf(n-2)+pibo_pf(n-1)
print(pibo_pf(int(input()))) #return이 계속해서 반복되기 때문에 입력 숫자가 커지면 시간도 오래 걸린다.


number = int(input("number : "))
print(factorial_repetition(number))
print(factorial_recursion(number))
print(globals())

def fibo_loop(n) -> int : #시간 엄청 오래걸림.
    """
    반복문을 이용한 피보나치 수 계산 함수
    :param n: int
    :return: 피보나치 계산 결과 값
    """
    n_list = [0,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i+1])
    return n_list[n]
n=int(input())
print(fibo_loop(n))

def explosion(n) -> int :
    """
    재귀함수를 이용한 함수
    :param n:
    :return:
    """
    if n<=0:
        return
    print(n, end=" ")  # 현재 숫자 출력
    explosion(n - 1)  # 재귀 호출

def countdown_loop(n):
    for i in range(n, -1, -1):
        if i ==0:
            print('펑')
    else :
        print(i)

countdown_loop(int(input()))

def countdown_recursion(n):
    if n<0:#종료조건
        return
    if n==0:
        print("펑")
    else:
        print(n)
    countdown_recursion(n-1) #끝내지 않으면 계속 loop가 돌아가므로 들여쓰기 x

