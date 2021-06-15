#1. different ways creating a string
string='hi'
string1="hello"
string2='''welcome'''
string3="""python"""
print(string)
print(string1)
print(string2)
print(string3)

#2. concatinating two strings using + operator

print(string+string1)

#3. finding the length of the string

string="jala technologies programming questions"
print(len(string))

#4. extract substring using string

print(string[5:9])

#5.searching in strings using index()

x='programming'
x1=string.index(x)
print(x1)

#6. matchin a string against regular expression with matches()
#python does not have matches() function

import re
list1=["usha11 get","usha give"]
for element in list1:
    z= re.match("(u\w+)",element)

if z:
    print((z.groups()))


#7. comparing the strings using the methods equals()
  # python does not have equals() methods

s1='hi welcome to python'
s2='hi welcome to python'
if s1==s2:
    print('both strings are equal')
if s1.__eq__(s2):
    print('both strings are equal')

s1='HI'
s2='Hi'
if s1==s2:
    print('both same')
else:
    print('not same')


#8.# equalsIgnorecase(),startswith(), endswith(),compareTo()

#python does not have equalsIgnorecase() and compareTo() instead of these we use == operators in python
if s1.lower()==s2.lower():
    print('both are same')
s1='hi welcome to python'
re=s1.startswith('hi')
print(re)
re1=s1.startswith('welcome')
print(re1)

re=s1.endswith('to')
print(re)
re1=s1.endswith('python')
print(re1)

print(s1==s2)
print(s1!=s2)

#9. trimming strings with trim()
# pytho does not have trim() instead of these we use strip(), lstrip(),rstrip()

s1='@@hi welcome to python @easy programming language@@@@'
print('old string ',s1)
re=s1.strip('@')
print('string after spliting :::',re)

print('splitting using rstrip()',s1.rstrip('language@@@@'))

print('splitting using lstrip()',s1.lstrip('@@hi'))

#10. replacing characters in strigs with replace

print('replaching python with easy python ',s1.replace('python','easy python'))

#11. splitting strings with split()

print('splitting string using space:',s1.split())
print('splitting string using at position e:',s1.split('e'))

#12. converting numbers to strings with valueof()

#python does not have valueof() method insted of this we use str() method in pyhton
str1=int(90)
print(type(str1))
str2=str(str)
print(type(str2))

#13.converting integer objects to strings

s1=568
print(type(str(s1)))

#14. converting to uppercase and lowercase

s1='WELcome'
print('original string',s1)
print(s1.upper())
print(s1.lower())









