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
         self._displayRollAndBranch(self)
        
        

class Geek(Student):
  
       
       def __init__(self, name, roll, branch): 
                Student.__init__(self, name, roll, branch) 
          
       
       def displayDetails(self):
            print("Name: ", self._name)
            self._displayRollAndBranch()
  

obj = Geek("gg", 1706256, "Information Technology") 
  

obj.displayDetails() 

obj._displayRollAndBranch()

#default feilds and methds

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

#public fields methods
class publicclass:
     def __init__(self, name, age):
            self.publicclassname = name
            self.publicclassage = age    
     def displayAge(self):
           print("Age: ", self.publicclassage)

obj = publicclass("usha", 23)
print("Name: ", obj.publicclassname)
obj.displayAge()
