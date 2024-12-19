#model:1
# cars =['audi','bwm','toyata']
# for i in cars:
#     print(i)

#model:2
# cars =['audi','bwm','toyata']
# [print(ca)for ca in cars]

#get only keys
# course={'name':'python','language':'java'}
# for x in course.keys():
#     print(x)

#get only values
# course={'name':'python','language':'java'}
# for x in course.values():
#     print(x)

#get keys and values
# course={'name':'python','language':'java'}
# for x,y in course.items():
#     print(x,y)

# fav=['python','c','java','html']
# for lang in fav:
#     if 'html' ==lang:
#         print("i like html")
#         break
# else:
#     print("i dont like html")

# numbers=list(range(0,100))
# for num in numbers:
#     if num > 56:
#         break
#     print(num,end=' ')

# while True:
#     num=input("enter thr number(q for qit):")
#     if num=='q':
#         break
#     print(num)

# for i in range(5):
#     if i==2 or i==4:
#         continue
#     print(i)

# n=0
# while n<=10:
#     n=n+1
#     if n % 2!=0:
#         continue
#     print(n,end=" ")

# list1=[1,2,3]
# list2=[4,5,6]
# for i in list1:
#     for j in list2:
#         print(i, j)
#     print()

# list1=[1,2,3]
# list2=[4,5,6]
# i=0
# while i< len(list1):
#     j=0
#     while j< len(list2):
#         print(list1[i],list2[j])
#         j+=1
#     print()
#     i+=1

# items=[0]
# for ite in items:
#     print(ite)
#     items.append(ite)

# item=0
# while True:
#     print(item)

# li=list(range(1,25))
# even=[]
# odd=[]
# for it in li:
#     if it%2==0:
#         even.append(it)
#     else:
#         odd.append(it)
# print(even)
# print(odd)

# num1=float(input("enter ther num1"))
# num2=float(input("enter the num2"))
# print(num1+num2)

# a=int(input("enter the num:"))
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# a=float(input("enter the num:"))
# b=float(input("enter the num:"))
# c=float(input("enter the num:"))
# if a>=b and b>=c:
#     largest=a
# elif b>=a and b>=c:
#     largest=b
# else:
#     largest=c
# print(f"the laargest{a},{b} and {c} is the {largest} number")


# a=input("ente the string:")
# count=0
# vowel="aeiouAEIOU"
# for char in a:
#     if char in vowel:
#         count=count+1
# print(count)

# text=input("enter the text:")
# reversed_text=""
# for i in text:
#         reversed_text=i+reversed_text
# print(reversed_text)


# for i in range(1,11):
#     print(i,"x2=",i*2)

# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)

# numbers=[1,2,3,4,4,5,5,6,5]
# unique_num=[]
# for num in numbers:
#     if num not in unique_num:
#         unique_num.append(num)
# print(unique_num)

# file_name=input("enter the filename:")
# try:
#     with open(file_name,'r') as file:
#         lines=file.readlines()

#     line_count=len(lines)
#     word_count=sum(len(line.split()) for line in lines)
#     char_count=sum(len(lines)for line in lines)
#     print(line_count)
#     print(word_count)
#     print(char_count)

# except FileNotFoundError:
#     print("the file is not exist")

# Input: Get the file name and text to append from the user
# file_name = input("Enter the file name: ")
# text_to_append = input("Enter the text to append: ")

# try:
#     # Append text to the file
#     with open(file_name, 'a') as file:
#         file.write(text_to_append + '\n')
    
#     # Read the updated file
#     with open(file_name, 'r') as file:
#         updated_content = file.read()
    
#     # Output: Display the updated content
#     print("\nUpdated File Content:")
#     print(updated_content)

# except FileNotFoundError:
#     print(f"The file '{file_name}' does not exist. Please check the file name and try again.")


# filename=input("enter the filename:")
# text_append=input("enter the append line:")
# try:
#     with open(filename,'a') as file:
#         file.write(text_append + '\n')
#     with open(filename,'r') as file:
#         update_content=file.read()
#     print("update the line")
#     print(update_content)
# except FileNotFoundError:
#     print(" this file not exisiting")

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* factorial(n-1)
# num=int(input("enter the num:"))
# if num < 0:
#     print("factorial is not ")
# else:
#     print(f"the {num} is {factorial(num)}")


# sentence=input("enter the sen:")
# words=sentence.lower().split()
# word_count={}
# for word in words:
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1
# print("\nword frequincies:")
# for word,count in word_count.items():
#     print(word,count)

# dict1 = {'a': 5, 'b': 1, 'c': 3}
# dict2 = {'d': 4, 'e': 2, 'f': 6}
# merged_dict = {**dict1, **dict2}
# sorted_dict = dict(sorted(merged_dict.items(), key=lambda item: item[1]))
# print("Merged and Sorted Dictionary:", sorted_dict)


# squares = [n ** 2 for n in range(1, 11)]
# print(squares)


# squares_dict = {n: n ** 2 for n in range(1, 11)}
# print(squares_dict)

# class BankAccount:
#     # Step 1: Initialize the balance to 0 or the given initial amount
#     def __init__(self, initial_balance=0):
#         self.balance = initial_balance
    
#     # Step 2: Method for depositing money
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: ${amount}")
#         else:
#             print("Deposit amount must be positive.")
    
#     # Step 3: Method for withdrawing money
#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Withdrew: ${amount}")
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Withdrawal amount must be positive.")
    
#     # Step 4: Method for displaying the balance
#     def display_balance(self):
#         print(f"Current balance: ${self.balance}")

# # Step 5: Create an instance of BankAccount and test the methods
# account = BankAccount(100)  # Initial balance of $100

# # Test deposit
# account.deposit(50)  # Deposit $50

# # Test withdrawal
# account.withdraw(30)  # Withdraw $30

# # Test displaying balance
# account.display_balance()  # Display the current balance


# rows=int(input("enter the rowa:"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# rows=int(input("enter the num:"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         square=i*j
#         print(square,end=" ")
#     print()
