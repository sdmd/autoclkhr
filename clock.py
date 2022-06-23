import time
import schedule
import webclk
import random



inlist = ["08:01","08:02","08:03","08:00","08:04","08:05","08:07","08:09","08:00","08:10","08:01","08:00","08:00","08:06"]
outlist = ["19:01","19:02","19:03","19:00","19:04","19:05","19:07","19:09","19:20","19:30","19:01","19:00","19:10","20:00"]

usrid1= '190809'
usrpass1= '*****123'

usrid2= '19****'
usrpass2= '123***'

usrid3= '19****'
usrpass3= '123***'

while True:
    tin = random.choice(inlist)
    tout = random.choice(outlist)

    schedule.every().monday.at(tin).do(webclk.clkin(usrid1,usrpass1))
    schedule.every().tuesday.at(tin).do(webclk.clkin(usrid1,usrpass1))
    schedule.every().wednesday.at(tin).do(webclk.clkin(usrid1,usrpass1))
    schedule.every().thursday.at(tin).do(webclk.clkin(usrid1,usrpass1))
    schedule.every().friday.at(tin).do(webclk.clkin(usrid1,usrpass1))

    schedule.every().monday.at(tout).do(webclk.clkout(usrid1,usrpass1))
    schedule.every().tuesday.at(tout).do(webclk.clkout(usrid1,usrpass1))
    schedule.every().wednesday.at(tout).do(webclk.clkout(usrid1,usrpass1))
    schedule.every().thursday.at(tout).do(webclk.clkout(usrid1,usrpass1))
    schedule.every().friday.at(tout).do(webclk.clkout(usrid1,usrpass1))


    while True:
        schedule.run_pending()
        if not schedule.jobs:
            break
        time.sleep(1)




    print("Clock Excecution")
    print('#####################################')
