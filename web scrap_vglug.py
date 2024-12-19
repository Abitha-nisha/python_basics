# import requests
# from bs4 import BeautifulSoup
# stored_book=[]
# for i in range(1,18):

#   url=f"https://vglug.org/category/free-ebooks/page/{i}/"
#   if requests.get(url).status_code==200:
#     print(stored_book)
    
    
#     response=requests.get(url).text
#     soup=BeautifulSoup(response,'html.parser')

    
#     for i in soup.find_all("h2",class_="entry-title"):
#         book_name=i.find("a",{'rel':'bookmark'})
#         stored_book.append(book_name.text)
#     check_book_name="கணிக்கோவை"
#     if check_book_name in stored_book:
#         print("Yes")

# for i in stored_book:
#    print(i)


# with open("book.stored.txt","w")as file:
#     for name in stored_book:
#         file.writelines(f"{name}\n")
        

#         import requests
# from bs4 import BeautifulSoup

# all_book_names=[]

# for  i in range(1,18):
#     url=f"https://vglug.org/category/free-ebooks/page/{i}/"    
    
#     if requests.get(url).status_code == 200:
#       print(all_book_names)
    
#       responce = requests.get(url).content
#     soup=BeautifulSoup(responce,features='html.parser')

# books_name=soup.find_all("header",class_="entry-header")
# for i in books_name:
#             book=i.find("h2",class_="entry-title").a.text
#             all_book_names.append(book)

# with open("book_title.txt","w") as file:
#     for name in all_book_names:
#         file.writelines(f"{name}\n")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the target URL
    driver.get("https://sagasoft.io/signup")

    # Wait for the element to be present
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "form-control"))  # Replace 'form-control' with the actual id
    )

    # Interact with the element
    email_input.send_keys("abithakabithak561@gmail.com")

    # Additional interactions (if needed)
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-button"))  # Replace 'submit-button' with the actual id
    )
    submit_button.click()

finally:
    # Close the browser
    driver.quit()
