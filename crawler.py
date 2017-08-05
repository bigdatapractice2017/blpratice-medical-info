from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = []
pages1 = []

#file = open('ys.txt', "wb")
def getlinks():
    global pages
    html = urlopen("http://www.cnys.com/shicai/").read().decode("utf-8")
    bsobj = BeautifulSoup(html, "html.parser")
    data = bsobj.find("div", {"class": "wrap1000"}).findAll("a", href=re.compile(r"^http://"))
    # data = bsobj.findAll("a", href=re.compile(r"^http://"))
    for url in data:
        pages.append(url["href"])
        # file.write(('\r' + url.get_text() + '\r\n').encode('UTF-8'))
        print(url.get_text())

    # print(data)
getlinks()
print(len(pages))
print(pages[0])

def getnutuition():
    i = 0
    while i < len(pages):
        html = urlopen(pages[i]).read().decode("utf-8")
        bsobj = BeautifulSoup(html, "html.parser")
        # gongxiao = bsobj.find("div", {"class": "shicai_head"}).select(".tit01")[0].text
        gongxiao = bsobj.find("div", {"class": "shicai_head"}).findAll("h2")[0]

        nutu1 = bsobj.find("div", {"class": "shicai_head"}).select(".tit01")[1].text
        # nutu1 = bsobj.find("div", {"class": "shicai_head"}).findAll("h2")[1]

        gongxiao1 = bsobj.find("div", {"class": "gongxiao"}).findAll("a")

        shiyi = bsobj.find("div", {"class": "shicai_head"}).find("ul", {"class": "infos"}).find("li", {"c3"}).p
        jinji = bsobj.find("div", {"class": "shicai_head"}).find("ul", {"class": "infos"}).find("li", {"c4"}).p

        # for s in gongxiao:

        print(gongxiao.get_text())
        # print(gongxiao)


        for gx in gongxiao1:
            print(gx.get_text())
        print("适宜人群："+shiyi.get_text())
        print("禁忌人群："+jinji.get_text())
        print(nutu1)
        try:
            yingyang = bsobj.find("div", {"class": "yingyangs"}).findAll("a")
            yingyang1 = bsobj.find("div", {"class": "yingyangs"}).findAll("i")

            try:
                a = []
                for yg in yingyang:
                    a.append(yg.get_text())
                    # print(yg.get_text())
            except Exception as ex:
                    print(ex)
            try:
                b = []
                for yg1 in yingyang1:
                    b.append(yg1.get_text())
                    # print(yg1.get_text())
            except Exception as ex:
                    print(ex)
            # n = 0
            # while n < len(b):
                # print(a[n] + b[n])
                # n = n + 1
            for (aa, bb) in zip(a, b):
                print(aa, bb)

        except Exception as ex:
            print(ex)
        # print(nutu1.get_text())




        i = i + 1
getnutuition()
def getdata():
    global pages1
    i = 0
    while i < len(pages):
        html = urlopen(pages[i]).read().decode("utf-8")
        bsobj = BeautifulSoup(html, "html.parser")
        data = bsobj.find("div", {"class": "tabmenu"}).findAll("a", href=re.compile(r"dapei\.html$"))
        for url in data:
            pages1.append("http://www.cnys.com"+url["href"])
            print(url.get_text())
        i = i+1
getdata()
# print(pages1)
# print(len(links))

def getgood():
    i = 0
    while i < len(pages1):
        html = urlopen(pages1[i]).read().decode("utf-8")
        bsobj = BeautifulSoup(html, "html.parser")
        print(bsobj.h2.get_text())
        good = bsobj.find("div", {"id": "dapeiyes"}).findAll("h5")
        good1 = bsobj.find("div", {"id": "dapeiyes"}).findAll("span")


        for l in good:
            print(l.get_text())
        for l in good1:
            print(l.get_text())
        bad = bsobj.find("div", {"id": "dapeino"}).h2
        bad1 = bsobj.find("div", {"id": "dapeino"}).findAll("h5")
        bad2 = bsobj.find("div", {"id": "dapeino"}).findAll("span")
        print(bad.get_text())
        for b in bad1:
            print(b.get_text())
        for b in bad2:
            print(b.get_text())

        i = i + 1
getgood()



