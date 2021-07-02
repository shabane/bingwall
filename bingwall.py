#!/bin/python3

import logging
import json
import requests
import datetime

date = datetime.datetime.now()
logging.basicConfig(filename='/var/log/bingwall.log', encoding='utf-8', level=logging.DEBUG)

def main():
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    print("Sending request")
    logging.debug('----------------' + str(date) + '----------------')
    req = requests.get(url)
    if(req.status_code == 200):
        print("Request sent succes")
        j = json.loads(req.content)
        imageUrl = "https://bing.com" + j["images"][0]["url"]
        imageName =  j["images"][0]["hsh"] + ".jpg"
        req = requests.get(imageUrl)
        print("Downloading . . .")
        logging.debug('starting to download')
        if(req.status_code == 200):
            fli = open("/home/loading/Pictures/"+imageName, "wb")
            fli.write(req.content)
            print("image saved at %s" %(imageName))
            logging.debug(f'image saved at {imageName}')
        else:
            print("err in download image or saveing")
            logging.error('fail to download')
            main()
    else:
        print("err in request the url:", req.status_code)
        logging.error('fail to connect to bing.com')
        main()

main()
