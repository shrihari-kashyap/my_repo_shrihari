"""
Program to check weater to buy sunscreen or moisturizer
"""
#import webdriver from the selenium
from selenium import webdriver
#create an object web driver
driver=webdriver.Chrome()   
#to maximize the browser window
driver.maximize_window()
#fetch the url
def stmt_print(heading_path):
    if (heading_path=='Sunscreens' and temperature>=34):
        print("Sunscreens")
    elif(heading_path=='Moisturizers' and temperature<=19):
        print("Moisturizers")
    else:
        print("Failed to load the page")
        
driver.get("https://weathershopper.pythonanywhere.com")
# used to fetch the temperature
temperature=driver.find_element_by_xpath("//span[@id='temperature']").text.encode("utf-8")
#convert string values to integer values
temperature=int(temperature.split()[0])
#print temp values
print(temperature)

#use if else condition to redirct the required page
if temperature<=19:
    #click for the moisturizers page
    driver.find_element_by_xpath("//button[text()='Buy moisturizers']").click()
    heading_path=driver.find_element_by_xpath("//h2").text
    #display the comment
    print("Entered moisturizers page")
    stmt_print(heading_path)
else:
    #click for sunscreens page
    driver.find_element_by_xpath("//button[text()='Buy sunscreens']").click()
    heading_path=driver.find_element_by_xpath("//h2").text
    #display the comment page
    print("Entered sunscreen page")
    stmt_print(heading_path)
#close the driver
driver.close()