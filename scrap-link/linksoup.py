#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Aug 23, 2018

Source:

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Firefox()



# Google Chrome 
browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

browser.get('http://www.google.com')


time.sleep(2) # sleep for 5 seconds so you can see the results

browser.get("https://www.idiotinside.com/2014/10/19/top-30-python-projects-in-github/")

elements2 = browser.find_elements_by_css_selector('div.panel h5 a')
#print(elements2.text)
time.sleep(5)
link = []

for element2 in elements2:
    #print(element.get_attribute("data-href"))
    
    # ignore the 
    time.sleep(5)
    time.sleep(5)
    #link.append(element2.get_attribute("href"))
    #print(link)
    
    print(element2.get_attribute("href"))


browser.quit()


