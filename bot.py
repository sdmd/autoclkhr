import requests
from datetime import datetime, timedelta
import time
import pytz

BDT = pytz.timezone('Asia/Dhaka')

def today_date():
    tdate = datetime.now(BDT).strftime("%d-%m-%Y") #Current Date
    return tdate



def curr_time():
    ctime = (datetime.now().strftime("%H:%M:%S")) #Current time
    return ctime


tele_auth_token = "5295826579:AAHVm6nfkYH-npZHTK5nuPKO4mAB1YGAAsM"
tel_group_id = "-544287525"
#tel_group_id = "5276990520"

def send_msg_on_telegram(msg):
    telegram_api_url = "https://api.telegram.org/bot" + tele_auth_token + "/sendMessage?chat_id=" + tel_group_id + "&text=" + msg
    tel_resp = requests.get(telegram_api_url)

    if tel_resp.status_code == 200:
        print ("Notification has been sent on Telegram")
    else:
        print ("Could not send Message")


#send_msg_on_telegram("Today Date is " + today_date + " , Time is " + curr_time)


def textin(usrid):
    if usrid == '130709':
        nam = "Akhi Apu, ID: "
        print("CLOCK IN AKHI APU")
    elif usrid == '190809':
        nam = "SAYED, ID: "
        print("CLOCK IN SAYED")
    else:
        nam = "Other ID:"


    send_msg_on_telegram(nam + usrid + " CLOCK IN Done \nDATE: " + today_date() + " , Time: " + curr_time())
    print("CLOCK IN confirmed")


def textout(usrid):
    if usrid == '130709':
        nam = "Akhi Apu, ID: "
        print("CLOCK OUT AKHI APU")
    elif usrid == '190809':
        nam = "SAYED, ID: "
        print("CLOCK OUT SAYED")
    else:
        nam = "Other ID:"


    send_msg_on_telegram(nam + usrid + " CLOCK OUT Done \nDATE: " + today_date() + " , Time: " + curr_time())
    print("CLOCK OUT confirmed")



def clockerr(txt):
    send_msg_on_telegram(txt + "Error Occurred. ")
    print("Some thing is Wrong")



