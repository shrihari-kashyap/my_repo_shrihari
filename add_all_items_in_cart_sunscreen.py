"""
Program to add all the items in the sunscreen page into the cart
"""
import time
from selenium import webdriver

#create object for webdriver
driver=webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
time.sleep(3)
#check if have landed on the correct page
if(driver.title=='The best moisturizers in the world!'):
    print("Successfully entered the sunscreen shopping site")
else:
    print("Failed to to enter the desired page.")
time.sleep(2)

#find the location of the cart
cart_before=driver.find_element_by_xpath("//BUTTON[@onclick='goToCart()']").text

#extract the quantity of items in the cart
cart_before_split=cart_before.split()[-1]
print(cart_before_split)

#Find and click the buttons to add the items into the cart
for i in range(1,7):
    	driver.find_element_by_xpath("(//BUTTON[contains(@class,'btn btn-primary')][text()='Add'])[%d]"%i).click()
	

#find the location of the cart after adding items
cart_after=driver.find_element_by_xpath("//BUTTON[@onclick='goToCart()']").text
print(cart_after)
#extract the quantity of items in the cart
cart_after_split=cart_after.split()[2]
print(cart_after_split)

#check if the cart before matches with cart after adding item
if(cart_after_split==cart_before_split):
    print("Failed to add items into the cart")

final_items=int(cart_after_split)

#check if all items are correctly added to the cart
if(final_items<6):
    print("Some of items not added to the cart")

#check if extra items are added to the cart
if(final_items>6):
    print("Additional items added to the cart")

#check if all the items added are successfully reflects in the cart
if(final_items==6):
    print("Successfully added items into the cart")