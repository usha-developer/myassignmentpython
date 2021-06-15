#1. write a program to generate arthematic excepction with out using exception handling
try:
    1/0
except ArithmeticError as e:
    print(f"{e}, {e.__class__}")

#2. HANDLE ARTHEMATIC EXCPTION USING TRY EXCEPT BLOCK
try:  
    a = 13
    b = 0   
    c = a/b  
except:  
    print("Can't divide with zero")  

#3. write a method which throws exception,call that method in main class without try block

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

#4. write a program with multiple except blocks
try:
    arr = [1,2,3,4]
    print('value = ',arr[5])
		
except ArithmeticError as e:    
    print('ArithmeticError exception caught - ',e)

except IndexError as e:   	
    print('IndexError exception caught -',e)
	
except Exception as e:	
    print('Exception exception caught - ',e)

#5. write a program to throws exception with your own message
try:  
    a = 13
    b = 0   
    c = a/b  
except:  
    print("Can't divide with zero")

#6. write a program to create own exception

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value))
  
try:
    raise(MyError('there is no repr function'))
except MyError as error:
    print('A New Exception occured: ',error.value)

#7. program with finally block
try:
   f = open("test.txt","w")
finally:
    f.close()
    print('file closed')

#8. write a program to generate arthematic exception
try:  
    a = 13
    b = 0   
    c = a/b  
except:  
    print("Can't divide with zero is arthematic exception")

#9.write a program to generate array indexoutofboundexception
import numpy as np
arr=np.array([1,2,3,4,5,6])
try:
    #here i am accesing 8th index position but in arr contains 5 indexes only
    val=arr[8]
    print(val)
except:
    print('this is a arrayindexoutofboundexception')

#10.write a program to generate class not found exception

class new:
    def print(self):
        print('hi')
try:
    b=new1()
    b.print()
except:
    print('this is class not found exception')

#11.write a program to generate file not found exception
try:
    f=open('txt1.txt','r')
except:
    print('this is a filenotfoundexception')

#12. program to generate IOE exception

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

#13.program to generate nosuchfieldexception
#python does not have no such field exception

#14. program to generate nosuchmethodexception
def printpro():
        print('welcome')
try:
    print1()
except:
    print('this is a nosuchmethodexception')

#15. program to generate nullpointer exception
#16. program to generate numberpointer exception
#17. program to generate stringindexoutofboundexception
string='welcome'
try:
    s1=string[7]
    print(s1)
except:
    print('stringindexoutofboundexception')

#18.program to generate SQLE exception


