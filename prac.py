# #tuple
# a=(2,3.8,True ,'Veera')
# print(a)
# b=list(a)
# print(b)
# b.append('Nisha')
# print(b)
# if "Veera" in a:
#     print("Yes")
# else:
#     ("No")
# a=tuple(b)
# print(a)
# print(len(a))
# for i in a:
#     print(i)
# c=(1,88,98,54)
# print(max(c))
# print(min(c))

#nested tuples
# a=(11,12,13,14,15)
# b=(16,17,18,19,20)
# c=a,b
# print(c)
# print(c[0])
# print(c[1])
# print(c[0][2])

#List constructor
# print(list(range(4)))
# print(list("ABITHA"))
# a=[10,40,1000,100,70]
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# b=["cat","book","lion","tiger"]
# print(b)
# b.sort()
# print(b)
# b.sort(reverse=True)
# print(b)
# b.sort(key=len)
# print(b)

#list
# name=["Anitharoobi"]
# print(name)
# name.append("Anitha")
# name.append("Dhivya")
# print(name)
# name1=["Elaiyanila","Monisha"]
# name.extend(name1)
# print(name)
# name.insert(0,"Abitha")
# print(name)

#list ex:1
# a=[14,25,55,25,55]
# print(a)
# a.clear()
# print(a)
# a=[14,25,55,25,55]
# b=a.copy()
# print(b)
#ex 2
# a=[14,54,34,66,98,66]
# print(a)
# print(a.count(66))
# print(a.index(34))
# print(len(a))
# print(max(a))
# print(min(a))
# a.pop(3)
# print(a)
# a.remove(54)
# print(a) 

#ex 3
# a=[3,True,"Sakthi",4.5,[1,2,3,4]]
# print(a)
# print(type(a))
# print(a[0],type(a[0]))
# print(a[1],type(a[1]))
# print(a[2],type(a[2]))
# print(a[3],type(a[3]))
# print(a[4][1])

#ex 4
# a=[5,6,7,9,8]
# print(a)
# a[1]=100
# print(a)
# print(a[2])

#while else:
# for i in range(1,21):
#   if(i==10):
#     break
#   print(i)



# for i in range(1,10):
#     for j in range(1,10):
#         for k in range(1,10):
#             if i+j+k ==13:
#                 print(i,j,k)    

# un={"a","b","c","d","e"}
# su={"e","f","g","i"}
# an=un.intersection(su)
# print(an)
# un.intersection_update(su)
# print(un) 

# g={1,2,3,4,5,6}
# h={'a','b','c','d','e'}
# j=g.union(h)
# print(j)
# g.update(h)
# print(g) 

# n={1,2,3,4,5}
# m={5,6,7,8,9}
# o=n.symmetric_difference(m)
# print(o)
# n.symmetric_difference_update(m)
# print(n) 

# q={6,7,8,1,2}
# r={3,4,5}
# s=q.isdisjoint(r)
# print(s)

# r={1,3,4,}
# t={1,3,4,5,6}
# w=r.issubset(t)
# print(w)

# r={1,2,3,4}
# s={1,2,3,4}
# t=r.issuperset(s)
# print(t)

# if 5 > 2:
    # print("five greater than two")

# x=str(3)
# y=int(3)
# z=float(3)
# print(x,y,z)

# x=y=z="orange"
# print(x)
# print(y)
# print(z) 
 
# x="pyhton"
# y="is"
# z="avwsome"
# print(x,y,z)

# x="awesome"
# def myfunc():
#     print("python is" + x)
# myfunc()
    
# f=[4,5,6]
# g=[4,5,6]
# h=g
# print(id(f))
# print(id(g))
# print(id(h))
# print(f is g)
# print(g is h)
# print(f==g)
# print(f is not g)
# print(g is not h)
# print(f!=g)

# def add(a,b):
#     c=a+b
#     print("total:",c)
# add(100,300) 

# def sub():
#     a=int(input("enter number:"))
#     b=int(input("enter number:"))
#     c=a-b
#     print("values:",c)
# sub()

# def div(a,b):
#     c=a/b
#     return c
# d=div(16,3)
# print("divisiom",d)

# def mul():
#     a=int(input("enter the number:"))
#     b=int(input("enter the number:"))
#     c=a*b
#     return c
# f=mul()
# print("mul",f)

# def ds_10(*colors):
#     print(colors)
#     for i in colors:
#         print(i)
# ds_10("red","blue","green","yellow")

# ishvarya=input()
# if ishvarya=="breakup":
#     print("gowtham weds kundavi")
# else:
#     print("gowtham weds ishvarya")

# para=[]
# print("enter the para:")

# while True:
#     line=input()
#     if line:
#         para.append(line)
#     else:
#         break
#     print(para)
#     output='/n'.join(para)
#     print(output)

# a=[]
# print(" enter paragraph :")

# while True:
#     b=input()
#     if b:
#         a.append(b)
#     else:
#         break
#     print(a)
#     c='/n'.join(a)
#     print(c)

# import requests
# source = requests.get("https://vglug.org/")
# print(source)

# person={
#     "saritha":9886575971,
#     "sakthi":8870932429,
#     "santhiya":8489716029,
#     "shakshi":8754688304,
# }


# person_values=8489716029
# for name,number in person.items():
#     # print(name,number)
#      if name==person_values:
#        print(number)
#      elif number==person_values:       
#         print(name)


# for i in range(97,102,1):
#     for j in range(65,70,1):
#      print(chr(j),end="")
#     print("")

# class person:
#     department='computer science'
#     city='bangalore'
# getattr(person,'department')
# print(getattr(person,'department'))
# print(getattr(person,'city'))
# print(person.department)
# print(person.city)
# setattr(person,'name',"abii")
# print(person.name)
# setattr(person,'gender','female')
# print(person.gender)
# person.age=21
# print(person.age)
# print(person.__dict__)
# delattr(person,'city')

# duplicate=['abi','sakthi','abi','nisha','nisha']
# original=[]
# for i in duplicate:
#     if i not in original:
#         original.append(i)
#         print(i)

from collections import Counter
my_list = [1, 2, 3, 4, 5, 6, 2, 3, 4, 4]
counter = Counter(my_list)
duplicates = [item for item, count in counter.items() if count > 1]
print("Duplicates:", duplicates)
