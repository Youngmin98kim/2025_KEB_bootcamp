y=3
x=y*9
z=list(range(x)) #
print(z)
print(tuple(map(str,z)))

def my_range(first=0,last=5, step=1): #default 매개변수
    number = first
    while number < last :
        yield number #generator(iterable 반복가능 객체)로 함수를 만들어줌 
        number += step 

r = my_range()
print(r,type(r))

for x in r:
    print(x)
for x in r:
    print(x)