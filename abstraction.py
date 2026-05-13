from abc import abstractmethod,ABC

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,len:int,breadth:int):
        self.len=len
        self.breadth=breadth
    
    def area(self):
        print (self.len * self.breadth)
    
    def perimeter(self):
        print (2*(self.len * self.breadth))
    

rectangle=Rectangle(2,4)
rectangle.area()
rectangle.perimeter()




