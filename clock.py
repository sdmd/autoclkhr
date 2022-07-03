import time
import schedule
import webclk
import random
import functools

usrid1= '****09'
usrpass1= '****123'

usrid2= '****09'
usrpass2= '****1234'

usrid3= '19****'
usrpass3= '123***'

inlist = ["08:01","08:02","08:03","08:00","08:04","08:05","08:07","08:09","08:00","08:10","08:01","08:00","08:00","08:13","08:06"]
outlist = ["19:01","19:02","19:03","19:00","19:04","19:05","19:07","19:09","19:20","19:30","19:01","19:00","19:10","20:00","20:09"]



while True:
    tin = random.choice(inlist)
    tout = random.choice(outlist)

    tin2 = random.choice(inlist)
    tout2 = random.choice(outlist)


    schedule.every().monday.at(tin).do(functools.partial(webclk.ckout,usrid1,usrpass1))
    schedule.every().tuesday.at(tin).do(functools.partial(webclk.ckout,usrid1,usrpass1))
    schedule.every().wednesday.at(tin).do(functools.partial(webclk.ckout,usrid1,usrpass1))
    schedule.every().thursday.at(tin).do(functools.partial(webclk.ckout,usrid1,usrpass1))
    schedule.every().friday.at(tin).do(functools.partial(webclk.ckout,usrid1,usrpass1))

    schedule.every().monday.at(tout).do(functools.partial(webclk.ckout,usrid1,usrpass1))
    schedule.every().tuesday.at(tout).do(functools.partial(webclk.ckout,usrid1,usrpass1))
    schedule.every().wednesday.at(tout).do(functools.partial(webclk.ckout,usrid1,usrpass1))
    schedule.every().thursday.at(tout).do(functools.partial(webclk.ckout,usrid1,usrpass1))
    schedule.every().friday.at(tout).do(functools.partial(webclk.ckout,usrid1,usrpass1))

    # USER 2

    schedule.every().monday.at(tin2).do(functools.partial(webclk.ckout,usrid2,usrpass2))
    schedule.every().tuesday.at(tin2).do(functools.partial(webclk.ckout,usrid2,usrpass2))
    schedule.every().wednesday.at(tin2).do(functools.partial(webclk.ckout,usrid2,usrpass2))
    schedule.every().thursday.at(tin2).do(functools.partial(webclk.ckout,usrid2,usrpass2))
    schedule.every().friday.at(tin2).do(functools.partial(webclk.ckout,usrid2,usrpass2))

    schedule.every().monday.at(tout2).do(functools.partial(webclk.ckout,usrid2,usrpass2))
    schedule.every().tuesday.at(tout2).do(functools.partial(webclk.ckout,usrid2,usrpass2))
    schedule.every().wednesday.at(tout2).do(functools.partial(webclk.ckout,usrid2,usrpass2))
    schedule.every().thursday.at(tout2).do(functools.partial(webclk.ckout,usrid2,usrpass2))
    schedule.every().friday.at(tout2).do(functools.partial(webclk.ckout,usrid2,usrpass2))






    while True:
        schedule.run_pending()
        if not schedule.jobs:
            break
        time.sleep(1)




    print("Clock Excecution")
    print('#####################################')
