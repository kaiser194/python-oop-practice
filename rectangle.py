class Rectangle:
    
    def __init__(self,l,w):
        self.length = l
        self.width = w 
        
        
    def perimeter(self):
        return 2*(self.length+self.width)
        
    def area(self):
        return self.length*self.width
        
    def display(self):
      print('The length of rectangle is: ',self.length)
      print('The width of rectangle is: ',self.width)
      print('The perimeter of rectangle is: ',self.perimeter())
      print('The area of rectangle is: ',self.area())
        
obj = Rectangle(3,4)
obj.display()
