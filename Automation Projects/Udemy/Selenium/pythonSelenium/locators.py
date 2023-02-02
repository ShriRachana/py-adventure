#Import Chrome Driver Module

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
#Open said url
driver.get("http://rahulshettyacademy.com/angularpractice/")
print('driver Title:',driver.title)
print('Driver name:',driver.name)
print('Driver URL:',driver.current_url)
driver.implicitly_wait(30)

#ID, Xpath, CSS Slector, classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.implicitly_wait(90)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.implicitly_wait(90)
driver.find_element(By.ID, "exampleCheck1").click()
driver.implicitly_wait(90)

print('driver Title:',driver.title)
print('Driver name:',driver.name)
print('Driver URL:',driver.current_url)
driver.implicitly_wait(30)

#xpath format : //tagname[@attribut='value']
