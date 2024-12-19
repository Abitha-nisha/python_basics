# user = {
#     "name":"Abi",
#     "age":21,
#     "girl":True
# }
# print(user)
# print(type(user))
# print(user["name"])
# print(user["girl"])
# print(user["age"])
# print(user.keys())
# print(user.values())
# print(user.items())

# for i in user:
#     print(i,"",user[i])

# for i in user.values():
#     print(i)  

# for i in user.keys():
#     print(i)

# for i,j in user.items():
    # print(i,j)

# if "name" in user:
#     print("yes")
# # #changing values
# user.update({"gender":"female"})
# print(user)
# user["age"]=35
# print(user)
# user.pop("age")
# print(user)
# user.clear()
# print(user)

# # #nested dictionary
# users={
#    "user1": {
#        "name":"Abi",
#        "agr":21,
#        "married":True
#  },
#  "user2":{
#      "name":"Sakthi",
#      "age":18,
#      "maried":False
#  }
     
#  }
# print(users) 

# a=[1,2]
# b=[1,2]
# c=a
# print(id(a))
# print(id(c))
# print(id(b))
# print(a is c)

# dic={
#     "name":"shakshi",
#     "age":20,
#     "gender":"female",
#     "married":False
# }
# print(dic)
# print(type(dic))
# print(dic["name"])
# print(dic["gender"])
# print(dic["married"])
# print(dic.values())
# print(dic.keys())
# print(dic.items())

# for i in dic:
#     print(i,"",dic[i])
# for i in dic.values():
#     print(i)
# for i in dic.keys():
#     print(i)
# for i in dic.items():
#     print(i)
# if "name" in dic:
#     print("yes")
# if "age" in dic:
#     print("ya")

# dic.update
# print(dic)
# dic["age"]=18
# print(dic)
# dic.pop("gender")
# print(dic)
# dic.clear()
# print(dic)

#identy operator
# a=[1,2]
# b=[1,2]
# c=a
# print(id(a))
# print(id(b))
# print(id(c))
# print(a is c)
# print(a is b)
# print(a==b)

# print(a is not c)
# print(a is not b)
# print(a!=b) 

#membership operator
# a=[24,54,65,76]
# print(54 in a)
# print(22 not in a) 

#functions
# def welcome():
#     print("welcomr to my house")
# welcome()
# welcome()
# welcome() 

#no return type without arguments fucntion
# def add():
#     a=int(input("Enter the value of A:"))
#     b=int(input("Enter the value of B:"))
#     c=a+b
#     print("total",c)
# add() 

#no return type with arguements function 
# def sub(a,b):
#     c=a-b
#     print("difference:",c)
# sub(55,2)


# return type withount argument function
# def mul():
#     a=int(input("Enter the value of A:"))
#     b=int(input("Enter the value of B:"))
#     c=a*b
#     return c
# x=mul()
# print("Mul",x)

#return type with argument python
# def div(a,b):
#     c=a/b
#     return c
# x=div(25,2)
# print("division",x)

#arbitary arguments function(*)
# def class_10(*students):
#     print(students)
#     for i in students:
#         print(i)
# class_10("abi","sakthi","nisha","veera")

#keyword argument function
# def messege(name,age):
#     print(name,"age is",age)
# messege(age=45,name="kasi")

#arbitary keyword argument (**)
# def bioData(**data):
#     print(data)
# bioData(name="saritha",age=40,gender="female")

#defalt parameter function
# def user(name,city="bangalore"):
#     print(name,"is from",city)
# user("abi","viluppuram")
# user("veera")
# user("sakthi","coimbatore")

#passing a list as an argument in funtion
# def students(marks):
#     return sum(marks)
# print(students([55,75,44,76]))

#recursive function
# def factorial(a):
#     if a==1:
#         return 1
#     else:
#         return(a * factorial(a - 1))
    
# print("Factorial:",factorial(5))

#labbda funtion
# c=lambda a: a + 50
# print(c(5))

# c=lambda a,b:a*b
# print(c(10,25))

# c=lambda a,b:a/b
# print(c(10,25))

#date time import datetime
# import datetime as dt
# current_date=dt.date.today()
# print("current:",current_date)

# new=dt.date(2002,3,28)
# print(new)
# print("Year:",new.year)
# print("Month",new.month)
# print("day:",new.day)
# print("---------------")
# a=dt.time(10,30,4,666606)
# print(a)
# print("hour:",a.hour)
# print("minute:",a.minute)
# print("second:",a.second)
# print("microsecond:",a.microsecond)
# print("----------------")
# current_time=dt.datetime.now()
# print("current time:",current_time)
# print("---------------")
# new=dt.datetime(2005,9,25,12,30,20)
# print(new)
# print(new.time())
# print(new.date())
# print("--------------")
# current_date=dt.datetime.now()
# new_year=dt.datetime(2025,1,1)
# difference=current_date-new_year
# print(difference)

#math function
# import math
# print(math.sqrt(4))
# print(math.ceil(1.5555))
# print(math.floor(1.5555))
# print(math.factorial(5))
# print(math.fabs(-5))
# print(math.pow(2,3))
# print(math.log2(2))
# print(math.log10(2))
# print(math.pi)
# print(math.e)

#try block
# try:
#     a=10/0
# except Exception as e:
#    print(e) 

#try else block
# try:
#     a=10/25
# except Exception as e:
#    print(e) 
# else:
#     print("A value:",a)

#try finally block
# try:
#     a=10/25
# except Exception as e:
#     print(e)
# else:
#     print("a value:",a)
# finally:
#     print("thank you")

#types of EXception
# print(dir(locals()['__builtins__']))
# print(len(dir(locals()['__builtins__']))) 

#NameError exception
# try:
#     print(a)
# except NameError as  e:
#     print("A is not defined")

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print("denominator cant be zero")

# try:
#     a=int("Abitha")
# except ValueError as e:
#     print("plrse enter number only")

# try:     
#      a=[10,20,30,40]
#      print(a[10])
# except IndexError as e:
#      print("invalid index")
# try:
#     f=open ("test.txt")
# except FileNotFoundError as e:
#     print("file not found")
# else:
#     print(f.read()) 

#multiple exception
# try:
#      a=10/20
#      print(a)
#      b=[10,20,30,40]
#      print(b[10])
# except ZeroDivisionError :
#      print("denominator cant be zero")
# except IndexError:
#      print("invalid index")

#class
# class car():
#     pass

# a=10
# print(type(a))
# print(type(car))
# swift=car()
# print(isinstance(swift,car))
# print(isinstance(a,int))
# print(type(swift))

#class
# class MyClass:
#     a=5
# # print(MyClass)
# c1=MyClass()
# print(c1.a)

# class member:
#     def __init__(self,name,age,department):
#         self.name=name
#         self.age=age
#         self.department=department
# p1=member("abi",21,"computer")
# print(p1.name)
# print(p1.age)
# print(p1.department)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}({self.age})"
# p1=person("abi",21)
# print(p1)

# class students:
#     def __init__(self,name,age,gender,city):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.city=city
# p1=students("abi",21,"female","viluppuram")
# print(p1.name)
# print(p1.age)
# print(p1.gender)
# print(p1.city) 

# class member:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfun(self):
#         print("Hello my name is "+self.name)
# p1=member("Sakthi",19)
# p1.myfun()

# class person():
#     def __init__(mysillyobject,name,age):
#         mysillyobject.name=name
#         mysillyobject.age=age

#     def myfun(abc):
#         print("Hello my name is "+abc.name)

# p1=person("nisha",15)
# p1.myfun()

# class car():
#     pass
# a=10
# print(type(a))
# print(type(car))
# swift=car()
# print(isinstance(swift,car))
# print(isinstance(a,int))
# print(type(swift)) 

# class student:
#     name="saritha"
#     age=40
#     #getattr methos
# print(getattr(student,"name"))
# print(getattr(student,"age"))
# print(getattr(student,"gender",'no such Attribute Found'))
# #dot . notation
# print(student.name)
# print(student.age)
# #setattr
# setattr(student,"name","kasi")
# print(student.name)
# setattr(student,"gender","male")
# print(student.gender)
# print(student,"city","vilupuram")
# print(student.city)

# class student:
#     name="abi"
#     age=21
#     def printall(self,department):
#         print("Name:",student.name)
#         print("Age:",student.age)
#         print("Department:",department)
# o=student()
# student.printall(o,"computer sceince")
class user:
    def __init__(self):
        print("")