# class students():
#     name="kasisaritha"
#     age=45
# print(getattr(students,'name'))
# print(getattr(students,'age'))
# print(getattr(students,'gender','no such attribute error'))
# #dotnotation
# print(students.name)
# print(students.age)
# #setattr
# setattr(students,'name','sakthi')
# print(students.name)
# setattr(students,'gender','female')
# print(students.gender)

# students.city='viluppuram'
# print(students.city)

# print(students.__dict__)
# delattr(students,"city")
# print(students.__dict__)

# #inheritance
# class dad():
#     def money():
#         print("dad money")

# class mom(dad):
#     def phone():
#         print("mom phone")

# abi=mom
# abi.phone()
# abi.money()

# class car():
#     pass
# swift=car()
# print(isinstance(swift,car))

#instance attribute
# class user:
#     course = "java"
# o=user()
# print(user.__dict__)
# print(user.course)#print class attribute
# print(o.__dict__)
# print(o.course)
#  o.course="python"
# print(o.__dict__)
# print(o.course)
# o2=user()
# print(o2.course)

# class leader:
#     name='anitha'
# q=leader()
# print(leader.__dict__)
# print(q.__dict__)
# print(q.name)
# print(leader.name)
# q.name='nila'
# print(q.__dict__)
# print(q.name)
# q2=leader()
# print(q2.name)

#class methods
# class student:
#     name="nila"
#     age=21
#     def printall():
#         print("Name:",student.name)
#         print("Age:",student.age)
# student.printall()
# print(student.__dict__)
# print(getattr(student,"printall"))
# getattr(student,"printall")()
# student.__dict__['printall']()

#instance methods
# class student:
#     name='veera'
#     age=19

#     def printall(self,gender):
#         print("Name:",student.name)
#         print("Age:",student.age)
#         print("Gender:",gender)
# o=student()
# o.printall("male")
# student.printall(o,"male")#this line option

#constructor init methods
# class user:
#     def __init__(self,name):
#         print("call when new instance created")
#         self.name=name
#     def printall(self):
#         print("Name:",self.name)
# o=user("kasi")
# o.printall()
# print(o.__dict__)
# o1=user("saritha")
# o1.printall()
# print(o1.__dict__)
# print(user.__dict__)

# class user():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         # self.msg=self.name + "is" + str(self.age) + "years old"
#     def msg (self):
#         return self.name + " is " + str (self.age) + "years old"
# o=user("abii",21)
# print(o.name)
# print(o.age)
# print(o.msg())

# class laptop:
#     price='0'
#     processor=''
#     ram=''
# hp=laptop()
# dell=laptop()

# hp.price=60000
# hp.processor='i5'
# hp.ram='8gb'
# dell.price=70000
# dell.processor='i7'
# dell.ram='16gb'
# print(hp.price)
# print(dell.price)

# class phone:
#     def __init__(self):
#         self.memory=''
#         self.brand=''
#     def color(self):
#         print("memory:",self.memory)
#         print("brand:",self.brand)
# mobile=phone()
# tab=phone()
# mobile.memory='8gb'
# mobile.brand='oppo'
# tab.memory='128gb'
# tab.brand='apple'
# mobile.color()
# tab.color()

# class student:
#     def __init__(self):
#         self.name='Veera'
#         self.register_num='12345'
#     def display(self):
#         print("name:",self.name)
#         print("register_num:",self.register_num)
# o=student()
# o1=student()
# o.name='sneha'
# o.register_num='3'
# o1.name='bicky'
# o1.register_num='4'
# o.display()
# o1.display()

# class fruit:
#     def __init__(self,col):
#         self.color=col
# apple=fruit('red')
# print(apple.color)

# class teacher:
#     def __init__(self,nam,reg):
#         self.name=nam
#         self.regno=reg
#     def display(self):
#         print("name",self.name)
#         print("regno:",self.regno)
# t1=teacher('janis','1')
# t2=teacher('kamalesh','2')
# t1.display()
# t2.display()

# class calculator:
#     # def __init__(self,a,b):
#     #     self.num1=a
#     #     self.num2=b
#     def add(self,a,b):
#         print("add:",a+b)
# obj=calculator()
# obj.add(10,2)

#class kulla variable use panna ella object kum common ah oru irukka podhu na adha class kulla kudukkanum
# class phone:
#     chargetype="c-type"
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def display(self):
#         print("brand:",self.brand)
#         print("price:",self.price)
#         print("chargetype:",self.chargetype)
# # phone.chargetype="b-type"
# samsang=phone("samsang","10000")
# samsang.display()
# redmi=phone("redmi","5000")
# redmi.display()
# google=phone("poco","9000",)
# google.display()

# #different types of method in class
# class laptop():
#     chargetype="c type"
#     def __init__(self):
#         self.brand=''
#         self.price=34
#     def setprice(self,price):
#         self.price=price
#     def getprice(self):
#         print(self.price)
#     def changechargetype(cls):
#         cls.chargetype='b type'
#         print("charge type changed to b")
#     @staticmethod
#     def info():
#         print("this is laptop class")
# hp=laptop()
# hp.setprice(10000)
# hp.getprice()
# laptop.changechargetype(laptop)
# hp.info()

# #class and object la important method in inheritance
# class dad():
#     def phone(self):
#         print("dad's phone")
# class mom(dad):
#     def money(self):
#         print("mom's money")
# class son(mom):
#     def laptop(self):
#         print("son's laptop")
# abi=son()
# abi.laptop()
# abi.money()
# abi.phone()
# nish=mom()
# nish.phone()

# #heirachy
# class dad():
#     def money(self):
#         print("dad money")
# class son1(dad):
#     pass
# class son2(dad):
#     pass
# class son3(dad):
#     pass
# s1=son2()
# s1.money()

# #heirachy
# class dad():
#     def money(self):
#         print("dad money")
# class land():
#     def importand(self):
#         print("imporatant land")
# class son1(dad,land):
#     pass
# class son2(dad):
#     pass
# class son3(dad):
#     pass
# s1=son2()
# s1.money()

# #instance method
# class student:
#     name='sakthi'
#     age=19
#     def printall(self,gender):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("gender:",gender)
        
# o=student()
# o.printall("female")
# #old model option # student.printall(o,"female")

# #constructor
# class user:
#     def __init__(self,name):
#         print("i am going to banglore")
#         self.name=name
#     def printall(self):
#         print("name:",self.name)
# o=user("nisha")
# o.printall()
# o1=user("sakthi")
# o1.printall()

# #property
# class user:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @property
#     def mesg(self):
#         return self.name + "is" + str(self.age) + "years old"        
# o=user("nisha",15)
# print(o.name)
# print(o.age)
# print(o.mesg)
# o.age=20
# print(o.mesg)

# #encaptulation
# class company:
#     def __init__(self):
#         self.__companyname="google"
#     def companyname(self):
#         print(self.__companyname)
# o=company()
# o.companyname()

# #polymorphism
# def add(a,b,c=0):
#     print(a+b+c)
# add(1,2)
# add(4,3,5)

# class animal():
#     def sound(self):
#         print("animal makes sound")
# class dog(animal):
#     def sound(self):
#         print("dog barks")
# class bird(animal):
#     def sound(self):
#         print("bird sing")
# b=bird()
# b.sound()
# o=dog()
# o.sound()


# class shape():
#     def area(self):
#         return 0
# class rectangle(shape):
#     def area(self):
#         a=10
#         b=20
#         print(a*b)
# r=rectangle()
# r.area()

# class nokia:
#     company="nokia india"
#     website="www.nokia-india"
#     def contact_details(self):
#         print("south street,kolapparai,thirukkovilur talk")
# class nokia1(nokia):
#     def __init__(self):
#         self.name="nokia100"
#         self.year=1998
#     def product_details(self):
#         print("name:",self.name)
#         print("year:",self.year)
#         print("company:",self.company)
#         print("websiite:",self.website)
# o=nokia1()
# o.contact_details()
# o.product_details()

#diamond program
# class a:
#     def display(self):
#         print("i am the display a")
# class b(a):
#     def display(self):
#         print("i am the display of b")
# class c(a):
#     pass
# class d(b,c):
#     pass
# o=d()
# o.display()

# #operator overloading
# class Addition:
#         def __init__(self,a):
#             self.a=a
#         def __add__(o1,o2):
#             return o1.a + o2.a
#         def __sub__(o1,o2):
#              return o1.a-o2.a
# o1=Addition(8)
# o2=Addition(10)
# print("total:",(o1+o2))
# print("total:",(o1-o2))

# #abstract method
# from abc import ABC,abstractmethod
# class bank(ABC):
#     @abstractmethod
#     def loan(self):pass
#     @abstractmethod
#     def credit(self):pass
#     @abstractmethod
#     def debit(self):pass
# class SBI(bank):
#     def loan(self):
#         print("we can provide 75% intrest loan")
#     def credit(self):
#         print("sbi provide credit")
#     def debit(self):
#         print("sbi provide debit")
# o=SBI()
# o.credit()
# o.loan()
# o.debit()

# class per():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# o=per("abi",21)
# print(o.name)
# print(o.age)

class laptop():
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("Display")
hp=laptop()
hp.ram="8gb"
hp.processor="i5"
print(hp.price)
print(hp.processor)
print(hp.ram)
