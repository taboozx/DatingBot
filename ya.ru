from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


file = open("C:/Users/Tbz/Desktop/badoo_myself.txt", "r")
data = file.read()

driver = webdriver.Firefox()
driver.get("ya.ru")


 string=driver.find_element_by_xpath("//*[@id="text"]")
 string.send_keys("", data)
   