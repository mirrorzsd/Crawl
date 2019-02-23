# -*- coding:utf-8 -*-
#Author:Mirror
#CreateDate:18.10.20
#ModfiedDate:18.10.23

import requests
import re
import urllib

def get_baidu_pic(keyWord,number=100):
    URL ="http://image.baidu.com/search/flip?tn=baiduimage"
    pageNum = int(number/60)+1
    #print(pageNum)
    count = 1
    for page in range(pageNum+1):
        #URL = "http://image.baidu.com/search/flip?tn=baiduimage&pn=120&word="
        URL = URL + "&pn=" + str(page*60)+"&word="+urllib.parse.quote(keyWord, safe='/')
        #print("[+]"+str(URL))
        html = requests.get(URL).text
        urls = re.findall('"objURL":"(.*?)",', html, re.S)
        #print(urls)
        #print(len(urls))
        for url in urls:
            # url = url.replace("\\","")
            #print(url)
            if count == number+1:break
            try:
                pic = requests.get(url,timeout=30)
                string = "pictures/" + str(count) + '.jpg'
                with open(string, "wb") as f:
                    f.write(pic.content)
                    print("[%d%%]下载第%d张图片：%s" % (int(count*100/number),count, str(url)))
                    count += 1
            except Exception as e:
                print('[%d%%]下载第%d张图片时失败: %s' % (int(count*100/number),count, str(url)))
                print(e)
                continue


if __name__ == "__main__":
    get_baidu_pic("刘雯", number=100)