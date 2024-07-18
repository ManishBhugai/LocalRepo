#class Student:
 #   name="karan"

#s1=Student()
#print(s1.name)

#class car:
  #  color="blue"

#car1=car()
#print(car.color)

#class student:
 #   collage_name="Manish institue" #this is class atrribute
  #  def __init__(self , fullname, marks): #this is constructor, self is the parameter used to do call the value from the oobject
   #     self.name=fullname #.name is used to  make a variable used by object
    #    self.marks=ma rks
    #def hello(self):# it is the methods 
     #   print("hello my friend i am manish bhugai")



##s1 = student("karan", 97)
#s1.hello()

#print(s1.name)

##   name="manish bhugai"
#
#s1=student() #instances of class
#print(s1.name)

class student:
    def __init__(self, name , marks):
        self.name= name
        self.marks=marks
    def get_avg(self):
        sum =0
        for i in self.marks:
            sum+=i
        print("your average marks is", sum/3)     

s1=student("manish bhugai",[99,100,98])
s1.get_avg()

#static methods
class student:
    @staticmethod #decorator
    def hello():
        print("hhello my name is manish bhugai")


#abstraction
class car:
    def __init__(self):
        self.aceelerator= False
        self.brk=False
        self.clutch=False
    def start(self):
        self.aceelerator=True
        self.clutch=True
        print("start")


car1=car()
car1.start()

class account:
    def __init__(self, balance,accn):
        self.balance=balance
        self.accn=accn

    def debit(self,amount):
        self.balance-=amount
        print("rs",amount,"is debited")
        print("your total amount is", self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("rs",amount,"is credited")
        print("your total amount is",self.get_balance())

    def get_balance(self):
        return self.balance    
            
s1= account(1000,10)
s1.debit(4000)
s1.credit(5000)            