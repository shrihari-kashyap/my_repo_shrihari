"""
To add the most expensive sunscreen to the cart
"""
#import webriver from selenium
from selenium import webdriver
#set the webdriver supoort for chrome
driver=webdriver.Chrome()
#set the webpage to redirected
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
#got to the sunscreens page
if (driver.find_element_by_xpath("//h2").text=="Sunscreens"):
    print("SUcessfully entered the sunscreens page")
else:
    print("Failed too enter the required page")
#find the xpath for the price
price=driver.find_elements_by_xpath("//p[contains(text(),'Price')]")
#to check for the max price from the new price 
max_price=1
for k in range(6):
    new_price=int(price[k].text.split()[-1])
    if(new_price>max_price):
        max_price=new_price
#print the max price
print(max_price)
driver.find_element_by_xpath("(//p[contains(text(),'%d')])/following-sibling::button"%max_price).click()
print("The sunscreens added to the cart is",driver.find_element_by_xpath("(//p[contains(text(),'%d')])/preceding-sibling::p"%max_price).text)