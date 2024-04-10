from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")

service=ChromeService(ChromeDriverManager().install())
# Configurar el controlador del navegador Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.saucedemo.com/"
driver.get(url)
assert "Swag Labs" in driver.title, print("El título de la página no es 'Swag Labs'")
print(driver.title)

driver.close()