# Q2. Car 클래스를 이용해서 Bike 클래스를 새로 제작, 
# Car 클래스를 상속 받아 새로운 Bike 클래스를 출력한다. 
# output : gas 2 small

# A. 
#   1. fuel, wheels 값을 가지고 있는 Car 클래스(부모)를 제작
#   2. size 값을 가지고 있는 Bike 클래스(자식)에 상속한 후 출력

class Car(object): # class에 부모가 없으면, object를 기본으로 삼는다. 생략 가능
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels
    
    def car(self): # class Car는 self.fuel과 self.wheels 값을 return 한다. 
        return (self.fuel, self.wheels)

class Bike(Car): # 부모 class 
    def __init__(self,fuel, wheels, size):
        super().__init__(fuel, wheels) 
        # super와 __init__에 대한 호출 확인
        # super().init() : 다른 클래스의 속성, method를 자동으로 호출, 해당 클래스에서 사용이 가능하도록 해준다. 
        # 상속 받은 클래스 내에서 해당 method를 새롭게 다시 구현해주면
        # 부모 클래스와 다른 기능을 수행하도록 만들 수 있다. 
        self.size = size # 변수 size 추가 

    def bike(self):
        return (self.fuel, self.wheels, self.size)

bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)