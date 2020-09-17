#!/usr/bin/python3
# BingWall Is A Simple Script To Download Daily WallPaper Of www.bing.com (Base On Date Of The Day)
# I Hope Have Fun And Beauty Backgroud :)
# Please Visit My GitHub At https://github.com/shabane

import requests
import datetime
import time
from pathlib import Path
import pathlib
import os

YMD_Now = "!"
global YMD_LastDay 
YMD_LastDay = ""


def Idown():
    
    usrhome =str(Path.home())

    x = datetime.datetime.now()
    
    Date = str(x.year)+"/"+str(x.month)+"/"+str(x.day)+" "+str(x.hour)+":"+str(x.minute)+":"+str(x.second)

    JsonUrl = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

    res = requests.get(JsonUrl) 

    tmp = res.json()

    tmp2 = tmp['images'] 

    tmp3 = tmp2[0]

    name = tmp3['hsh']

    url = "https://www.bing.com/"+tmp3['url']

    r = requests.get(url)
    print("file download")
    os.mkdir(usrhome+"/Downloads/bingwall/")
    print("dir maked")
    with open(usrhome+"/Downloads/bingwall/"+name+".jpg", 'wb') as f:
        f.write(r.content)
        print("file saved")
    # Save Download Log To Main Directory  
    file = open("/var/log/bingwall/"+"bingwall.log","a")
    file.write("---------------------------------------- New WallPaper Downloaded ----------------------------------------"+"\n")
    file.write("Date        > "+Date+"\n")
    file.write("Url         > https://www.bing.com/"+tmp3['url']+"\n")
    file.write("Copyright   > "+tmp3['copyright']+"\n")
    file.write("Hash/Name   > "+name+"\n")
    file.close()
    
    global YMD_LastDay
    YMD_LastDay = str(x.year)+"/"+str(x.month)+"/"+str(x.day)

while(True):
    NDate = datetime.datetime.now()
    YMD_Now = str(NDate.year)+"/"+str(NDate.month)+"/"+str(NDate.day)
    if(YMD_Now != YMD_LastDay):
        time.sleep(60)
        try:
            Idown()
        except:
            # Save Faild Log
            print("Some Fucking Thing Wrong ! Shit")
            file = open("/var/log/bingwall/"+"bingwall.log","a")
            file.write("------------------- Fail To Download WallPaper _ Auto ReTry At 11 Minute -------------------"+"\n")
            file.write("Date        > "+YMD_Now+" "+str(NDate.hour)+":"+str(NDate.minute)+":"+str(NDate.second)+"\n")
            file.close()
    time.sleep(600)
