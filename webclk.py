from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import bot
import os
import schedule
print("Starting")

usrid1= '****09'
usrpass1= '****123'

usrid2= '****09'
usrpass2= '****1234'

usrid3= '19****'
usrpass3= '123***'


def  load_driver():
        chrome_op=webdriver.ChromeOptions()
#        chrome_op.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
#        chrome_op.add_argument("--headless")
#        chrome_op.add_argument("--disable-dev-shm-usage")
#        chrome_op.add_argument("--no-sandbox")
#        chrome_driver=webdriver.Chrome(options=chrome_op)
#        chrome_driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_op)

        chrome_op.add_argument("--disable-dev-shm-usage")
        chrome_op.add_argument("--no-sandbox")
        chrome_driver = webdriver.Chrome(options=chrome_op)

        return chrome_driver


def clkout():
        ckout(usrid1, usrpass1)
        print("CLOCK OUT SAYED")
        #ckout(usrid2, usrpass2)
        #print("CLOCK OUT AKHI APU")





def clkin():
        ckin(usrid1, usrpass1)
        print("CLOCK IN SAYED")
        #ckin(usrid2, usrpass2)
        #print("CLOCK IN AKHI APU")




def ckin(usrid,usrpass):
        driver = load_driver()
        try:
                driver.get("https://ulkasemi.peopleshr.com/hr/security/login?ReturnUrl=%2fhr%2fhome%2findex")
                print(driver.title)
                time.sleep(5)
                driver.find_element(By.ID,'txtusername').send_keys(usrid)
                print('userid done!')
                driver.find_element(By.ID,'txtpassword').send_keys(usrpass)
                print('password done!')
                driver.find_element(By.ID,'btnsubmit').click()
                print('Authentication')
                print('You are logged in!')
                print('Sleeping for 40 sec!')
                time.sleep(40)
                print(driver.title)
                print('Clock IN! in process')
                driver.find_element(By.XPATH,'//*[@id="ManualSwipeWidget"]/div[4]/div[2]/a/i').click()
                time.sleep(5)

                print('Clock IN! Done')
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ")
                bot.textin(usrid)
                print('Browser closed!')
                print("****************************************")
                driver.quit()
                return schedule.CancelJob
        except Exception as e:
                print("An exception occurred")
                # Telegram text
                bot.clockerr("Clock IN ")
                print("*********************----------------------*******************")
                print(e)





def ckout(usrid,usrpass):
        driver = load_driver()
        try:
                driver.get("https://ulkasemi.peopleshr.com/hr/security/login?ReturnUrl=%2fhr%2fhome%2findex")
                print(driver.title)
                time.sleep(5)
                driver.find_element(By.ID,'txtusername').send_keys(usrid)
                print('userid done!')
                driver.find_element(By.ID,'txtpassword').send_keys(usrpass)
                print('password done!')
                driver.find_element(By.ID,'btnsubmit').click()
                print('Authentication')
                print('You are logged in!')
                print('Sleeping for 40 sec!')
                time.sleep(40)
                print(driver.title)
                print('Clock OUT! in process')
                driver.find_element(By.XPATH,'//*[@id="ManualSwipeWidget"]/div[4]/div[2]/a/i').click()
                time.sleep(5)

                print('Clock OUT! Done')
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ")
                bot.textout(usrid)
                print('Browser closed!')
                print("****************************************")
                driver.quit()
                return schedule.CancelJob
        except Exception as e:
                print("An exception occurred")
                # Telegram text
                bot.clockerr("Clock OUT ")
                print("*********************----------------------*******************")
                print(e)
