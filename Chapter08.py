#from 모듈명 import 클래스/함수

from instanceVar import InstanceVar

if __name__ == '__main__':
    a = InstanceVar('차승철',26)
    b = InstanceVar('차호철',19)
    c = InstanceVar()
    
    a.add('a')
    a.add('b')
    b.add('c')
    b.add('a')
    a.print_list()
    b.print_list()

    c.print_info()
    a.print_info()
    b.print_info()

    InstanceVar.print_instance_count()
    

#Inheritance

class Derived(InstanceVar):
    pass

d = Derived();
d.add('a')
d.print_list()
d.print_info()
InstanceVar.print_instance_count()
