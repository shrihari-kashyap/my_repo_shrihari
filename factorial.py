"""
This program tests the factorial application
"""
import time
import math
from selenium import webdriver


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://qainterview.pythonanywhere.com/")
text=driver.find_element_by_xpath("//input[@id='number']")
input_value= 12
text.send_keys(input_value)
driver.find_element_by_xpath("//button[@id='getFactorial']").click()
time.sleep(5)
result=driver.find_element_by_xpath("//p[@id='resultDiv']").text
print (result)
result=int(result.split()(-1))
print(result)
if(result==math.factorial(1)):
    print ("Fail")
else:
        print ("Pass")
