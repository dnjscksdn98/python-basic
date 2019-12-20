# 상속, 다중 상속

class Car :
    """Parent Class"""

    def __init__(self, type, color) :
        self.type = type
        self.color = color

    def show(self) :
        return 'Car Class "Show Method!"'

class BmwCar(Car) :
    """Sub Class"""

    def __init__(self, car_name, type, color) :
        super().__init__(type, color)
        self.car_name = car_name

    def show_model(self) :
        return "Your Car Name : %s" %(self.car_name)

class BenzCar(Car) :
    """Sub Class"""

    def __init__(self, car_name, type, color) :
        super().__init__(type, color)
        self.car_name = car_name

    def show_model(self) :
        return "Your Car Name : %s" %(self.car_name) 

    def show(self) :
        print(super().show())
        return "Car Info : %s %s %s" %(self.car_name, self.type, self.color) 


model1 = BmwCar("520d", "sedan", "red")
print(model1.color)
print(model1.type)
print(model1.car_name)
print(model1.show())
print(model1.show_model())

model2 = BenzCar("220d", "suv", "black")
print(model2.show())

# Parent Method Call
model3 = BenzCar("350s", "sedan", "silver")
print(model3.show())

# Inheritance Info
# 상속 정보를 리스트 형태로 반환 - mro()
print(BmwCar.mro())
print(BenzCar.mro())

# 다중 상속
class X :
    pass

class Y :
    pass

class Z :
    pass

class A(X, Y) :
    pass

class B(Y, Z) :
    pass

class M(B, A, Z) :
    pass

# 너무 복잡한 상속 관계는 효율성이 떨어짐
print(M.mro())