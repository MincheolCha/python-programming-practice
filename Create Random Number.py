#난수 생성기
import random

randomNumber = []

print("난수 개수 입력하시오")
count = int(input())
print("최대 범위를 입력하시오")
maxNumber = int(input())

for i in range(count):
    randomNumber.append(random.randint(0,maxNumber))

print(randomNumber)
