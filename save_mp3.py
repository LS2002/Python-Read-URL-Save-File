#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import requests
import time
import urllib2
import shutil
import urlparse
import os
import re


def main():
    global isDev

    #create date folder
    folderName = time.strftime("%Y-%m-%d")
    if not os.path.exists(folderName): 
        os.makedirs(folderName)

    #iterate text_file_contains_mp3_url.txt
    with open('text_file_contains_mp3_url.txt') as file:
        for line in file:
            id,fileName,tag = line.split(',')
            print 'Saving',id,tag,fileName
            #assemble the mp3 url
            if isDev:
                url = 'http://path-to-dev.com/AudioMP3/?id=%s&Latest=Y' % (id)
            else:
                url = 'http://path-to-production.com/AudioMP3/?id=%s&Latest=Y' % (id)
            #save mp3 from url to file system
            download(url, folderName+'/'+fileName+".mp3")



def download(url, fileName):
    r = urllib2.urlopen(urllib2.Request(url))
    try:
        with open(fileName, 'wb') as f:
            shutil.copyfileobj(r,f)
    finally:
        r.close()

if __name__=="__main__":

    isDev = False
    main()
