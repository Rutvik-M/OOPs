class Animal:
    def __init__(self,name:str,age:int):
        self.name=name 
        self.age=age 
      
    def sleep(self):
        print("I am sleeping")
    
    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self,name:str,age:int,bread:str):
        super().__init__(name,age)
        self.bread=bread 
        print("this is dog init")

    def bark(self):
        print("bhow bhow")

    def display(self):
        print (f"my name is {self.name} and age is {self.age}")

dog = Dog("cherry",4,"atlassin")
dog.display()

