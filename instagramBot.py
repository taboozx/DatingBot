from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
import sys

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class InstagramBot():
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver 
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        login_in = driver.find_element_by_name("username")
        login_in.clear()
        login_in.send_keys(self.username)
        pswd_in = driver.find_element_by_name("password")
        pswd_in.clear()
        pswd_in.send_keys(self.password)
        pswd_in.send_keys(Keys.RETURN)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1

username = 'taboozx@gmail.com'
password = '8Symbols'

alkemonka = InstagramBot(username, password)
alkemonka.login()

ig = InstagramBot(username, password)
ig.login()

hashtags = ['powderday', 'asia', 'adventure', 'travelling', 'fitness', 'snowboard',
            'jungle', 'cambodia', 'indonesia', 'thailand', 'fitnessgirls',  'hemp',
            'powder', 'snowboarding', 'snowboardgirls', 'followme', 'follow']

while True:
    try:
        # Choose a random tag from the list of tags
        tag = random.choice(hashtags)
        ig.like_photo(tag)
    except Exception:
        ig.closeBrowser()
        time.sleep(60)
        ig = InstagramBot(username, password)
        ig.login()