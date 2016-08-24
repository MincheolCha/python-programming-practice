#출력 해보기
print("hello world")

#수 다루기 // : 나눗셈 몫 구하기
a = 3
b = 3.5
c = -2
print(a)
print(type(b))
d = a+b
print('a+b =' + str(d))

# hex, oct, bin
a = 255
print(hex(a))
print(oct(a))
print(bin(a))

#decimal 라이브러리로 정밀한 계산가능
#복소수
b = 2 + 3j
print(b.real)
print(b.imag)
print(b.conjugate())

#절대값, 반올림, 버림
import math
c = 2.6
print(abs(c))
print(round(c))
print(math.trunc(c))

#제곱 제곱근
d = 4
print(d**d)
print(math.pow(d,d))
print(math.sqrt(d))
