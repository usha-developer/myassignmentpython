#1.

class defaultcon:
    # default constructor
	def __init__(self):
		self.geek = "defaultconstructor"

	# a method for printing data members
	def print_defaultcon(self):
		print(self.geek)
obj = defaultcon()

# calling the instance method using the object obj
obj.print_defaultcon()

class Addition:
	first = 0
	second = 0
	answer = 0
	
	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s
	
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()

class sub():
    first=0
    def __init__(self,f):
        self.first=f
    def displayresult(self):
        print('number is',self.first)
obj1=sub(100)
obj1.displayresult()


#2..


class defaultcon:
    def __init__(self):
        print('defaultconstructor')
	#self.geek = "defaultconstructor"

	# a method for printing data members
    def print_defaultcon(self):
	    print('defaultconstructor1')


class sub(defaultcon):
    first=0
    def __init__(self,f):
        self.first=f
    def displayresult(self):
        print('number is',self.first)
class exsub(sub):
    second=0
    def __init__(self,y):
        sub.__init__(self,y)
        self.second=y
    def dis(self):
        print('number2 is',self.second)

obj = exsub(100)

# calling the instance method using the object obj
obj.displayresult()
obj.print_defaultcon()
obj.dis()

#3.. w to create public,private, protected and default modifiers to the constructor

class Geek:
    def __init__(self, name, age):
        self.geekName = name
        self.geekAge = age
    # public memeber function	
    def displayAge(self):
        print("Age: ", self.geekAge)


obj = Geek("usha", 20)
print("Name: ", obj.geekName)
obj.displayAge()


# protected acces modifiers

class Student:
    # protected data members
    _name = None
    _roll = None
    _branch = None
# constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch
	
	# protected member function
    def _displayRollAndBranch(self):
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class Geek(Student):
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)
		
    def displayDetails(self):
        print("Name: ", self._name)
        self._displayRollAndBranch()
	
obj = Geek("usha", 256, "cse")
obj.displayDetails()

# private acces modifliers
class Student:
    # protected data members
    __name = None
    __roll = None
    __branch = None
# constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch
	
	# protected member function
    def __displayRollAndBranch(self):
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)
		
    def displayDetails(self):
        self.__displayRollAndBranch()
	
obj = Student("usharani", 256, "IT")
obj.displayDetails()



#4. write constuctors with return type int and string

class Addition:
    first = 0
    second = 0
    answer = 0
    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s
    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("First number = ",int(self.first))
        print("Second number = ",int(self.second))

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)
obj.display()


#5.try to call the constructor multiple times with the same object
class new:
    def __init__(self):
        print('constructor is created')
a=new()
a=new()
a=new()
a=new()






