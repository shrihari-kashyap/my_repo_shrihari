"""
To verify the items in the cart and sum of the items
"""
import time
#import webdriver from selenium
from selenium import webdriver
#import chrome webdriver
driver=webdriver.Chrome()
#go to the moisturizer link
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

#find the xpath for both almond and aloe
aloe=driver.find_elements_by_xpath("//p[contains(text(),'Aloe')]/following-sibling::p")
almond=driver.find_elements_by_xpath("//p[contains(text(),'Almond')]/following-sibling::p")
least_moisturizer=[almond,aloe]
#find the least expensive item from aloe and almond
sum=0
list_moist=[]
for moist in least_moisturizer:
    min_value=10000
    for each_element in moist:    
        price_moisturizer=int(each_element.text.split()[-1])
        if(price_moisturizer<min_value):
            min_value=price_moisturizer
    list_moist.append(driver.find_element_by_xpath("//p[contains(text(),'%d')]/preceding-sibling::p"%min_value).text)
    sum=sum+min_value
    #select the item by clicking the add button
    driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value).click()
    time.sleep(2)
    #print the name of the product and price of aloe and almond
    print("the moisturizer added to the cart is %s and its price is %d"%(driver.find_element_by_xpath("//p[contains(text(),'%d')]/preceding-sibling::p"%min_value).text,min_value))    
    time.sleep(2)
print(list_moist)
#click on the cart button
driver.find_element_by_xpath("//button[@class='thin-text nav-link']").click()
time.sleep(3)
#compare the name and sum of the items
print(sum)
list_name=[]
table1=driver.find_elements_by_xpath("//td[1]")
for each_element in table1:
    list_name.append(each_element.text)
#check whether the list of items matches
print(list_name)
if (list_moist==list_name):
    print("list matching")
else:
    print("list is not matching")    
#check whether sum matches the total
sum_total=(driver.find_element_by_xpath("//p[@id='total']").text)
sum_total=int(sum_total.split()[-1])
print("Total price of the cart",sum_total)
if (sum_total==sum):
    print("Sum matches")
else:
    print("sun does not match")
#click to go to payment page    
driver.find_element_by_xpath("//span[contains(text(),'Pay with Card')]").click()