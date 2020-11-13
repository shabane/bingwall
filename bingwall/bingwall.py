#!/usr/bin/python3
# BingWall Is A Simple Script To Download Daily WallPaper Of www.bing.com
# I Hope Have Fun And Beauty Backgroud :)
# Please Visit My GitHub At https://github.com/shabane

import requests
import datetime
from pathlib import Path
import pathlib
import os

def Idown():
    
    x = datetime.datetime.now()
    
    login = os.path.expanduser('~')

    Date = str(x.year)+"/"+str(x.month)+"/"+str(x.day)+" "+str(x.hour)+":"+str(x.minute)+":"+str(x.second)

    JsonUrl = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

    res = requests.get(JsonUrl) 

    tmp = res.json()

    tmp2 = tmp['images'] 

    tmp3 = tmp2[0]

    name = tmp3['hsh']

    url = "https://www.bing.com/"+tmp3['url']

    r = requests.get(url)
    
    with open(login+"/Pictures/"+name+".jpg", 'wb') as f:
        f.write(r.content)

    # Save Download Log 
    file = open(login+"/Pictures/"+"bingwall.log","a")
    file.write("_________New WallPaper Downloaded"+"\n")
    file.write("Date        > "+Date+"\n")
    file.write("Url         > https://www.bing.com/"+tmp3['url']+"\n")
    file.write("Copyright   > "+tmp3['copyright']+"\n")
    file.write("Hash/Name   > "+name+"\n")
    file.close()



try: 
    Idown()
except Exception as e: # Save Faild Log
    login = os.path.expanduser('~')
    x = datetime.datetime.now()

    file = open(login+"/Pictures/"+"bingwall.log","a")
    file.write("Err______Faild To Download"+"\n")
    file.write("Date        > "+str(x.year)+"/"+str(x.month)+"/"+str(x.day)+" "+str(x.hour)+":"+str(x.minute)+":"+str(x.second)+"\n")
    file.write("Message     > "+e)


    