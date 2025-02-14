y=3
x=y*9
z=list(range(x))
print(z)
print(tuple(map(str,z)))

def my_range(first=0,last=5, step=1): #default 매개변수
    number = first #number라는 지역변수에 시작값을 부여
    while number < last : #number가 last보다 작을 때까지
        yield number #generator(iterable 반복가능 객체)로 함수를 만들어줌. return이면 코드가 끝남. number return후 그 뒤의 함수를 실행
        #number += step #yield여서 이게 실행됨.
        number = number + step
r = my_range()
print(r,type(r)) #r이 my range 함수의 return을 받음 , r type은 generator

for x in r:
    print(x) #yield가 보낸 값이 r에 담겨서 출력됨.
for x in r:
    print(x) # 두 번째는 출력되지 않음. 비워짐.