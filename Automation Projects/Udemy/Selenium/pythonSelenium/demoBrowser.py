from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://google.com")
print('driver Title:',driver.title)
print('Driver name:',driver.name)
print('Driver URL:',driver.current_url)
driver.quit()