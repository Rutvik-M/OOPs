class Animal:
    def __init__(self,name:str,age:int):
        self.name=name 
        self.age=age 
      
    def sleep(self):
        print("I am sleeping")
    
    def eat(self):
        print("I am eating")
    
    def move(self):
        print ("i am walking")

class Dog(Animal):
    def __init__(self,name:str,age:int,bread:str):
        super().__init__(name,age)
        self.bread=bread 
        print("this is dog init")

    def bark(self):
        print("bhow bhow")

    def display(self):
        print (f"my name is {self.name} and age is {self.age}")
    
    def move(self):
        print ("I will run faster I have 4 legs")

dog = Dog("cheery",2,"indie")
dog.move()
dog.display()

