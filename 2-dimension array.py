#2차원 배열 생성하기
rowNumber = 2
colNumber = 2
table = [[0 for col in range(rowNumber)] for row in range(colNumber)]

table[0][0] = 1
table[0][1] = 2
table[1][0] = 2
table[1][1] = 4

print(table)


#numpy를 사용하여 1,2차 배열 생성
import numpy

oneDim = numpy.array([1,2,3,4])
print(oneDim)

twoDim = numpy.array([[1,2,3],[4,5,7]])
print(twoDim)
print(twoDim.shape)
