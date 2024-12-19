# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://www.google.com")
# time.sleep(20)


# import time
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver 
# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
# search_input=driver.find_element( by="name",value="q")
# time.sleep(2)
# search_input.send_keys("sagasoft.io")
# time.sleep(3)
# search_input.send_keys(Keys.RETURN)
# time.sleep(20)
# driver.quit()


# from selenium import webdriver


# browser=webdriver.Chrome()
# browser.get("https://selenium.dev/")
# browser.maximize_window()

# from selenium import webdriver
# from selenium.webdriver.common.keys import keys
# from selenium.webdriver.common.by.import By
# driver=webdriver.Firefox


# from selenium import webdriver

# # Set up the driver (example with Chrome)
# driver = webdriver.Chrome()

# # Navigate to a website
# driver.get("https://example.com")

# # Get the page title
# actual_title = driver.title
# expected_title = "Example Domain"

# # Assert the page title
# assert actual_title == expected_title, f"Title mismatch! Expected: {expected_title}, Got: {actual_title}"

# # Close the driver
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()

# driver.get("http://www.python.org")

# # assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")


# elem.clear()
# elem.send_keys("Pycon")
# elem.send_keys(Keys.RETURN)
# time.sleep(8)

# assert "no result found" not in driver.page_source
# time.sleep(20)

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://sagasoft.io/signup")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a.btn-white").click()
time.sleep(10)

# driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/form/div[1]/input")
# driver.click()
element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH," /html/body/div/div/div/div[2]/div/div/div/form/div[1]/input") )
)
element.send_keys("abithakabithak561@gmail.com")

 

#  /html/body/div/div/div/div[2]/div/div/div/form/div[1]/input
# /html/body/div/div/div/div[2]/div/div/div/form/div[2]/div/input
# /html/body/div/div/div/div[2]/div/div/div/form/div[3]/input


  