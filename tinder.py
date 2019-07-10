from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

"""
XPATHS

like button(right swipe) - //*[@id="content"]/span/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[3]/span/svg
reject button(left swipe)- //*[@id="content"]/span/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[1]/span/svg
to be identified - '//*[@id="content"]/span/div/div[1]/div/aside/nav/div/div/div/div[1]/div/div[2]'))
"""

userPhone=input("enter Phone number")
url="https://tinder.com/app/recs"
#url="https://www.facebook.com/"
options=Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver=webdriver.Chrome(options= options ,executable_path=r"C:\Program Files (x86)\Google\chromedriver.exe",)
driver.get(url)
print("url opened")
#driver.maximize_window()
#print("Window maximized")


driver.implicitly_wait(10)

loginp=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div/div[3]/div[1]/button')
loginp.click()
driver.implicitly_wait(4)
Phonetextbox=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input').send_keys(userPhone)
#login=driver.find_element_by_class_name('My.(10px).My(16px)--m')

continueButton=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
continueButton.click()
cont='//*[@id="modal-manager"]/div/div/div[2]/button'
print("waiting for user to enter otp")
element=WebDriverWait(driver,30)
element.until(EC.presence_of_element_located((By.xpath,cont)))
#driver.implicitly_wait(30)
continue2=driver.find_element_by_xpath(cont)
continue2.click()
