import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")

driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(1)
driver.find_element_by_name("q").send_keys("harman")
time.sleep(1)
driver.find_element_by_name("btnK").click()
time.sleep(5)
driver.close()
print("Test case has successfully completed")