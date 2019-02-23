# -*- coding:utf-8 -*-
#Author: Mirror
#CreateDate: 18.10.20
#ModifiedDate:18.10.22

import sys
import requests
import urllib
import re
import os
from testDialog import *
from PyQt5 import QtCore, QtGui, QtWidgets
import tencent as tc
import argparse
import base64
import json
import threading
from time import sleep
from lxml import html



class Ui(Ui_Form):
    def __init__(self):
        print("init")
        self.platform = "baidu"
        self.targetNum = 10
        self.keyWord = "皮卡丘"
        self.downloadFile = "Download/"
        self.getCount = 0

    def targetBaidu(self):
        self.platform = "baidu"
        self.textTarget.setText(self.platform)
        self.BaiduButt.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.MiguButt.setStyleSheet("background-color: rgb(230,230,230);")
        self.TencentButt.setStyleSheet("background-color: rgb(230,230,230);")

    def targetMigu(self):
        self.platform = "migu"
        self.textTarget.setText(self.platform)
        self.BaiduButt.setStyleSheet("background-color: rgb(230,230,230);")
        self.MiguButt.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.TencentButt.setStyleSheet("background-color: rgb(230,230,230);")

    def targetTencent(self):
        self.platform = "tencent"
        self.textTarget.setText(self.platform)
        self.BaiduButt.setStyleSheet("background-color: rgb(230,230,230);")
        self.MiguButt.setStyleSheet("background-color: rgb(230,230,230);")
        self.TencentButt.setStyleSheet("background-color: rgb(191, 191, 191);")

    def search(self):
        self.keyWord = self.keywordEdit.text()
        self.textGet.setText(str(self.keyWord))
        self.targetNum = self.picNumEdit.text()
        if not self.targetNum:
            self.targetNum=0
        else:
            self.targetNum = int(self.targetNum)


        #===============搜索的函数=====================
        if self.platform =="baidu":
            self.get_baidu_pic(self.keyWord, number=self.targetNum)
        if self.platform =="tencent":
            self.get_tencent_pic(self.keyWord)
        if self.platform =="migu":
            self.get_migu_pic()
        #==============================================

    def get_baidu_pic(self,keyWord, number=100):
        URL = "http://image.baidu.com/search/flip?tn=baiduimage"
        pageNum = int(number / 60) + 1
        #print(pageNum)
        count = 1
        imgPath = self.downloadFile+"/"+keyWord
        if not os.path.isdir(imgPath):
            os.makedirs(imgPath)
        for page in range(pageNum + 1):
            # URL = "http://image.baidu.com/search/flip?tn=baiduimage&pn=120&word="
            URL = URL + "&pn=" + str(page * 60) + "&word=" + urllib.parse.quote(keyWord, safe='/')
            #print("[+]"+str(URL))
            html = requests.get(URL).text
            urls = re.findall('"objURL":"(.*?)",', html, re.S)
            for url in urls:
                # url = url.replace("\\","")
                # print(url)
                QtWidgets.QApplication.processEvents()
                if count == number + 1: break
                try:
                    pic = requests.get(url, timeout=30)
                    string = imgPath + "/"+str(count) + '.jpg'
                    with open(string, "wb") as f:
                        f.write(pic.content)
                        #print("[%d%%]下载第%d张图片：%s" % (int(count * 100 / number), count, str(url)))
                        #print(round(count * 100 / number, 1))
                        self.getBar.setProperty("value", round(count * 100 / number, 1))
                        self.textGet.setText(str(count)+"/"+str(number))
                        count += 1
                except Exception as e:
                    print('[%d%%]下载第%d张图片时失败: %s' % (int(count * 100 / number), count, str(url)))
                    print(e)
                    continue

    def get_tencent_pic(self,keyWord):
        '''url: 要爬取的漫画首页。 path: 漫画下载路径。 lst: 要下载的章节列表(-l|--list后面的参数)'''
        url= "http://ac.qq.com/Comic/comicInfo/id/"+tc.get_id(keyWord)
        path= self.downloadFile
        lst = None
        one_folder = False
        count = 0
        try:
            if not os.path.isdir(path):
                os.makedirs(path)
            id = tc.getId(url)
            comicName, comicIntrd, chCount, contentList = tc.getContent(id)
            contentNameList = []
            for item in contentList:
                contentNameList.append(item['name'])
            # print('漫画名: {}'.format(comicName))
            # print('简介: {}'.format(comicIntrd))
            # print('章节数: {}'.format(chCount))
            # print('章节列表:')
            # try:
            #     print('\n'.join(contentNameList))
            # except Exception:
            #     print('章节列表包含无法解析的特殊字符\n')

            forbiddenRE = re.compile(r'[\\/":*?<>|]')  # windows下文件名非法字符\ / : * ? " < > |
            comicName = re.sub(forbiddenRE, '_', comicName)  # 将windows下的非法字符一律替换为_
            comicPath = os.path.join(path, comicName)
            if not os.path.isdir(comicPath):
                os.makedirs(comicPath)
            # print()
            listpath = comicPath + '/list.txt'
            listfile = open(listpath, 'w')
            listfile.write('漫画名: {}'.format(comicName) + '\n')
            listfile.write('简介: {}'.format(comicIntrd) + '\n')
            listfile.write('章节数: {}'.format(chCount) + '\n')
            listfile.write('章节列表:' + '\n')
            try:
                listfile.write('\n'.join(contentNameList))
            except Exception:
                listfile.write('章节列表包含无法解析的特殊字符\n')

            listfile.close()
            if not lst:
                contentRange = range(1, len(contentList) + 1)
            else:
                contentRange = tc.parseLIST(lst)
            for i in contentRange:
                if i > len(contentList):
                    print('警告: 章节总数 {} ,'
                          '参数中包含过大数值,'
                          '自动忽略'.format(len(contentList)))
                    break

                contentNameList[i - 1] = re.sub(forbiddenRE, '_',
                                                contentNameList[i - 1]).strip()  # 将windows下的非法字符一律替换为_
                contentPath = os.path.join(comicPath, '第{0:0>4}话-{1}'.format(i, contentNameList[i - 1]))

                # try:
                #     print('正在下载第{0:0>4}话: {1}'.format(i, contentNameList[i - 1]))
                # except Exception:
                #     print('正在下载第{0:0>4}话: {0}'.format(i))

                if not one_folder:
                    if not os.path.isdir(contentPath):
                        os.mkdir(contentPath)

                imgList = tc.getImgList(contentList[i - 1]['url'])
                tc.downloadImg(imgList, contentPath, one_folder)
                count+=1
                self.getBar.setProperty("value", round(count * 100 / len(contentRange), 1))
                self.textGet.setText(str(count) + "/" + str(len(contentRange)))
                QtWidgets.QApplication.processEvents()


        except Exception as e:
            print(e)
            return 0
            #exit(e.code)

    def get_migu_pic(self):
        # ==============================
        URL = "http://www.migudm.cn/search/result/list.html?hintKey="
        URL = URL + str(base64.b64encode(self.keyWord.encode('utf-8')), 'utf-8') + "&hintType=2&pageSize=30&pageNo=1"

        html = requests.get(URL).text
        allID = re.findall('<div class="clItemLeft">(.*?)"Position_ID":.*?href="/comic/(.*?).html"(.*?)</a', html,re.S)
        if not allID:
            id = -1
            #print("[+]Can't find keyword")
            self.textError.setText("Can not find keyword:" + self.keyWord)
            return 0  # 报错退出

        for item in allID:
            if len(re.findall('<s>(.*?)s>', str(item[2]), re.S)) == 0:
                id = item[1]
                break

        url = "http://www.migudm.cn/comic/" + str(id) + ".html"
        # ======================getChapNum===================
        page = requests.get(url).text
        chapterNum = re.findall('<span class="num">更新至(.*?)话</span>', page, re.S)
        # <span class="num">更新至134话</span>
        if not chapterNum:
            print("[+]作品已下架")
            self.textError.setText(self.keyWord+"作品已下架")
            return 0  # return 0
        chapterNum = int(chapterNum[0])
        # ======================
        folderPath = self.downloadFile + self.keyWord
        if not os.path.isdir(folderPath):
            os.mkdir(folderPath)
        for i in range(1, chapterNum + 1):
            QtWidgets.QApplication.processEvents()
            # chapterUrl = "http://www.migudm.cn/"+str(id)+"/chapter/"+str(i)+".html"
            chapterUrl = "http://www.migudm.cn/opus/webQueryWatchOpusInfo.html?hwOpusId=" + str(id) + "&index=" + str(i) + "&opusType=2"
            imgPage = requests.get(chapterUrl).content
            imgUrls = re.findall('"url":"(.*?)"}', str(imgPage), re.S)
            if not imgUrls:
                self.textError.setText(self.keyWord+":"+str(i)+"章无图片")
                continue  # 章节无图片，退出
            chapterPath = folderPath + "/" + str(i)
            if not os.path.isdir(chapterPath):
                os.mkdir(chapterPath)
            for index, imgUrl in enumerate(imgUrls):
                QtWidgets.QApplication.processEvents()
                img = requests.get(imgUrl).content
                imgPath = folderPath + "/" + str(i) + "/" + str(index) + ".jpg"
                with open(imgPath, "wb") as f:
                    f.write(img)
            self.getBar.setProperty("value", round(i * 100 / chapterNum, 1))
            self.textGet.setText(str(i) + "/" + str(chapterNum))

        print("[Done!]")

class testForm(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(testForm, self).__init__(parent=parent)
        print("testForm")

    def test1(self):
        box = QtWidgets.QMessageBox()
        box.warning(self,"提示","点击了system按钮")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = testForm()
    mainWindow.setWindowTitle("test")

    Form = Ui()#Ui_Form()
    Form.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())