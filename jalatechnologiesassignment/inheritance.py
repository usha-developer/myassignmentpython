class parentA:
    def wake(self):
        print('i woked up')
    def eat(self):
        print('i have taken breafast')
    def sleep(self):
        print('i am sleeping')
class childB(parentA):
    def run(self):
        print('i am running')
    def walk(self):
        print('i am walking')
    def sleep(self):
        print('i am sleeping')
class childC(childB):
    def jump(self):
        print('i am jupping')
    def drive(self):
        print('i am drivig')
    def sleep(self):
        print('i am sleeping')
a=parentA()
b=childB()
c=childC()
a.wake()
a.eat()
b.run()
b.walk()
c.jump()
c.drive()
a.sleep()
b.sleep()
c.sleep()


