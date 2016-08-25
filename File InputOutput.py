#File I/O
studentName = ['차민철','차승철','차호철']
listSize = len(studentName)

print(listSize)

with open("test.txt",'w') as file:
    i = 0;
    while i < listSize:
        file.write(studentName[i])
        file.write('\n')
        i = i+1

with open("test2.txt","w") as file:
    file.writelines(studentName)







