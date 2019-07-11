import time
from selenium import webdriver

#create object for webdriver
driver=webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
time.sleep(3)

#check if the heading of the page matches so that we can confirm we have landed on the right page
if(driver.find_element_by_xpath("//h2").text=="Moisturizers"):
    print("Successfully entered the Moisturizers shopping site")
else:
    print("Failed to to enter the desired page.")
time.sleep(2)
#find all the elements on the page which contains 'SPF-50' in it
aloe=driver.find_elements_by_xpath("//p[contains(text(),'Aloe')]/following-sibling::p")

#assign an initial minimum price and iterate comparing the prices of all the elements to the minimum price and assign the new minimum price
min_value_aloe=10000
for each_element in aloe:
        #split and extract the prices of item in integer format    
        price_aloe=int(each_element.text.split()[-1])
        if(price_aloe<min_value_aloe):
            min_value_aloe=price_aloe

#find and click the Add button corresponding to the minimum price
driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value_aloe).click()      
print("the sunscreen added to the cart is %s and its price is %d"%(driver.find_element_by_xpath("//p[contains(text(),'%d')]/preceding-sibling::p"%min_value_aloe).text,min_value_aloe))    

#find all the elements on the page which contains 'SPF-30' in it
almond=driver.find_elements_by_xpath("//p[contains(text(),'Almond')]/following-sibling::p")

#assign an initial minimum price and iterate comparing the prices of all the elements to the minimum price and assign the new minimum price
min_value_almond=10000

for each_element in almond:
        #split and extract the prices of item in integer format
        price_almond=int(each_element.text.split()[-1])
        if(price_almond<min_value_almond):
            min_value_almond=price_almond

#find and click the Add button corresponding to the minimum price
driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value_almond).click()      
print("the sunscreen added to the cart is %s and its price is %d"%(driver.find_element_by_xpath("//p[contains(text(),'%d')]/preceding-sibling::p"%min_value_almond).text,min_value_almond))