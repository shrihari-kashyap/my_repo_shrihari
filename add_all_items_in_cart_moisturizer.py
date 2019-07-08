"""
Program to add all the items in the Moisturizer page into the cart

"""
import time
from selenium import webdriver

#create object for webdriver
driver=webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
time.sleep(3)
#check if have landed on the correct page
if(driver.title=='The best moisturizers in the world!'):
    print("Successfully entered the Moisturizer shopping site")
else:
    print("Failed to to enter the desired page.")
time.sleep(2)

#Find and click the buttons to add the items into the cart
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/button").click()