#1.write two methods with the same name but different number of parameters of same type and call the methods from main method
#python does not suport method overloading concept
def product(a, b):
	p = a * b
	print(p)
	
def product(a, b,c):
	p = a * b * c
	print(p)
#product(10,5)
product(4, 5,90)

#2. write two methods with the same name but different number of parameters of different data type and call the methods from main method

# Function to take multiple arguments
def add(datatye,a,b):
    print(a+b)
def add(datatype,name,city,hi):
    print(name+city+hi)
#add('int',10,20)
add('str','usha','hyderabad','welcome')


#3. write two methods with the same name and same number parameters  of same  type and call the methods from main method

def add(a,b):
    print(a*b)
def add(a,b):
    print(a*b)
add(50,40)

#4.write two methods with the same name and same number of parameters of different type and call the methods from main method

def add(a,b):
    print(a*b)
def add(a,b):
    print(a*b)
add(50,67)
#add('hi','welcome')

#5. write teo methods with same name,number of parameters and data type but different return type

def add(a,b):
    print(a*b)
def add(a,b):
    print(a+b)
add(50,67)
add('hi','welcome')
