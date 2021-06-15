#1. how to create class object method in python

class a:
    def hi(self):
        print('welcome')
def main():
    b=a()
    b.hi()
if __name__=='__main__':
    main()

# 2. program to print your name

print('usharani')

#3.program for single line multiline and documentaion strings

# this is a single line comment

# this
# is example
# for multiline comments

''' this is the example for more than one line comment or documentation comments in pytho'''

a=6
print(type(a))
a=True
print(type(a))
print(chr(78))
a=chr(46)
print(type(a))
b=ord(a)
print(type(b))
print(a,b)
print(type(a))
a=0.6
print(type(a))



#4. defining local and global variable with the same name and printing both variables

a=10
b=20
def sum():
    a=10
    b=20
    print(a+b)
sum()
print(a+b)

# wite a function to print your name and calling function fom main method

def name(name):
    print(name)
#name('usha')
if __name__=='__main__':
    name('usha')



        
