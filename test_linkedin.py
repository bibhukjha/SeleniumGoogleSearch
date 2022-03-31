import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
username = input("Enter username: ")
password = input("Entre Password:")

print("Test cases started")

driver.maximize_window()
driver.get("https://www.linkedin.com/login")
time.sleep(5)
driver.find_element_by_name("session_key").send_keys(username)
time.sleep(5)
driver.find_element_by_name("session_password").click(password)
time.sleep(5)
driver.close()
print("Test case has successfully completed")