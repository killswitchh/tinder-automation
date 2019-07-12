from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

"""
TODO
1 . Open Tinder and login using Phone number[DONE]
2 . Wait till user enters OTP[DONE]
3 . Ability to like / unlike cards[DONE]
4 . Read Description of cards[TO BE DONE]
5 . segregate sentences and look for their presence in quote sites from internet[TO BE DONE]
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
RSwipe='//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]'
#reject button(left swipe)-
LSwipe='//*[@id="content"]/span/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[1]/span/svg'
#information button to view description
Info='//*[@id="content"]/span/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[6]/div[2]/svg'
#not now button for homescreen
Nhome='//*[@id="modal-manager"]/div/div/div[3]/button[2]'
#div for description
Desc='//*[@id="content"]/span/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div'
"""
---------------------------------------
"""

def runSelenium():
    global url
    global options
    global driver
    global userPhone
    userPhone=input("enter Phone number\n")
    url="https://tinder.com/app/recs"
    '''finding chrome driver'''
    options=Options()
    options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    driver=webdriver.Chrome(options= options ,executable_path=r"C:\Program Files (x86)\Google\chromedriver.exe",)
    
def login():
    
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

    '''Waiting for user to enter OTP'''
    print("WAITING FOR OTP")
    classNameChange="Bg($c-gray)" #class name does not have this string when otp is entered
    while True:
        time.sleep(2)
        continueOtp=driver.find_element_by_xpath(otpCont)
        cname=continueOtp.get_attribute("class")
        #print(cname)
        if classNameChange not in cname:
            print("OTP ENTERED")
            break
        else:
            print(".",end="",sep="")
    continueOtp.click()

    ''' [NEEDS WORK] Clicking allow location and disable notification button '''
    #driver.implicitly_wait(10)
    time.sleep(2)
    allowLocation = driver.find_element_by_xpath(allowLocationx)
    allowLocation.click()
    print("Allow Location clicked")
    #driver.implicitly_wait(10)
    time.sleep(1)
    disableNotifications=driver.find_element_by_xpath(disableNotificationsx)
    disableNotifications.click()
    print("Disable Notifications clicked")
    print("login succesful")

    
def unlimitedLikes():
    time.sleep(5)#for the tutorial animation to play out
    print("Number of pictures liked=")
    count=0
    '''Presses the like button once , every second'''
    while(True):
        if(count==6):
            time.sleep(2)
            notNow=driver.find_element_by_xpath(Nhome)
            notNow.click()
        like=driver.find_element_by_xpath(RSwipe)
        like.click()
        count=count+1
        time.sleep(1)
        
        print(count)

        
runSelenium()
login()
unlimitedLikes()
