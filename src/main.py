from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = './drivers/chrome/chromedriver'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

url = "https://www.saucedemo.com/"
driver.get(url)

driver.close()