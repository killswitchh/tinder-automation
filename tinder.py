from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

"""
TODO  :
1 . Open Tinder and login using Phone number[DONE]
2 . Wait till user enters OTP[NEEDS WORK - Using time.wait() for the meantime]
3 . Read Description of cards[TO BE DONE]
4 . segregate sentences and look for their presence in quote sites from internet[TO BE DONE]
"""




"""
-----------------XPATHS----------------
"""
#login button in popup window -
loginB='//*[@id="modal-manager"]/div/div/div[2]/div/div[3]/div[1]/button'
#Phonenumber text box -
EnterPhone='//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input'
#OTP continue button -
otpCont='//*[@id="modal-manager"]/div/div/div[2]/button'
#Phone Number continue button -
phoneCont='//*[@id="modal-manager"]/div/div/div[2]/button'
#Allow Location
allowLocationx= '//*[@id="content"]/span/div/div[2]/div/div/div[3]/button[1]'
#Disable Notification
disableNotificationsx= '//*[@id="content"]/span/div/div[2]/div/div/div[3]/button[2]'
#like button(right swipe) -
RSwipe='//*[@id="content"]/span/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[3]/span/svg'
#reject button(left swipe)-
LSwipe='//*[@id="content"]/span/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[1]/span/svg'

"""
---------------------------------------
"""

def login():
    userPhone=input("enter Phone number\n")
    url="https://tinder.com/app/recs"

    '''finding chrome driver'''
    options=Options()
    options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    driver=webdriver.Chrome(options= options ,executable_path=r"C:\Program Files (x86)\Google\chromedriver.exe",)

    '''opening page'''
    driver.get(url)
    print("url opened")
    #driver.maximize_window()
    #print("Window maximized")

    '''waiting for login page to popup'''
    driver.implicitly_wait(10) #<-not working as intended 
    loginp=driver.find_element_by_xpath(loginB)
    loginp.click()
    driver.implicitly_wait(4)

    '''Entering phone number '''
    Phonetextbox=driver.find_element_by_xpath(EnterPhone).send_keys(userPhone)
    continuePhone=driver.find_element_by_xpath(phoneCont)
    continuePhone.click()

    '''[NEEDS WORK] Waiting for user to enter OTP'''
    print("waiting for user to enter otp")
    #element=WebDriverWait(driver,30)
    #element.until(EC.presence_of_element_located((By.XPATH,otpCont)))
    #winddriver.implicitly_wait(30)
    time.sleep(15)
    continueOtp=driver.find_element_by_xpath(otpCont)
    continueOtp.click()

    ''' [NEEDS WORK] Clicking allow location and disable notification button '''
    #driver.implicitly_wait(10)
    time.sleep(3)
    allowLocation = driver.find_element_by_xpath(allowLocationx)
    allowLocation.click()
    #driver.implicitly_wait(10)
    time.sleep(2)
    disableNotifications=driver.find_element_by_xpath(disableNotificationsx)
    disableNotifications.click()
    print("login succesful")

login()
