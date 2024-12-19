# a=3%5
# print(a)





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
# for i in range(1,1001):
#     if(i%3==0 and i%5==0):
#         count=count+1
#         print(count)


# a=[]
# print("Enter 10 numbers:")
# for i in range(5):
#     num=int(input("Enter num "+str(i+1)))
#     a.append(num)
#     print(a)

# user={
#     "name":"abi",
#     "age":"21",
#     "married":False

# }
# print(user)
# print(type(user))
# print(user["name"])
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
# for i  in user.items():
#     print(i)

# if "name" in user:
#     print("yes")
# if "age" in user:
#     print()

# user={
#     "abii":78904895094,
#     "sakthi":52673873998,
#     "nisha":876788989909,
# }


# user_value="abii"

# for name,phonenumber in user.items():
#     # print(name,phonenumber)
#     if name == user_value:
#         print(phonenumber)
#     elif phonenumber == user_value:
#         print(name)

# import requests
# from bs4 import BeatifulSoup


# def ExractData(url):
#     response = requests.get(url=url).content
#     soup=BeatifulSoup(response, 'htmlparser')
#     title
#     thead=title.find("thead")
#     print(thead)
# ExractData(url="https://vglug.org/category/free-ebooks/")

# user={
#     "saritha":123456789,
#     "abitha":987654321,
#     "sakthi":123459876,
   
# }
# user_values="abitha"
# for name,phonenum in user.items():
#     print(name,phonenum)
#     if name==user_values:
#         print(phonenum)
#     elif phonenum==user_values:
#         print(name)

# a="abi""sakthi"
# print(a)
# print(type(a))
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.count("a"))
# print(a.endswith("ed"))
# print(a.find("i"))
# print(a.replace("i","9"))
# b="saritha 123"
# print("IS UPPER:",b.isupper())
# print("IS LOWER:",b.islower())
# print("IS ALPHA NUMBERIC:",b.isalnum())
# c="she\nis\ngood"
# print(c)
# print(c.splitlines())
# print(c.splitlines(True))
# d="kasi,saritha,abi"
# print(d.split(","))
# f="     sakkthi    "
# print(len(f))
# print(len(f.strip()))
# print(len(f.lstrip()))
# print(len(f.rstrip()))

# a="people"
# print(a)
# print(a[0:2])
# print(a[:5])
# print(a[1:])
# print(a[-1])
# print(a[-2:-1])
# print(a[:-1])
# print(a[::-1])

# a=10
# b=20
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# import requests
# from bs4 import BeautifulSoup
# all_book_title=[]
# # for i in range(1,17):

# #   url=f"https://vglug.org/category/free-ebooks/page/{17}/"
# #   if requests.get(url).status_code==200:
# #      print(all_book_title)

# response=requests.get(url).content
# soup=BeautifulSoup(response,features='html.parser')
# book_title=soup.find_all("header",class_="entry-header")
# for i in book_title:
#     book=i.find("h2",class_="entry-title")
#     all_book_title.append(book)
    
# with open("book_name.txt","w") as file:
#    for name in all_book_title:
#       file.writelines(f"{name}\n")

import requests
from bs4 import BeautifulSoup
stored_book=[]
for i in range(1,18):

  url=f"https://vglug.org/category/free-ebooks/page/{i}/"
  if requests.get(url).status_code==200:
    print(stored_book)
    
    
    response=requests.get(url).text
    soup=BeautifulSoup(response,'html.parser')

    
    for i in soup.find_all("h2",class_="entry-title"):
        book_name=i.find("a",{'rel':'bookmark'})
        stored_book.append(book_name.text)
    check_book_name="கணிக்கோவை"
    if check_book_name in stored_book:
        print("Yes")

# for i in stored_book:
#    print(i)


# with open("book.stored.txt","w")as file:
#     for name in stored_book:
#         file.writelines(f"{name}\n")
        

# # import requests
# # from bs4 import BeautifulSoup

# # url="https://vglug.org/category/free-ebooks/page/2/"

# # response=requests.get(url).text
# # soup=BeautifulSoup(response,features='html.parser')
# # book_name=soup.find_all("header",class_="entry-header")





