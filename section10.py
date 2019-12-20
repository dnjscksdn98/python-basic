# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법
# print('Test)
# if True

# NameError : 참조 변수 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
# x = [10, 20, 30]
# print(x[3])

# KeyError
# dic = {"name" : "kim", "age" : 33, "city" : "seoul"}
# print(dic["hobby"])
# print(dic.get("hobby")) # get() : 키값이 없으면 None 반환, 사용할것을 권장

# AttributeError : 모듈, 클래스에 있는 잘못됫 속성 사용시에 에러
# import time
# print(time.month())

# ValueError : 참조 값이 없을때
# x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError
# f = open("test.txt", "r")

# TypeError
# x = [1, 2]
# y = (1, 2)
# z = "test"
# print(x + y)
# print(x + z)



# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩을 권장(EAFP 코딩 스타일)



# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행


# 예제 1
name = ["Kim", "Lee", "Park"]

try :
    z = "Kim"  # Cho - 예외 발생
    x = name.index(z)
    print("{} Found it! in name".format(z))

except ValueError :
    print("Not Found! - Occurred ValueError")

else :
    print("Ok! else!")




# 예제 2
name = ["Kim", "Lee", "Park"]

try :
    z = "Jin"
    x = name.index(z)
    print("{} Found it! in name".format(z))

# 모든 예외를 잡는다
except :
    print("Not Found! - Occurred Error")

else :
    print("Ok! else!")



# 예제 3
name = ["Kim", "Lee", "Park"]

try :
    z = "Jin"
    x = name.index(z)
    print("{} Found it! in name".format(z))

# except Exception :
except :
    print("Not Found! - Occurred Error")

else :
    print("Ok! else!")

# 반드시 실행
finally :
    print("finally ok!")


# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try :
    print("try")

finally :
    print("finally ok!")



    
# 예제 5
name = ["Kim", "Lee", "Park"]

try :
    z = "Jin"
    x = name.index(z)
    print("{} Found it! in name".format(z))

# 계층 예외 처리
# 작은 범위의 예외부터 작성
# Alias로 설정 가능
except ValueError as v:
    # 에러 내용 출력
    print(v)

except IndexError :
    print("Not Found! - Occurred IndexError")

except Exception :
    print("Not Found! - Occurred Error")

else :
    print("Ok! else!")

finally :
    print("finally ok!")




# 예제 6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try :
    a = "Kim"

    if a == "Kim" :
        print("Ok 허가")
    
    else :
        raise ValueError

except ValueError :
    print("문제 발생!")

except Exception as e :
    print(e)

else :
    print("Ok!")