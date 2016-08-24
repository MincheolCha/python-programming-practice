#텍스트 String 한줄 '',"" 여러줄 '''''',""""""
a = 'hello world'
b = '''hello
world'''
print(a)
print(b)

#Slicing, Access, in연산자
print(a[1])
print(a[:5])
print('Hello' in  a)
print('hello' in  a)
print('length = ' + str(len(a)))

#Format
c = 'My name is {0}. I\'m {1} years old.'
print(c.format('Mincheol',27))
d = "My name is {name}. I'm {age} years old."
print(d.format(name='Mincheol',age=27))
print(name)
print(age)

#int(), float(), complex(), str()
#논리 연산자, <<. >>, &, |, ^, ~
