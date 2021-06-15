#1.create a class with Private files private methods and main method print the fileds in main method call the private method in main method

class Student:
    _schoolName = 'XYZ School'
    def __func(self):
        print('my school name is:',a._schoolName)
    def final(self):
        self.__func()
class A: 
   
    # Declaring public method
    def fun(self):
        print("Public method")
   
    # Declaring private method
    def __fun(self):
        print("Private method")
      
    # Calling private method via
    # another method
    def Help(self):
        self.fun()
        self.__fun()
a=Student()
a.final()
obj = A()
obj.Help()

#2. create a class with default fields and methods acess these fields and methods from any ther class in the same package


class A:
    def student(self,name, age =23, city ='Nellore'):
        print(name, age, 'lives in', city)
class B(A):
    pass

obj=B()
obj.student('jamesbong')                      
obj.student('billgates',23,'ilaty')    
obj.student('smith',23,'france')                 
obj.student('tannera', 45)
# accesing default variables from different package
import pack
class cc(A):
    pass
ob=cc()
ob.student('usa',22,'tpt')

class MyClass:
    def __getattr__(self, item):
        def default():
            print(item)
            print(self)
        return default
obj1=MyClass()
obj1.myMethod()

#3. create a class with protected fields and methods acess these fields and methods from any ther class in the same package
# also access protected fields and methods from child class located in different package
# access the protected fields and methods from any class in different package


class Student:
     _name = None
     _roll = None
     _branch = None
     def __init__(self, name, roll, branch):  
          self._name = name
          self._roll = roll
          self._branch = branch
     def _displayRollAndBranch(self):
          print("Roll: ", self._roll)
          print("Branch: ", self._branch)
     def home(self):
         self.___displayRollAndBranch(self)
        
        

class Geek(Student):
       def __init__(self, name, roll, branch): 
                Student.__init__(self, name, roll, branch) 
       def displayDetails(self):
                print("Name: ", self._name) 
                self._displayRollAndBranch()
  
obj = Geek("R2J", 1706256, "Information Technology") 
obj.displayDetails() 
obj._displayRollAndBranch()


# accesing protected fields and methods from child class from different package

import pack
class protectedclass(Geek):
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)
        Geek.__init__(self, name, roll, branch)
    def accessing(self):
        self._displayRollAndBranch()
        
aa=protectedclass('john',56,'cse')
aa.accessing()
aa.displayDetails()
# accesing protected fields and methods from parent class from different package

import pack
class protectedclass(Student):
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)
        Geek.__init__(self, name, roll, branch)
    def accessing(self):
        self._displayRollAndBranch()
        
aa=protectedclass('john',56,'cse')
aa.accessing()


#4. create a class with public fields and methods.
# access the public methods and fields from any class in the same package or different package

class publicclass:
     def __init__(self, name, age):
            self.publicclassname = name
            self.publicclassage = age    
     def displayAge(self):
           print("Age: ", self.publicclassage)

obj = publicclass("usha", 23)
print("Name: ", obj.publicclassname)
obj.displayAge()

# accesing public fields and methods from different package
import pack
class newpublicclass(publicclass):
    pass
newpc=newpublicclass('usharani',23)
print('name is:',newpc.publicclassname)
newpc.displayAge()




