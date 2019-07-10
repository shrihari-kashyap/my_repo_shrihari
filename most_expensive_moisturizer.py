"""
To add the most expensive moisturizer to the cart
"""

#import webdriver from selenium
from selenium import webdriver
#import chrome webdriver
driver=webdriver.Chrome()
#maximize the window
driver.maximize_window()
#got to the moisturizer webpage
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

#check if the page is redirected properly
if(driver.find_element_by_xpath("//h2").text=="Moisturizers"):
    print("Sucessfully entered the moisturizers page")
else:
    print("Failed to enter the required page")

#find the xpath for the prices
price=driver.find_elements_by_xpath("//p[contains(text(),'Price')]")
#to fetch the max price from the new price
max_price=1
for k in range(6):
    new_price=int(price[k].text.split()[-1])
    if(new_price>max_price):
        max_price=new_price
#print the max price
print(max_price)
driver.find_element_by_xpath("(//p[contains(text(),'%d')])/following-sibling::button"%max_price).click()

print("The moisturizer added to the cart is",driver.find_element_by_xpath("(//p[contains(text(),'%d')])/preceding-sibling::p"%max_price).text)