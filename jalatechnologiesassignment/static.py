#1. write a class with static variables 2.instance variables 3. static methods 4. instance methods and main method
class person:
    name='usha'
    age=23
obj=person()
print(person.name)
print(person.age)

#static methods
class result:
    @staticmethod
    def add():
        print('hi')
obj1=result()
obj1.add()
result.add()


class CSStudent:
	stream = 'cse' # Class Variable
	def __init__(self,name,roll):
		self.name = name # Instance Variable
		self.roll = roll# Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) 
print(b.stream) 
print(a.name) 
print(b.name) 
print(a.roll) 
print(b.roll)
print(CSStudent.stream) 


# instance methods
class shape:
    def __init__(self, edge, color):
        self.edge = edge
        self.color = color
		
    # Instance Method
    def finEdges(self):
        return self.edge
		
    # Instance Method
    def modifyEdges(self, newedge):
        self.edge = newedge
		
circle = shape(0, 'red')
square = shape(4, 'blue')

# Calling Instance Method
print("No. of edges for circle: "+ str(circle.finEdges()))

# Calling Instance Method
square.modifyEdges(6)

print("No. of edges for square: "+ str(square.finEdges()))


#2. 

import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
a=Pizza(20,33)
a.area()
a.circle_area(30)
a.__repr__()



class Marks:  
    def Math_num(a, b): # define the static Math_num() function  
        return a + b  
  
    def Sci_num(a, b): # define the static Sci_num() function  
        return a +b  
  
    def Eng_num(a, b):  # define the static Eng_num() function  
        return a +b  
# create Math_num as static method  
Marks.Math_num = staticmethod(Marks.Math_num)  
  
# print the total marks in Maths  
print (" Total Marks in Maths" , Marks.Math_num(64, 28))   
  
# create Sci_num as static method  
Marks.Sci_num = staticmethod(Marks.Sci_num)  
  
# print the total marks in Science  
print (" Total Marks in Science" , Marks.Sci_num(70, 25))   
  
# create Eng_num as static method  
Marks.Eng_num = staticmethod(Marks.Eng_num)  
  
# print the total marks in English  
print (" Total Marks in English" , Marks.Eng_num(65, 30))



        
# static variables and instance variables

class CSStudent:
	stream = 'cse' # Class Variable
	def __init__(self,name,roll):
		self.name = name # Instance Variable
		self.roll = roll# Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) 
print(b.stream) 
print(a.name) 
print(b.name) 
print(a.roll) 
print(b.roll)
print(CSStudent.stream) 


# static methods and instance methods

class shape:
    def __init__(self, edge, color):
        self.edge = edge
        self.color = color
    def shapes(self):
        a=10
        print('number is:',a)
		
    # Instance Method
    def finEdges(self):
        return self.edge
		
    # Instance Method
    def modifyEdges(self, newedge):
        self.edge = newedge
		
circle = shape(0, 'red')
square = shape(4, 'blue')

# Calling Instance Method
print("No. of edges for circle: "+ str(circle.finEdges()))

# Calling Instance Method
square.modifyEdges(6)

print("No. of edges for square: "+ str(square.finEdges()))
a=shape(0,'greeen')
a.shapes()
