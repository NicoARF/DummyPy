from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Configurar el controlador del navegador Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.saucedemo.com/"
driver.get(url)

driver.close()