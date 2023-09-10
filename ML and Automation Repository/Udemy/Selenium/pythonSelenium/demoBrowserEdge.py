from selenium import webdriver
#from webdriver_manager.Edge import EdgeDriverManager
#driver = webdriver.Edge(executable_path=EdgeDriverManager().install())
driver.get("http://www.google.com/")
print(driver.title)
driver.maximize_window()
#webdriver class contains all the driver methods that I can import like 'get,close,quit' etc
driver.get("https://shrirachana.com")
print('driver Title:',driver.title)
print('Driver name:',driver.name)
print('Driver URL:',driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.minimize_window()
driver.maximize_window()
driver.close()

#driver.quit()

"""close() closes only the current window on which Selenium is running automated tests. The WebDriver session, however, remains active. 
On the other hand, the driver. quit() method closes all browser windows and ends the WebDriver session."""