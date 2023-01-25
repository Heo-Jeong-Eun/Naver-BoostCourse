# Q2. Car 클래스를 이용해서 Bike 클래스를 새로 제작, 
# Car 클래스를 상속 받아 새로운 Bike 클래스를 출력한다. 
# output : gas 2 small

# A. 
#   1. 

class Car():
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels

# class Bike():
    
bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)