import time
#from selenium import webdriver
from selenium import webdriver
#get the chrome driver
driver=webdriver.Chrome()
#go to the moisturizer link
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
#find the xpath for both almond and aloe
aloe=driver.find_elements_by_xpath("//p[contains(text(),'Aloe')]/following-sibling::p")
almond=driver.find_elements_by_xpath("//p[contains(text(),'Almond')]/following-sibling::p")
least_moisturizer=[almond,aloe]
#find the least expensive item from aloe and almond
min_value=10000
for moist in least_moisturizer:
    for each_element in moist:    
        price_moisturizer=int(each_element.text.split()[-1])
        if(price_moisturizer<min_value):
            min_value=price_moisturizer
    #select the item by clicking the add button
    driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value).click()
    time.sleep(2)
    #print the name of the product and price of aloe and almond
    print("the moisturizer added to the cart is %s and its price is %d"%(driver.find_element_by_xpath("//p[contains(text(),'%d')]/preceding-sibling::p"%min_value).text,min_value))    
    time.sleep(3)
