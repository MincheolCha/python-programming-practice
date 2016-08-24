class InstanceVar:
    count = 0
    def __init__(self, name='차민철', age=27):
        self.text_list=[]
        self.name = name
        self.age = age
        InstanceVar.count += 1

    def print_info(self):
        print("name is {0} and he is {1} years old".format(self.name, self.age))

    def add(self,text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

    @classmethod
    def print_instance_count(cls):
        print(cls.count)

    
