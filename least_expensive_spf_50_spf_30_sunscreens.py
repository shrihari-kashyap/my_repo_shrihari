"""
To find the least expensive sunscreen
"""
import time
#from selenium import webdriver
from selenium import webdriver
#get the webdriver set to chrome
driver=webdriver.Chrome()
#get the website from the driver
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
#check for the condition to select spf-50 and spf-30 items
spf_50=driver.find_elements_by_xpath("//p[contains(text(),'SPF-50')]/following-sibling::p")
spf_30=driver.find_elements_by_xpath("//p[contains(text(),'SPF-30')]/following-sibling::p")
least_sunscreen=[spf_50,spf_30]
#find the least expensive item from spf-50 and spf-30

for sun in least_sunscreen:
    min_value=10000
    for each_element in sun:    
        price_sunscreen=int(each_element.text.split()[-1])
        if(price_sunscreen<min_value):
            min_value=price_sunscreen
    #select the item by clicking the add button
    driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value).click()
    time.sleep(2)
    #Print the least expensive spf-50 and spf-30 items
    print("the sunscreen added to the cart is %s and its price is %d"%(driver.find_element_by_xpath("//p[contains(text(),'%d')]/preceding-sibling::p"%min_value).text,min_value))    
    time.sleep(3)