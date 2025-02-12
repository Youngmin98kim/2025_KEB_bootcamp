import math
#print(exp(1)) #error
print(math.exp(1))
print(math.e)
print(math.log(16,2))

#지수가 음수 ?
def my_power(b:float,e:float) -> float:
    """
    A function that takes a base and an exponent as input, calculates the power (exponentiation),
    and returns the result as a floating-point number.
    :param b: base number
    :param e: exponent
    :return: the power result in the form of a real number
    """
    result = 1

    if e < 0:
        b= 1/b
        e = e * -1
        #return 1 / my_power(b, -e)

    i = int(e)
    f = e - i

    for _ in range(i): #for k in range(e)
        result = result * b

    if f > 0:
        result = result * math.exp(f*math.log(b))

    return result


print(my_power(2,9))
print(my_power(16,0.5))
print(my_power(10,3))
print(my_power(25,-2))

#포크 : 다른 사람의 원격 repository 를 내 것으로 떠오는 것. 떠먹는 티라미수 pull request 받으면 코드 리뷰를 하고 거기에 최종 merge
#다른 사람이 내 repository를 떠가서 수정해서 반영해달라고 request 해온 걸 수락하면 원본에 반영됨.
#pull 원격에 있는 걸 내꺼로 다운, push는 원격에 올림.
