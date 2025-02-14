class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

#class Pikachu:
class Pikachu(Pokemon):  # is-a
    def __init__(self, name, type):
        super().__init__(name)  #부모 클래스 호출
        self.type = type #type 받아서 할당

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")

    def electric_info(self):
        print("전기 계열의 공격을 합니다")


class Squirtle(Pokemon):  # is-a
    pass

class Agumon:
    pass

p1 = Pikachu("피카츄", "전기") #괄호 내 매개변수
p2 = Squirtle("꼬부기") #부모클래스 생성자를 통해 꼬부기라는 이름을 할당.
p3 = Pokemon("아무개")
p1.electric_info()
#p3.electric_info()  # AttributeError: 'Pokemon' object has no attribute 'electric_info' electric 함수는 피카츄에 있음.
p1.attack(p2)
# p2.attack(p1)
# print(p1.name, p1.type)
# print(issubclass(Pikachu, Pokemon))
# print(issubclass(Agumon, Pokemon)) #issubclass 상속관계인지 확인하는 함수
