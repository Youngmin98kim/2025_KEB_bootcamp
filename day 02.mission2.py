#def is_prime(num:int)-> bool:
#    if num < 2:
#        return False
#    i=2
#    while i <= int(num**0.5):
#        if num% i==0:
#            return False
#        i+=1
#    return True
#
#start = int(input("처음 숫자를 입력: "))
#end = int(input("나중 숫자를 입력: "))

#current = start

#while current <= end:
#    if is_prime(current):  # 소수 판별 함수 호출
  #      print(current, end=" ")  # 소수 출력
 #   current += 1  # 다음 숫자로 이동

#print("\n소수 찾기 완료!")


def is_prime(num:int)-> bool:
    numbers = input("input number : ").split()

    n1 = int(numbers[0])
    n2 = int(numbers[1])

    if n1 > n2:
        n1,n2 = n2,n1

    j=n1
    while j <= n2:
        if is_prime(j):
                 print(j,end=' ')
        j = j+1