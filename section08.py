# 파이썬 모듈 & 패키지

# 상대 경로
# .. : 부모 디렉터리
# . : 현재 디럭테리



# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)



# 사용2(클래스)
# 한번에 모두 가져오기 - 리소스 낭비(권장x)
from pkg.fibonacci import *



# 사용3(클래스)
# Alias 설정
from pkg.fibonacci import Fibonacci as fb

fb.fib(300)

print("ex3 : ", fb.fib2(400))
print("ex3 : ", fb().title)



# 사용4(함수)
import pkg.calculation as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))



# 사용5(함수)
from pkg.calculation import div as d

print("ex5 : ", int(d(100, 10)))



# 사용6
import pkg.prints as p
import builtins  # 기본 제공 함수들

p.prt1()
p.prt2()
print(dir(builtins))