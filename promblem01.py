#Problem 1
import random
import numpy

dataSize = 1000000
sortArraySize = 100000


#Create random number and save as hexDec.bin
randomNumber=[]
for i in range(dataSize):
    randomNumber.append(random.randint(0,65535))

hexDec = numpy.array(randomNumber,dtype=numpy.uint16)

with open("hexDec.bin",'wb') as file:
    hexDec.tofile(file)


#Sort by ascending order
tempSortArray = numpy.zeros((1,sortArraySize),dtype=numpy.uint16)
trackArray = numpy.zeros((1,65536),dtype=numpy.uint16)
hexDecSortTemp = []

for j in range(10):
    for i in range(sortArraySize):
        trackArray[0][hexDec[i+j*sortArraySize]] = trackArray[0][hexDec[i+j*sortArraySize]] + 1


#Save as hexDecSort.bin
count = 0
for i in range(65536):
    for j in range(trackArray[0][i]):
        count = count + 1
        hexDecSortTemp.append(i)

hexDecSort = numpy.array(hexDecSortTemp,dtype=numpy.uint16)

with open("hexDecSort.bin",'wb') as file:
    hexDecSort.tofile(file)


#Sort by size order
sizeSortDic = {}

for i in range(65536):
    sizeSortDic[i] = trackArray[0][i]

sortValue = sizeSortDic.values()
sortValue.sort(reverse=True)



