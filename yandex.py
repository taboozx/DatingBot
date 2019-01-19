from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import datetime

file = open("C:/Users/Tbz/Desktop/badoo_myself.txt", "r")
data = file.read()

driver = webdriver.Firefox()
driver.get("https://ya.ru")

x = datetime.datetime.now()
print(x.strftime("%x"))

string = driver.find_element_by_css_selector("#text")
string.send_keys("hello " +x.strftime("%x"))
   