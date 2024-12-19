import requests
from bs4 import BeautifulSoup
stord_books=[]

for i in range(1,18):

    url =f"https://vglug.org/category/free-ebooks/page/{i}/"

if requests.get(url).status_code==200:
    print(stord_books)
reponce = requests.get(url).text

html_stor = BeautifulSoup(reponce,"html.parser")


# ckack_book_name="கணிக்கோவை"

stord_books=[]
for i in html_stor.find_all("h2",class_="entry-title"):
    bookname=i.find("a",{'rel':'bookmark'})
    stord_books.append(bookname.text)

with open("book_na.txt","w") as file:
   for name in stord_books:
        file.writelines(f"{name}\n")


# if ckack_book_name in stord_books:
#     print("iruuku")
# else:
#     print("illaeh")