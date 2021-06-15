#1. create abstract class with abstract and non abstract nethod
from abc import abstractmethod, ABC
class Person(ABC):#abstactclass
    #this abstract method
    @abstractmethod
    def fly(self):
        pass
class Person1(Person):
    #non abstract method
    def fly(self):
        print('a person can fly')
class Bird(Person1):
    def fly(self):
        print('a bird can fly')
a=Person1()
b=Bird()
a.fly()
b.fly()

#2.creating a subclass for an abstract class. create an object in the child class for the abstact class and access non abstract methods
import abc
 
class parent(ABC):      
    def move(self):
        pass
        #print('abstact class')
 
class child(parent):
    def move(self):
        print("child class")
aa=child()
aa.move()
print( issubclass(child, parent))
print( isinstance(child(), parent)) 

#3. create an instance for the child class in childclass and call abstactmethods
import abc
 
class parent(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def move1(self):
        print('anstact method')
class child(parent):
    def move(self):
        print("child class")
    def move1(self):
        print('abstract method')
aa=child()
aa.move()
aa.move1()

#4.create an instance for the child class in childclass and call non abstactmethods
class Parentclass(ABC):
    def sing(self):#non abstract method
        print('singing')
    def dance(self):#non abstract method
        print('dancing')
class Childclass(Parentclass):
    def fly(self):
        print('flying')
    def sleep(self):
        print('sleeping')
aa1=Childclass()
aa1.sing()
aa1.dance()
aa1.fly()
aa1.sleep()




 


