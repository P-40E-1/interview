import os
from selenium import webdriver
import time

os.environ['PATH'] += r"C:\SeleniumDrivers\chrome-win64"
driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.implicitly_wait(5)

time.sleep(10)

driver.quit()