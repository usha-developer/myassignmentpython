#1. program to print bright i carees 10 times

for i in range(1,11):
        print('Bright it carees')

#2.program to print 1 to 20 numbers using while loop

n=1
while(n<=20):
    print(n)
    n=n+1

#3. progam to find two numbers equal or not

a=20
b=20
if(a==b):
    print('true')
elif(a!=b):
    print('false')

#4. program to print odd and even numbers
a=[]
b=[]
for i in range(1,20):
    if(i%2==0):
        a.append(i)
        #print('even numbers',i)
    else:
        #print('odd numbes',i)
        b.append(i)
print('even numbers:',a)
print('ood numbers:',b)

#5. program to print largest number among 3 numbers
a=10
b=30
c=40
if(a>b and a>c):
    print('a is large',a)
elif(b>c and b>a):
    print('b is large',b)
else:
    print('c is large',c)

#6. program to print even numbers from 10 to 100 using while loop
n=10
while(n<=100):
    if(n%2==0):
        print(n)
    n=n+1

#7. program to print 1 to 10 using do-whileloop

'''python does not have do-while loop'''

#8. program to find amstrong number or not
num=407
#num=int(input('enter number'))
s=0
t=num
while(t>0):
    digit=t%10
    s+=digit**3
    t//=10
if(num==s):
    print(num,'is amstrong')
else:
    print(num,'is not amstrong')

#9. program to find prime or not

n=17
if(n%2==0):
    print(n,'is even number')
else:
    print(n,'is odd number')

#10.program for checking polindrome or not

num='989'
num1=num[::-1]
if(num==num1):
    print(num,'is polindrome')
else:
    print(num,'is not polindrome')

