#1. write a funtion to add integer values of an array

import array
def sumofarray(a1):
    sum=0
    for i in a1:
        sum=sum+i
    return(sum)
a1=array.array('i',[10,20,30,40,50])
result=sumofarray(a1)
print('sum of arraay:',result)

#2.function to caluclate the average values of an array
import numpy as np

def avgarray(a2):
    return np.average(a2)
a2=np.array([1,2,3,4,5,66,88,66])
res=avgarray(a2)
print('average values of an array is:',res)

#3. program to find index of an array element

print(a2[6])

#4. write a function to test if array contains specific value

def specific(a2):
    #for i in a2:
    if a2[5] in a2:
        print(a2[6],'is presented in a2')
    else:
        print(a2[6],'is not in array')
specific(a2)

#5. function to remove specific element from an array
def removespecificvalue(a2):
    a3=np.delete(a2,4)
    return a3
removespecificvalue(a2)
print('array is',a2)
print('array after removing element at 4th index is',removespecificvalue(a2))

#6.write a function to copy an array to another array
def copyarray(a2):
    a3=a2.copy()
    return a3
print('copied array is',copyarray(a2))

#7. function to insert specific element to an array

def insertelement(a2):
    a3=np.insert(a2,6,44)
    return a3
print('array is:',a2)
print('array after adding element at 6th index position is',insertelement(a2))

#8. function to find minimum amd maximum value of an array
def minmax(a2):
    minval=min(a2)
    maxval=max(a2)
    return minval,maxval
print('min and max values are',minmax(a2))

#9. function to reverse an array of integer values
def reversearray(a2):
    return a2[::-1]
print('original array',a2)
print('reverse array',reversearray(a2))

#10. program  to find duplicate values of an array

a2=[1,1,3,4,5,6,6,4,5]
print('duplicate values are')
for i in range(0,len(a2)):
    for j in range(i+1,len(a2)):
        if a2[i]==a2[j]:
            print(a2[j])

#11. program to find common values between two arrays

a1=np.array([10,20,30,40,50,60])
a2=[50,30,20]
print('common values are:',np.intersect1d(a1,a2))

# 12. program to remove duplicate elememts from an array
a2=[1,1,3,4,5,6,6,4,5]
a3=[]
print('array elements',a2)
for i in a2:
    if i not in a3:
        a3.append(i)
print('removing duplicate elements:',a3)

# 13,14.  program to find second largest element from an array
a2=[1,90,50,67,78]
a2.sort()
n=len(a2)
print(a2)
print(a2[n-2])

#15. program to find even and odd numbers in an array
a3=[]
a4=[]
for i in a2:
    if i%2==0:
        a3.append(i)
    else:
        a4.append(i)
print('even numbers are:',a3)
print('odd numbers are:',a4)

#16. program to get difference of largest and smallest number
print(max(a2))
print(min(a2))
print('difference between max and min values are:',max(a2)-min(a2))

#17. program to verify if array contains two specified elements(12,23)
a=[12,34,6,23]
if 12 and 23 in a:
    print('True')
else:
    print('false')

#18. program to find duplicate elememts and written new array
a2=[1,1,3,4,5,6,6,4,5,88]
a3=[]
print('array elements',a2)
for i in a2:
    if i not in a3:
        a3.append(i)
print('array after removing duplicate elements:',a3)

#19. program to find missing array of sorted array of 1 to 100
def find_missing(a1):
    return [x for x in range(a1[0], a1[-1]+1) 
                               if x not in a1]
a1 = [1, 2, 4, 6, 7, 9, 10,12]
print(find_missing(a1))

