class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print("공격~")

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스") #객체
c1 = Charizard("리자몽")
print(c1.fly())
print(g1.swim())
# c1.attack() #c1이 객체(self)이므로 동작 가능
#Charizard.attack() #객체없음  #클래스 이름.method <-- static 함수 (ex. math.random)
Charizard.attack(c1)
print(g1.name)
g1.name = "잉어킹"
print(g1.name)
