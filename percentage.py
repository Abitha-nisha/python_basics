# megna=input()
# if(megna=="died"):
#     print("surya meets priya")
# else:
#     print("surya weds megna")

# mark=int(input())
# if(mark>35):
#     print("pass")
# else:
#     print("fail")

# income=int(input())
# if(income>70000):
#     print("scholarship is available")
# else:
#     print("not eligible for scholarship")



# a=int(input())
# if(a%3==0 and a%5==0):
#     print("divisible by 3 and 5")
# else:
#     print("not divisible by 3 and 5")

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# f=(a+b+c+d+e)/5
# if(f<35):
#     print("addition")
# else:
#     print("good")

# for i in "Abii":
#     print(i)

# for i in range(1,11):
    # print(i,"x2=",i*2)

# a=int(input())
# b=int(input())
# for i in range(a+1,b):
#     print(i) 

# a=int(input())
# if(a%2==0):
#     print("Even")
# else:
#     print("odd")

# for i in range(1,11):
#     if(i%2==0):
#         print(i)

# e_count=0
# o_count=0
# for i in range(1,11):
#     if(i%2==0):
#         e_count=e_count+1
#     else:
#          o_count=o_count+1
# print(e_count)
# print(o_count)

# count=0
# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         count=count+1
#         print(count)

# sum=0
# for i in range(1,6):
#     sum=sum+i
#     print(sum)

# a=[]
# for i in range(2):
#     num=int(input("Enter num :"+str(i+1)))
#     a.append(num)
#     print(a)

# sum=0
# for i in range(1,10):
#     sum=sum+i
#     print(sum)

# a=42
# b=45
# c=a+b
# print("Total",c)
# print(type(a))
# print(id(a))
# print(id(b))
# print(id(c))

# import keyword
# print(keyword.kwlist)

# a=input("nter the value of A:")
# b=input("nter the value of B:")
# c=a+b
# print(c)

# a=float(input("nter the value of A:"))
# b=float(input("nter the value of B:"))
# c=a+b
# print(c)
# print(type(c))

# name1,name2,name3=input("Enter 3 Name:").split(',')
# print("Name 1:",name1)
# print("Name 2:",name2)
# print("Name 3:",name3)

# a="""Viluppuram GNU/Linux Users Group (VGLUG) is a non profit organization started in 2013, Impression of worldwide Free and Open Source Software movement."""
# print(type(a))
# print(a)

# para=[]
# print("enter the para:")
# while True:
#     line=input()
#     if line:
#         para.append(line)
#     else:
#         break
# print(para)
# output='\n'.join(para)
# print(output)
# 
# a=int(input("enter the a value a:"))
# b=int(input("enter the a value b:"))
# c=a+b
# print(c)

# name="abi write a program".split(",")
# print(name)

# a="Abitha sakthi"
# print(a)
# print(type(a))
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.count("t"))
# print(a.endswith("ed"))
# print(a.find("i"))
# print(a.find("i" , 5))
# print(a.replace("i" , "0"))

# b="abitha234"
# print("IS UPPER:", b.isupper())
# print("Is Lower:",b.islower())
# print("Is Alpha Nmberic:",b.isalnum())
# print("Is Alpha:",b.isalpha())

# c="she\nis\ngood"
# print(c)
# print(c.splitlines())
# print(c.splitlines(True))
# d="kasi,saritha,abitha"
# print(d.split(","))

# f="     sakthi    "
# print(len(f))
# print(len(f.strip()))
# print(len(f.lstrip()))
# print(len(f.rstrip()))
# g='28-03-2002'
# print(g.partition("-"))

#  s a m p l e
#  0 1 2 3 4 5
# -6-5-4-3-2-1
# a="sample"
# print(a)
# print(a[0:2])
# print(a[:5])
# print(a[1:])
# print(a[-1])
# print(a[-2:-1])
# print(a[:-1])
# print(a[::-1])

# s="beautiful"
# print(s)
# print(s[0:5])
# print(s[5:-1])
# print(s[::-1])

# a=123
# b=10
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(2**3)

# a=125
# print(a)
# a += 5
# print(a)
# a -= 10 
# print(a)
# a *= 10 
# print(a)
# a /= 10 
# print(a)
# a %=10 
# print(a)
# a **=10 
# print(a)
# a //=10 
# print(a)

# a = 10
# b =20
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >=  b)
# print(a <= b)

# a=25
# b=45
# print(a&b)
# print(a|b)
# print(a^b)
# print(~a)
# print(a<<2)
# print(a>>2)

# a=int(input("Enter the number:"))
# if(a%2==0):
#     print("Even")
# else:
#     print("Odd")

# name=input("name:")
# age=int(input("age:"))
# if(age>=18):
#     print(name,"age is",age,"eligible for vote.")
# else:
#     print(name,"age is",age,"not eligible for vote.")

# tam=int(input("Tamil:"))
# eng=int(input("English:"))
# math=int(input("Maths:"))
# sci=int(input("Science:"))
# soc=int(input("Social:"))
# total=(tam+eng+math+sci+soc)
# average=(total)/5
# print(total)
# print(average)
# if(average >= 90 and average<=100):
#     print("A Grade")
# elif(average >= 80 and average<90):
#     print("B Grade")
# elif(average >= 70 and average < 79):
#     print("C Grade")
# else:
#     print("no grade")

# a=int(input("ENTER TAMIL MARK :"))
# b=int(input("ENTER ENGLISH MARK :"))
# c=int(input("ENTER MATHS MARK :"))
# total=a+b+c
# print("TOTAL :",total)
# average=(total)/3
# print("AVERAGE :",average)
# if a>=35 and b>=35 and c>=35:
#     print("PASS.")
#     if average>=90 and average<=100:
#         print("A GRADE")
#     elif average>=80 and average<=89:
#         print("B GRADE")
#     elif average>=70 and average>=79:
#         print("C GRADE")
#     else:
#         print("D GRADE")
# else:
#     print("FAIL")
#     print("NO GRADE")

# days=int(input("Enter The Days :"))
# if(days==0):
#     print("NO FINE.")
# elif (days >= 1 and days <= 5):
#     print("FINE AMOUNT:",days * 0.5)
# elif (days >= 5 and days <= 10):
#     print("FINE AMOUNT:",days * 1)
# elif(days >= 10 and days <= 30):
#     print("FINR AMOUNT:",days * 5)
# else:
#     print("MEMBERSHIP CANCEL")

# s1=int(input("Enter Your Mark :"))
# s2=int(input("Enter Your Mark :"))
# s3=int(input("Enter Your Mark :"))
# s4=int(input("Enter Your Mark :"))
# s5=int(input("Enter Your Mark :"))
# total=s1+s2+s3+s4+s5
# average=(total)/5
# print("Total :",total)
# print("Average :",average)
# if s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100:
# # #if total<100:
#     print("DEFIND")
# else:
#     print("NOT DEFIND")

# mark1=int(input("Enter mark 1 :"))
# mark2=int(input("Enter mark 2 :"))
# mark3=int(input("Enter mark 3 :"))
# total=(mark1+mark2+mark3)
# average=(total)/3
# print("Total:",total)
# print("Average:",average)
# if mark1>=35 and mark2>=35 and mark3>=35:
#     print("Result:Pass")
#     if(average>=90 and average<=100):
#         print("Grade : A Grade")
#     elif(average>=80 and average<=89):
#             print("Grade :B Grade")
#     elif(average>=70 and average<=79):
#          print("Grade :C Grade")
#     else:
#          print("Grade : D Grade")
# else:
#     print("Result : Fail")
#     print("Grade : No Grade")

# i=1
# while i <=10:
#     print(i)
#     i+=1
#     print("even no:")
#     n=20
#     i=2
#     while i <=20:
#         print(i)
#         i+=2

# # i=1
# while i <=20:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=1
# while i <=20:
#     if i==9:
#         break
#     print(i)
#     i+=1

# print(list(range(5)))
# print(list(range(10,20)))
# print(list(range(0,21,2)))
# print(list(range(1,20,2)))

# for i in range(0,21,2):
#     print(i)

# for i in range(5):
#     a=int(input("Enter number :"))
#     b=int(input("Enter number :"))
#     print(a+b)

# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print("")

# for i in range(1,11):
    # print(i,"x2=",i*2)

# a=int(input())
# b=int(input())
# for i in range(a +1,b):
#     print(i)
    
# for i in range(2,11,2):
    # print(i)

# for i in range(1,11):
#     if(i%2==0):
#         print(i)

# for i in range(4):
#     a=int(input("Enter number:"))
#     b=int(input("Enter number:"))
#     print(a+b)

# for i in range(6):
#     for j in range(i):
#       print("*",end="")
#     print("")

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("")

# for i in range(97,102,1):
#     for j in range(65,70,1):
#      print(chr(j),end="")
#     print("")
    
# i=1
# while i<=5:
#     if(i==4):
#         break
#     print(i)
#     i+=1
# else:
#     print("loop completed")

# for i in range(1,21):
#     if(i==5):
#         # break
#     # print(i)
# else:
#     print("For loop completed")

# for i in range(3):   
#     for j in range(i):
#         print(j)

# a=[1,2,3,4,5]
# print(a)
# print(type(a))
# a[0]=200
# print(a)
# print(a[1])
# print(a[-1])
# print(a[0:3])
# print(a[1:])
# print(a[:4])

# a=[1,True,"Abi",2.6, [1,2,3,4]]
# print(a)
# print(type(a))
# print(a[0],"type is",type(a[0]))
# print(a[1],"type is",type(a[1]))
# print(a[2],"type is",type(a[2]))
# print(a[3],"type is",type(a[3]))
# print(a[4][1])

# a=[10,25,35,45]
# print(a)
# a.clear()  
# print(a)
# a=[10,25,35,45]
# b=a.copy()
# print(b)
# a=[10,25,35,45,25,4,25]
# print(a.count(25))
# print(a.index(25))
# print(len(a))
# print(max(a))
# print(min(a))
# a.pop(0)
# print(a)
# a=[10,25,35,45,25,4,25]
# a.remove(25)
# print(a)

# names=["Abi"]
# print(names)
# names.append("sakthi")
# names.append("veera")
# names.append("nisha")
# print(names)
# name2=["saritha","kasi"]
# names.extend(name2)
# print(names)
# names.insert(0,"hemanth")
# print(names)

# print(list(range(5)))
# print(list("Hemath"))
# a=[10,50,100,25,85]
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a=["orange","apple","zebra"]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a=["orange","apple","zebra","grape"]
# a.sort(key=len)
# print(a)

# #tuple
# a= (1,2.5, True,"Abi")
# print(a)
# print(type(a))
# print(a[0:])
# print(a[-1])
# print(a[1])
# b=list(a)
# print(b)
# b.append("Sakthi")
# print(b)
# print(type(b))
# a=tuple(b)
# print(a)
# print(type(a))

# for i in a:
#     print(i)

# if "Abi" in a :
#     print("yes")
# else:
#     print("no")
# print(len(a))
# a=(1,)
# print(type(a))
# del a
# a=(1,2,7,4)
# b=(5,6,7,8)
# c=a+b
# print(c)
# print(c.count(7))

#nested tuples
# a=(1,2,3,4)
# b=(5,6,7,8)
# c=a,b
# print(c)
# print(c[0])
# print(c[1])
# print(c[0][1])
# m=('Abi',) *10
# print(m)
# d=(1,3,6,8)
# print(min(d))
# print(max(d))

# #set 
# name={"Abi","Sakthi","Nisha"}
# name.add('veera')
# print(name)
# print(type(name))
# print(list(name))
# chtype=list(name)
# print(type(chtype))
# print(chtype)

# # # set 
# name={"Abi","Anitha","Dhivya"}
# print(name)
# print(type(name))
# #value using for loop
# for names in name:
#     print(names)
# # #addin new element
# name.add("Monisha")
# print(name)
# # #update another data
# a={"Surya","Vijay","Ajith"}
# name.update(a)
# print(name)
# name.remove("Monisha")
# print(name)
# name.discard("Abi")
# print(name)
# name.pop()
# print(name)
# name.clear()
# print(name)
# del name
# print(name)

# my_set=set({"a","b","c"})
# print(my_set)
# my_set.add("d")
# print(my_set)

# set={"book",10,True,25.5,"abi"}
# print(set)  

# normal_set={"a","b","c"}
# print(normal_set)
# frozen_set=("d","e","g")
# print(frozen_set)

# people={"alex","akaash","abishek" }
# print("people:",end="")
# print(people)
# people.add("prathap")
# for i in range(1,6):
#     people.add(i)
# print("\nSet after adding element:", end = " ")
# print(people)  

# a={"abi","sakthi","veera","abi"}
# print(a) 


# #union
# a={1,2,3,4}
# b={"a","b","c","d"}
# c=a.union(b)
# print(c)
# a.update(b)
# print(a)

#intersection
# a={1,2,3,4,5}
# b={5,6,7,8,9}
# c=a.intersection(b)
# print(c)
# a.intersection_update(b)
# print(a)

#symmentric difference
# a={1,2,3,4,5}
# b={5,6,7,8,9}
# c=a.symmetric_difference(b)
# print(c)
# a.symmetric_difference_update(b)
# print(a)

# isdisjoin
# d={5,6,7,8,9}
# e={5,6,7,8,9}
# f=d.isdisjoint(e)
# print(f)
# f=d.issubset(e)
# print(f)
# f=d.issuperset(e)
# print(f)

# print("\'it\'s Hero Time!\n\t\t-Ben 10")















