# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:PycharmProjects
# File_name:归一全本.py
# Author: fan fan
# Time:2020年03月01日
'''
分析:
    面向对象的方式
    属性:num:爬几章
    1. 获取所有链接
    2. 拼接网址
    3. 获取小说内容
    4. 存储到txt中
'''
#导入所需模块
import requests
import re

class GuiYi(object):

    def __init__(self,num):
        #头部信息
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
        }
        #网址链接
        self.url = "https://www.17k.com/"
        #全书的链接
        self.bookUrl = "https://www.17k.com/list/2849619.html"
        self.num = num

    #1. 获取所有链接
    def getLink(self):

        #请求网址
        r = requests.get(self.bookUrl,headers = self.headers)

        #接收响应
        response = r.content.decode("utf-8")
        # print(response)

        # 过滤链接
        gl1 = re.findall('<dl class="Volume">(.*?)<div class="Banner_ad"',response,re.S)
        # print(gl1[0])
        gl2 = re.findall('<dl class="Volume">(.*?)</dl>',gl1[0],re.S)
        # print(gl2)
        gl3 = re.findall(r'href="/(.*?)"\n\t\t\t\t\t   title="(.*?)&#13;',gl2[0],re.S)
        # print(gl3)
        return gl3

    #2. 拼接网址
    def pinJie(self):
        list = []
        for i,j in self.getLink():
            a = ((self.url+i),j)
            list.append(a)
        return list

    #3. 获取小说内容
    def getContent(self):
        d = {}
        a = 0
        for i,j in self.pinJie():
            if a==self.num:
                break
            r = requests.get(i,headers=self.headers)
            result = r.content.decode("utf-8")
            # print(result)
            info = re.findall('<div class="p">(.*?)<p class="copy ">', result, re.S)
            info2 = re.findall("<p>(.*?)</p>", info[0], re.S)
            # print(info2)
            d[j] = info2
            a+=1
            # print(d)
        return d

    #4. 存储到txt中
    def saveTxt(self):
        with open("归一全本.txt","w",encoding="utf-8") as f:
            for i,j in self.getContent().items():
                f.write(i+"\n")
                for z in j:
                    f.write(z+"\n")

if __name__ == '__main__':
    g = GuiYi(2)
    # g.getLink()
    # g.pinJie()
    # g.getContent()
    g.saveTxt()