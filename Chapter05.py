#리스트 []
a = ['차민철','차승철','차호철']
print(a);

b = [1,2,3,4,5,6]
print(b[2:5])

c = a+b
print(c)

b[2] = 10
print(b)
b.reverse()
print(b)

#튜플 () 패킹, 언패킹 
a = (1,2,3)
print(a)
b = 3,4,5
print(b)
print(a+b)
c = a[:2]
print(c)
one, two, three = a
print(one,two,three)

#딕셔너리 {} key-value
a = {}
a['banana']='yellow'
a['apple']='red'
print(a)
