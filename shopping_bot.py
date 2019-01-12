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

def image_to_string(src):
	img = cv2.imread(src,0)
	    # Convert to gray
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    # Apply dilation and erosion to remove some noise
	kernel = np.ones((1, 1), np.uint8)
	img = cv2.dilate(img, kernel, iterations=1)
	img = cv2.erode(img, kernel, iterations=1)

	    # Write image after removed noise
	cv2.imwrite("removed_noise.png", img)

	    #  Apply threshold to get image with only black and white
	img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

	    # Write the image after apply opencv to do some ...
	cv2.imwrite("thres.png", img)

	    # Recognize text with tesseract for python
	result = pytesseract.image_to_string(Image.open("thres.png"))
	Image.close()
	return result



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



while(1): #download captcha
	try:
		img = browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[1]/div[4]/div/div/div[1]/div/label[5]/div[2]/div/div/div/form/div/div[1]/img[1]')
		src = img.get_attribute('src')
		break
	except:
		print ("Retrying !!!")
result=""
while(1):
	try:
		result=image_to_string(src);
		break;
	except:
		print("Retrying!!!")

while(1):
	try:
		search=browser.find_element_by_xpath(''' //*[@id="container"]/div/div[1]/div/div[1]/div[4]/div/div/div[1]/div/label[5]/div[2]/div/div/div/form/div/div[2]/div/input ''')
			#write text in it
		search.send_keys(result)
		break
	except:
		print ("Retrying !!!")

input("press enter to close window")
browser.close()
