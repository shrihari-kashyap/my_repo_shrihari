import time
from selenium import webdriver

#create object for webdriver
driver=webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
time.sleep(3)

#check if the heading of the page matches so that we can confirm we have landed on the right page
if(driver.find_element_by_xpath("//h2").text=="Sunscreens"):
    print("Successfully entered the sunscreen shopping site")
else:
    print("Failed to to enter the desired page.")
time.sleep(2)
#find all the elements on the page which contains 'SPF-50' in it
spf_50=driver.find_elements_by_xpath("//p[contains(text(),'SPF-50')]/following-sibling::p")

#assign an initial minimum price and iterate comparing the prices of all the elements to the minimum price and assign the new minimum price
min_value_spf50=10000
for each_element in spf_50:
        #split and extract the prices of item in integer format    
        price_spf50=int(each_element.text.split()[-1])
        if(price_spf50<min_value_spf50):
            min_value_spf50=price_spf50

#find and click the Add button corresponding to the minimum price
driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value_spf50).click()      
print("the sunscreen added to the cart is %s and its price is %d"%(driver.find_element_by_xpath("//p[contains(text(),'%d')]/preceding-sibling::p"%min_value_spf50).text,min_value_spf50))    

#find all the elements on the page which contains 'SPF-30' in it
spf_30=driver.find_elements_by_xpath("//p[contains(text(),'SPF-30')]/following-sibling::p")

#assign an initial minimum price and iterate comparing the prices of all the elements to the minimum price and assign the new minimum price
min_value_spf30=10000

for each_element in spf_30:
        #split and extract the prices of item in integer format
        price_spf30=int(each_element.text.split()[-1])
        if(price_spf30<min_value_spf30):
            min_value_spf30=price_spf30

#find and click the Add button corresponding to the minimum price
driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value_spf30).click()      
print("the sunscreen added to the cart is %s and its price is %d"%(driver.find_element_by_xpath("//p[contains(text(),'%d')]/preceding-sibling::p"%min_value_spf30).text,min_value_spf30))