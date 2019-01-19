from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import datetime


#run firefox
driver = webdriver.Firefox()
driver.get("https://badoo.com/signin/")
driver.implicitly_wait(1)

#auth data
f = open("C:/Users/Tbz/Desktop/DatingBot/adata", "r")
badoologin = (f.readline())
badoopass = (f.readline())
bloggerlogin = (f.readline())
bloggerpass = (f.readline())


#make login
input_field = driver.find_element_by_name('email')
input_field.send_keys(badoologin)
driver.implicitly_wait(1)

input_field = driver.find_element_by_name('password')        
input_field.send_keys(badoopass)

driver.find_element_by_name("post").click()

#define variables
myselfcount = 0
msg = 0
likes = 0
myself = []
file = open("C:/Users/Tbz/Desktop/badoo_myself.txt", "a")

#--------------------------------------------------------------------
#start loop for define amount of profiles
for i in range(50):
    x = str(i)
    print("loop "+x) 

#if there any pop up type cancel
    try:
        driver.find_element_by_xpath("/html/body/aside/section/div[1]/div/div[2]/div/div[2]").click()
    except NoSuchElementException:
        print ("No Propustit4")

    try:
        driver.find_element_by_xpath("/html/body/aside/section/div[1]/div/div[3]/div[2]/span").click()
    except NoSuchElementException:
        print ("No seen by milliones")

#if someone like me, send a message
    try:
        input_field = driver.find_element_by_xpath("/html/body/aside/section/div[1]/div/div[1]/div[3]/form/div/div/div/div[1]/div/input")
        input_field.send_keys('Здрям! Давай дружить')
        driver.find_element_by_xpath("/html/body/aside/section/div[1]/div/div[1]/div[3]/form/div/div/div/div[2]/div").click()
        print ("msg sended")
        msg += 1
        time.sleep(2) #pause 1 second
    except NoSuchElementException:
        print("No vzaimno - Propustit")

#collecting info about myself
    try:
        myself.append(driver.find_element_by_css_selector("#mm_cc > div.encounters-card__inner > div > div > div.scroll__inner > div > div.encounters-card__sidebar-scroll.js-scroller > div.encounters-card__info > div.encounters-card__section.js-profile-about-me-container.js-core-events-container > div").text)
        myselfcount += 1
    except NoSuchElementException:
        print("No about myself")

#send like
    try:
        like=driver.find_element_by_css_selector(".profile-action--yes")
        driver.implicitly_wait(2)
        like.click()
        likes += 1
    except NoSuchElementException:
        print("No yes going to propustit")

#--------------------------------------------------------------------

#get info about my self from array and copy it to the file
for i in range(myselfcount):
    if len(myself[i]) > 30:
        file.write(myself[i]+"\n\n")  
   
    
boofer = '\n\n\n'.join(str(e) for e in myself)    
print(boofer)

#get script running statistics
file.close()

                    

myselfcount = str(myselfcount)  
likes = str(likes)
msg = str(msg)
print('\n')
print("-----------------------------------------------------------")
print("totally "+likes+" likes and "+msg+" messages was send and "+myselfcount+" myselfcount")


driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.blogger.com%2Fhome&ltmpl=blogger&service=blogger&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

#login into Blogger account
login = driver.find_element_by_css_selector('#identifierId')
login.send_keys(bloggerlogin)
driver.find_element_by_css_selector('#identifierNext > content:nth-child(3) > span:nth-child(1)').click()
time.sleep(1)

pswd=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input')
pswd.send_keys(bloggerpass)
driver.find_element_by_css_selector('#passwordNext > content:nth-child(3) > span:nth-child(1)').click()


#choose correct blog
driver.find_element_by_css_selector('a.blogg-button').click()

x = datetime.datetime.now()
time.sleep(3)

title = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/form/div[1]/input')
title.send_keys('Girl about them selfs in Moscow Region '+x.strftime("%x"))

title = driver.find_element_by_css_selector('#postingComposeBox')
title.send_keys("", boofer)

#--send--
#driver.find_element_by_css_selector('button.blogg-primary:nth-child(2)').click

#--save--
driver.find_element_by_css_selector('.K3JSBVB-Q-s').click
#driver.quit()