#!/usr/bin/env python3
# -*-coding:utf-8-*-
# 目的：爬取整个网站到本地以html的形式保存网页
# 结果：通过一层一层的不断获取整个网页的链接的方式爬取到了整个网站的网页到本地，很少的一部分网页丢失
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def get_links():
    global pages
    global info7
    html = urlopen("http://www.cnys.com").read().decode("utf-8")
    bsobj = BeautifulSoup(html, "html.parser")
    bsobj1 = BeautifulSoup(html, "html5lib")
    producer = bsobj1.findAll('a')
    # producer1 = bsobj1.findAll('a')['href'] = '1111'
    i = 0
    while i < len(producer):
        # print(producer)
        # str(producer[i]['href']).replace("http:", '')
        pageurl = str(producer[i]['href']).replace("http://www.", '').replace("//www.", '').replace("/", '_').replace(
            '.', '_')
        if pageurl.startswith('cnys'):
            # if pageurl not in pages2:
            link.append(pageurl)
            pages2.add(pageurl)
        producer[i]['href'] = str(producer[i]['href']).replace("http://www.", '').replace("//www.", '').replace("/", '_').replace('.', '_') + '.html'
        i += 1
    print(pages2)
    print(link)
    # print(bsobj1, file=file1)
    file1.write(str(bsobj1))
    file1.close()
    data = bsobj.findAll("a", href=re.compile(r"^(http:)|www"))
    # data = bsobj.findAll("a", href=re.compile(r"^(http:|)//"))
    # data = bsobj.findAll("a", href=re.compile(r"^(http:|www)"))
    # listurl = re.findall(r'www.+?', html)
    # print(listurl)
    for url in data:
        # link = re.split(r"//", url["href"])
        pages.append(url["href"])
        # file.write(('\r' + url.get_text() + '\r\n').encode('UTF-8'))
        # print(url.get_text())
        # print(link)
        # print(pages)
    info = str(pages).replace("//", "")
    info1 = info.replace("http:", "")
    info2 = info1.replace("]", "")
    info3 = list(re.findall(r"www.*", info2))
    info4 = info3[0]
    info5 = info4.replace("'", "")
    # print(len(info5))
    print(info5)
    info6 = [l for l in info5.split(",")]
    print(info6[0])
    i = 0
    while i < len(info6):
        info66 = str(info6[i])
        if info66.startswith(' www.cnys'):
            src = ('http://' + info66).replace(" ", '')
            if src not in info7:
                if src == 'http://www.cnys.com/' or src == 'http://www.cnys.com':
                    pass
                else:
                    info7.append(src)
        i += 1
    # info7.remove('http://www.cnys.com/')
    print(len(info7))
    print(info7)
    print("6" + info6[5])
    # print(len(info1))
    # print(info1)


# print(len(pages1))
# print(len(info1))
# print(info7[5])
# html = urlopen('http://www.cnys.com/ysys/').read().decode("utf-8")
# print(html)


def get_links1():
    i = 0
    global pages1
    while i < len(info7):
        try:
            html = urlopen(info7[i]).read().decode("utf-8")
            s = str(info7[i]).replace('http://www.', '')
            s1 = s.replace('/', '_').replace('.', '_')
            # print(html, file=file1)
            bsobj = BeautifulSoup(html, "html.parser")
            bsobj1 = BeautifulSoup(html, "html5lib")
            producer1 = bsobj1.findAll('a')
            l = 0
            while l < len(producer1):
                try:
                    if producer1[l].get('href'):
                        producer1[l]['href'] = str(producer1[l]['href']).replace("http://www.", '').replace("//www.", '').replace("/",'_').replace('.', '_').replace('?', '_') + '.html'
                    # 获取不到有问号的链接
                except Exception as ex:
                    print(ex)
                l += 1
            # while l < len(producer):
            #     # print(producer)
            #     # str(producer[i]['href']).replace("http:", '')
            #     # pageurl = str(producer[i]['href']).replace("http://www.", '').replace("//www.", '').replace("/",'_').replace('.', '_')
            #     # if pageurl.startswith('cnys'):
            #     #     # if pageurl not in pages2:
            #     #     link.append(pageurl)
            #     #     pages2.add(pageurl)
            #     producer[i]['href'] = str(producer[i]['href']).replace("http://www.", '').replace("//www.", '').replace("/", '_').replace('.', '_') + '.html'
            #     l = l + 1
            # #print(pages2)
            f1 = open('G:\Pycharm Code\cnys\cnyshtmls1\\' + s1 + '.html', 'w', encoding='utf-8')
            # print(bsobj1, file=f1)
            f1.write(str(bsobj1))
            f1.close()
            data = bsobj.findAll("a", href=re.compile(r"^http://"))
            for url in data:
                if url["href"] not in info7:
                    if url["href"] not in pages1:
                        if url["href"] == 'http://www.cnys.com/' or url["href"] == 'http://www.cnys.com':
                            pass
                        else:
                            pages1.append(url["href"])
    # print(url, file=file1)
        except Exception as ex:
            print(ex)
        i = i+1
    print(pages1)
    print(len(pages1))


def get_links2():
    global pages3
    i = 0
    while i < len(pages1):
        try:
            html = urlopen(pages1[i]).read().decode("utf-8")
            s = str(pages1[i]).replace('http://www.', '')
            s1 = s.replace('/', '_').replace('.', '_')
            # print(html, file=file1)
            bsobj = BeautifulSoup(html, "html.parser")
            bsobj1 = BeautifulSoup(html, "html5lib")
            producer2 = bsobj1.findAll('a')
            l = 0
            while l < len(producer2):
                try:
                    if producer2[l].get('href'):
                        if str(producer2[l]['href']).startswith('/shicai') or str(producer2[l]["href"]).startswith('/yingyang'):
                            producer2[l]["href"] = "http://www.cnys.com" + producer2[l]["href"]
                            producer2[l]['href'] = str(producer2[l]['href']).replace("http://www.", '').replace("//www.",'').replace("/", '_').replace('.', '_').replace('?', '_') + '.html'
                        else:
                            producer2[l]['href'] = str(producer2[l]['href']).replace("http://www.", '').replace("//www.", '').replace("/", '_').replace('.', '_').replace('?', '_') + '.html'
                        # 获取不到有问号的链接
                except Exception as ex:
                    print(ex)
                l += 1
            f2 = open('G:\Pycharm Code\cnys\cnyshtmls1\\' + s1 + '.html', 'w', encoding='utf-8')
            # print(bsobj1, file=f2)
            f2.write(str(bsobj1))
            f2.close()
            data = bsobj.findAll("a", href=re.compile(r"^(http://|/shicai|/yingyang)"))  # http://www.cnys不行
            for url in data:
                if url["href"] not in info7:
                    if url["href"] not in pages1:
                        if url["href"] not in pages3:
                            if url["href"] == 'http://www.cnys.com/' or url["href"] == 'http://www.cnys.com':
                                pass
                            elif str(url["href"]).startswith('/shicai') or str(url["href"]).startswith('/yingyang'):
                                url["href"] = "http://www.cnys.com"+url["href"]
                                pages3.append(url["href"])
                            else:
                                pages3.append(url["href"])
    # print(url, file=file1)
        except Exception as ex:
            print(ex)
        i += 1
    print(pages3)
    print(len(pages3))


def get_links3():
    global pages4
    i = 0
    while i < len(pages3):
        try:
            html = urlopen(pages3[i]).read().decode("utf-8")
            s = str(pages3[i]).replace('http://www.', '')
            s1 = s.replace('/', '_').replace('.', '_').replace('?', '_')
            # print(html, file=file1)
            bsobj = BeautifulSoup(html, "html.parser")
            bsobj1 = BeautifulSoup(html, "html5lib")
            producer3 = bsobj1.findAll('a')
            l = 0
            while l < len(producer3):
                try:
                    if producer3[l].get('href'):
                        if str(producer3[l]['href']).startswith('/shicai') or str(producer3[l]["href"]).startswith('/yingyang'):
                            producer3[l]["href"] = "http://www.cnys.com" + producer3[l]["href"]
                            producer3[l]['href'] = str(producer3[l]['href']).replace("http://www.", '').replace("//www.", '').replace("/", '_').replace('.', '_').replace('?', '_') + '.html'
                        else:
                            producer3[l]['href'] = str(producer3[l]['href']).replace("http://www.", '').replace("//www.", '').replace("/", '_').replace('.', '_').replace('?', '_') + '.html'
                # 获取不到有问号的链接
                except Exception as ex:
                    print(ex)
                l += 1
            f3 = open('G:\Pycharm Code\cnys\cnyshtmls1\\' + s1 + '.html', 'w', encoding='utf-8')
            # print(bsobj1, file=f3)
            f3.write(str(bsobj1))
            f3.close()
            data = bsobj.findAll("a", href=re.compile(r"^(http://)"))
            for url in data:
                if url["href"] not in info7:
                    if url["href"] not in pages1:
                        if url["href"] not in pages3:
                            if url["href"] not in pages4:
                                if url["href"] == 'http://www.cnys.com/' or url["href"] == 'http://www.cnys.com':
                                    pass
                                elif str(url["href"]).startswith('/shicai') or str(url["href"]).startswith('/yingyang'):
                                    url["href"] = "http://www.cnys.com" + url["href"]
                                    if url["href"] not in pages4:
                                        pages4.append(url["href"])
                                else:
                                    pages4.append(url["href"])
    # print(url, file=file1)
        except Exception as ex:
            print(ex)
        i += 1
    print(pages4)
    print(len(pages4))


if __name__ == '__main__':
    pages = []
    pages1 = []
    pages3 = []
    pages4 = []
    file = "G:\Pycharm Code\cnys\cnyshtmls1\cnys_com_.html"
    # fil = "G:\Pycharm Code\cnys\cnyshtml\cnys.txt"
    # fil1 = open(fil, 'w', encoding='utf-8')
    file1 = open(file, 'w', encoding='utf-8')
    info3 = []
    info4 = []
    info5 = []
    info6 = []
    info7 = []
    producer = []
    producer1 = []
    producer2 = []
    producer3 = []
    link = []
    pages2 = set()
    # pages3 = set()
    get_links()
    get_links1()
    get_links2()
    get_links3()