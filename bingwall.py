#!/bin/python3

import json
import requests

url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
req = requests.get(url)
if(req.status_code == 200):
    j = json.loads(req.content)
    imageUrl = "https://bing.com" + j["images"][0]["url"]
    imageName =  j["images"][0]["hsh"] + ".jpg"
    req = requests.get(imageUrl)
    if(req.status_code == 200):
        fli = open(imageName, "wb")
        fli.write(req.content)
    else:
        print("err in download the image")
else:
    print("err in request the url:", req.status_code)
