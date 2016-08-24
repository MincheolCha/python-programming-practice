#함수를 변수에 담아 사용하기
def hello_world():
    print('hello_world')

a = hello_world
a()
b = 5

def hello_greet(arg):
    arg()

hello_greet(a)

#중첩함수
import math

def stddev(*args):
    def mean():
        return sum(args)/len(args)

    def variance(m):
        total = 0
        for arg in args:
            total += (arg-m)**2
        return total/(len(args)-1)

    v = variance(mean())
    return math.sqrt(v)

print(stddev(2.3, 1.7, 1.4, 0.7, 1.9))
