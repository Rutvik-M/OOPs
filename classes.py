class Student:
    name=""
    age=0
    gender=""

    def get_info(self):
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")
    
    def display(self):
        print(f"My name is {self.name} , Age is {self.age} , and Gender is {self.gender}")


s1=Student()
s1.get_info()
s1.display()

s2=Student()
s2.get_info()
s2.display()