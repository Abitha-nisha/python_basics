# user={
#     "abi":90909090,
#     "sakthi":89898989,
#     "nisha":78787878
# }
# user_values=90909090
# for name,phone in user.items():
#     if name == user_values:
#         print(phone)
#     if phone == user_values:
#         print(name)

# student_id={112,114,116,118,115}
# print("student id:",student_id)
# print(type(student_id))

# country_capitals={
#     "germeny":"berlin",
#     "canada":"ottava",
#     "england":"london"
# }
# print(country_capitals['germeny'])
# print(country_capitals['england'])

# country_capitals={
#     "germany":"berlin",
#     "canada":"ottawa",
# }
# country_capitals["italy"]="rome"
# print(country_capitals)

# country_capitals={
#     "germany":"berlin",
#     "canada":"ottawa",
# }
# country_capitals.clear()
# print(country_capitals)

# country_capitals={
#     "united states":"washington D.C.",
#     "italy":"remo",
# }
# for country in country_capitals:
#     print(country)
# print()
# for country in country_capitals:
#     capital=country_capitals[country]
#     print(capital)

# class  myclass:
#     a=5
# a1=myclass
# print(a1.a)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# a1=person(input("enter ur name :"),int(input("enter ur age :")))
# print(a1.name)
# print(a1.age)


# class Dog:

#     # class attribute
#     name = "abi"
#     age=41

#     # Instance attribute
#     def __init__(self, name,age):
#         self.name = name
#         self.age=age

# # Driver code
# # Object instantiation
# Rodger = Dog("python",23)
# Tommy = Dog("hello",21)
# ur_age = Dog("dummy",42)

# # Accessing class attributes
# print("python is a {}".format(Rodger.__class__.name))
# print("hello is also a {}".format(Tommy.__class__.name))
# print("dummy is also a {}".format(ur_age.__class__.age))

# # Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))
# print("My age is {}".format(ur_age.name))


# print("My name is {}".format(Rodger.age))
# print("My age is {}".format(Tommy.age))
# print("My age is {}".format(ur_age.age))

# class student:
#     name="nila"
#     age=22
#     gender = "female"
#     def abitha(): #printall
#         print("name:",student.name)
#         print("Age:",student.age)
#         print("gender:",student.gender)
# student.abitha()
# print(student.__dict__)
# getattr(student,"abitha")()
# student.__dict__["abitha"]()

# a="beautiful"
# print(a)
# print(a[1:5])
# print(a[1:-1])
# print(a[:6])
# print(a[::-1])


# Input three numbers from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# # Find the largest number
# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3
# # Display the result
# print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")

# Input two numbers from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # Add the two numbers
# result = num1 + num2
# # Display the result
# print(f"The sum of {num1} and {num2} is {result}.")

# Input two numbers
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# print(f"Before swapping: a = {a}, b = {b}")

# # Swap using tuple unpacking
# a, b = b, a

# print(f"After swapping: a = {a}, b = {b}"


# n=int(input("enter a num:"))
# sum=0
# for i in range(1,n+1):
#     sum +=i
# print(f"sum of first {n} natural number is {sum}")
    
# for i in range(5,0,-1):
#     print(i)

# for i in reversed(range(1,6,1)):
#     print(i)


# name="abii"
# for i in name:
#     print(name)

# name="saritha"
# for i in name[::-1]:
#     print(i,end=" ")


# sentence="hello guys welcome to my,home."
# count=0
# for i in sentence.split():
#     count=count+1
# # print(f"there are {count} i in the sentence.")
# print(count)

# cars=["audi","bmw","toyato"]
# for i in cars:
#     print(i)

