
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

chrome_driver_path = "C:\\chromedriver\\chromedriver.exe"

os.environ["PATH"] += os.pathsep + chrome_driver_path

driver = webdriver.Chrome()

driver.get("https://nexign.com/ru")

store_link = driver.find_element(By.XPATH, "//span[contains(text(),'Store')]")
store_link.click()

time.sleep(2)

developer_products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/ru/store']")
developer_products_link.click()

time.sleep(2)

driver.quit()
