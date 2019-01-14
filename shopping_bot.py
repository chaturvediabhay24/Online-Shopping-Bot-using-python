import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import urllib.request
import os
import cv2
import numpy as np
import pytesseract
from PIL import Image
import getpass

usrname=input("enter username: ")
passwrd=getpass.getpass() 

browser=webdriver.Chrome()                            
browser.get("https://www.flipkart.com")                  #opening website

browser.maximize_window()                                #maximize window

while(1):
	try:
		search=browser.find_element_by_xpath("//*[@class='_2AkmmA _29YdH8']").click()          #exit the login window
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		search=browser.find_element_by_xpath("//*[@type='text']")     #writing text in search box
		search.send_keys('Redmi Note 6 Pro (Black, 64 GB)')
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("Retrying writing text in search box !!!")

while(1):
	try:
		link = browser.find_element_by_xpath("//*[@id='container']/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/a[2]")
		browser.get(link.get_attribute('href'))
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		browser.find_element_by_xpath("//*[@id='container']/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		browser.find_element_by_xpath('''//*[@id="container"]/div/div[1]/div/div[1]/div/div[3]/form/button''').click()
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		search=browser.find_element_by_xpath(''' //*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[1]/input ''')            #write text in it
		search.send_keys(usrname)
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		search=browser.find_element_by_xpath('''//*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[2]/input''')
		search.send_keys(passwrd)
		search.send_keys(Keys.RETURN)
		break
	except:
		print ("wrong password !!!")
while(1):
	try:
		browser.find_element_by_xpath('''//*[@id="CNTCTF85C72FB627F41D6BFAEAE05F"]/button''').click()
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		browser.find_element_by_xpath(''' //*[@id="to-payment"]/button ''').click()
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		elm=browser.find_element_by_tag_name('html')
		elm.send_keys(Keys.END)
		break
	except:
		print ("Retrying !!!")

while(1):
	try:
		browser.find_element_by_xpath(''' //*[@id="container"]/div/div[1]/div/div[1]/div[4]/div/div/div[1]/div/label[5] ''').click()
		break
	except:
		print ("Retrying !!!")


input("press enter to close window")
browser.close()
