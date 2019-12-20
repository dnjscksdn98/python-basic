# 파이썬 클래스

class UserInfo :
    def __init__(self, name) :
        self.name = name

    def user_info_p(self) :
        print("Name : ", self.name)

user1 = UserInfo("won")
user1.user_info_p()
print(user1.__dict__)


# self의 이해
class SelfTest :
    
    @staticmethod
    def function1() :
        print("function1 called")
    
    def function2(self) :
        print("function2 called")

self_test = SelfTest()
SelfTest.function1()
self_test.function2()


# 클래스 변수, 인스턴스 변수
class WareHouse :
    stock_num = 0

    def __init__(self, name) :
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self) :
        WareHouse.stock_num -= 1

user1 = WareHouse("won")
user2 = WareHouse("kim")
user3 = WareHouse("park")

print(WareHouse.stock_num)
print(user1.stock_num)

del user1