Google Maps automation with Python
Launch google maps to go from Destination A to Destination B
Provide different distances depending on the mode of transport
Behaves like a web scraping (Using Selenium)
Pre-Requisites :

Install and import selenium , import time (import sleep) and import drivers (Chrome, Firefox and edge)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
Code :

Launch chrome and google maps

driver.get('#openmaps')
sleep(2)
Function to search ‘From’ and ’To’, print the distance and time it takes to go from Destination A to Destination B


def search_place():
  place = driver.find_element_by_class_name('tactile-searchbox-input')
  place.send_keys('Trichy')
  #Submit the search value by clicking on search button
  submit = driver.find_element_by_xpath('/html/body/div[3]/dev[9]....')
  submit.click()
def direction():
  sleep(10)
  direct = driver.find_element_by_xpath('grab from maps')
  direct.click() 
def destionation_A():
  sleep(10)
  submit = driver.find_element_by_xpath('grab from maps')
  place.send_keys('Bangalore')
  #Submit the search value by clicking on search button
  submit = driver.find_element_by_xpath('grab from maps')
  submit.click()
def print_dest_info():
  sleep(10)
  distance = driver.find_element_by_xpath('grab from maps')
  time_car = driver.find_element_by_xpath('grab from maps')
print('Distance: ', distance.txt)
print('Time: ', time.txt)

search_place()
direction() 
destionation_A()
print_dest_info()

Selenium Automation
Python Programming
