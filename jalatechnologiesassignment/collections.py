
arrlist=['java','python','.net','bigdata','hadoop','php','appian','hyperloop','sql','laravel']

#add element to array list
arrlist.append('collections')
print(arrlist)

#add element at specific position
arrlist.insert(6,'hi')
print(arrlist)

#remove element from an array list
arrlist.remove('.net')
arrlist.pop(6)
print(arrlist)

#update element at specified index
arrlist.insert(2,'java10')

print(arrlist)

# check the element is presented in particular index or not

if(arrlist.index('bigdata')==5):
    print('yes')
else:
    print('no')
a=arrlist.index('bigdata')
if a:
    print('Presented')
else:
    print('Not presented')
#get element from particular index

a1=arrlist[5]
print(a1)

#find the size of arraylist
a2=len(arrlist)
print(a2)

#remove all elements from array list
a=arrlist.clear()
print(a)

#3..

class Bucket:
   def __init__(self):
      self.bucket=[]
   def update(self, key):
      found=False
      for i,k in enumerate(self.bucket):
         if key==k:
            self.bucket[i]=key
            found=True
            break
      if not found:
         self.bucket.append(key)
   def get(self, key):
      for k in self.bucket:
         if k==key:
            return True
      return False
   def remove(self, key):
      for i,k in enumerate(self.bucket):
         if key==k:
            del self.bucket[i]
class MyHashSet:
   def __init__(self):
      self.key_space = 2096
      self.hash_table=[Bucket() for i in range(self.key_space)]
   def add(self, key):
      hash_key=key%self.key_space
      self.hash_table[hash_key].update(key)
   def remove(self, key):
      hash_key=key%self.key_space
      self.hash_table[hash_key].remove(key)
   def contains(self, key):
      hash_key=key%self.key_space
      return self.hash_table[hash_key].get(key)
ob = MyHashSet()
ob.add(1)
ob.add(3)
print(ob.contains(1))
print(ob.contains(2))
ob.add(2)
print(ob.contains(2))
ob.remove(2)
print(ob.contains(2))

#2.. python dictionaries

student={11:'s1',22:'s2',33:'s3',44:'s4',55:'s5',66:'s6',77:'s7',88:'s8',99:'s9',10:'s10'}
print(student)

print(student[66])

std1=student.copy()
print(std1)

a=std1[77]
if a:
    print('True')
else:
    print('Flase')
print(std1.get(33))

std1[12]='s12'
print(std1)

std1[22]='hi'
print(std1)

a=std1.pop(77)
print(a)


a1=std1.popitem()
print(a1)

print(len(std1))

for x in std1:
    print(x)

for x in std1:
    print(std1[x])
for x in std1.values():
    print(x)

print(std1.items())

std2=('hi','hello','welcome')

std3=0

print(dict.fromkeys(std2,std3))








