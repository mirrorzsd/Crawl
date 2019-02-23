# -*- coding:utf-8 -*-
import requests
import base64
import re
import os


if __name__ =="__main__":

    downloadFile = "Download/"
    keyWord = "哆啦"
    #==============================
    URL = "http://www.migudm.cn/search/result/list.html?hintKey="
    URL = URL+str(base64.b64encode(keyWord.encode('utf-8')),'utf-8')+"&hintType=2&pageSize=30&pageNo=1"
    #print(URL)

    html = requests.get(URL).text
    #id = re.findall('"Position_ID":"1"}\' href="/comic/(.*?).html"', html, re.S)
    allID = re.findall('<div class="clItemLeft">(.*?)"Position_ID":.*?href="/comic/(.*?).html"(.*?)</a', html, re.S)#<a>
    if not allID:
        id = -1
        print("[+]Can't find keyword")
        pass#报错退出

    for item in allID:
        if len(re.findall('<s>(.*?)s>', str(item[2]), re.S))==0:
            id = item[1]
            break

    url = "http://www.migudm.cn/comic/"+str(id)+".html"
    #print(id)
    #print(url)

    #======================getChapNum===================
    page = requests.get(url).text
    #print(page)
    chapterNum = re.findall('<span class="num">更新至(.*?)话</span>', page, re.S)
    #<span class="num">更新至134话</span>
    if not chapterNum:
        print("[+]作品已下架")
        exit()#return 0
    chapterNum = int(chapterNum[0])
    print(chapterNum)
    #======================
    folderPath = downloadFile+keyWord
    if not os.path.isdir(folderPath):
        os.mkdir(folderPath)
    for i in range(1,chapterNum+1):
        #chapterUrl = "http://www.migudm.cn/"+str(id)+"/chapter/"+str(i)+".html"
        chapterUrl = "http://www.migudm.cn/opus/webQueryWatchOpusInfo.html?hwOpusId="+str(id)+"&index="+str(i)+"&opusType=2"
        print(chapterUrl)
        imgPage = requests.get(chapterUrl).content
        print(imgPage)
        imgUrls = re.findall('"url":"(.*?)"}', str(imgPage), re.S)
        print(imgUrls)
        if not imgUrls:
            continue#章节无图片，退出
        chapterPath = folderPath+"/"+str(i)
        if not os.path.isdir(chapterPath):
            os.mkdir(chapterPath)
        for index,imgUrl in enumerate(imgUrls):
            print(imgUrl)
            print(index)
            img = requests.get(imgUrl).content
            imgPath = folderPath+"/"+str(i)+"/"+ str(index) + ".jpg"
            print(imgPath)
            with open(imgPath,"wb") as f:
                f.write(img)
        print("[+]%d Done"%(i))
    print("[Done!]")


