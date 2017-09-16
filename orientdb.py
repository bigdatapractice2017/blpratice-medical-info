import pyorient
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# 导入了v_Cookbook,v_Food,v_Function,e_CookWith,e_HasFunction
pages = []
urls = []
pages1 = []

client = pyorient.OrientDB("localhost", 2424)
client.connect("rainkey", "12345678")
client.db_open("cnys", "admin", "admin")


def get_links():
    global pages
    html = urlopen("http://www.cnys.com/shicai/").read().decode("utf-8")
    bsobj = BeautifulSoup(html, "html.parser")
    data = bsobj.find("div", {"class": "wrap1000"}).findAll("a", href=re.compile(r"^http://"))
    for url in data:
        food_name = url.get_text()
        if url["href"] not in pages and food_name not in urls:
            pages.append(url["href"])
            urls.append(url.get_text())
        else:
            print(food_name)
        sql = "LET $food_name = select name from v_Food WHERE name='%s';" \
              "if($food_name.size() < 1){" \
              "CREATE VERTEX v_Food SET name='%s';" \
              "}" % (food_name, food_name)
        client.batch(sql)
    print(len(urls))

get_links()


def get_data():
    global pages1
    i = 0
    while i < len(pages):
        html = urlopen(pages[i]).read().decode("utf-8")
        bsobj = BeautifulSoup(html, "html.parser")
        data = bsobj.find("div", {"class": "tabmenu"}).findAll("a", href=re.compile(r"dapei\.html$"))
        for url in data:
            pages1.append("http://www.cnys.com"+url["href"])
        i = i+1
get_data()


def get_good():
    i = 0
    j = 0
    while i < len(pages1):
        html = urlopen(pages1[i]).read().decode("utf-8")
        bsobj = BeautifulSoup(html, "html.parser")
        good1 = bsobj.find("div", {"id": "dapeiyes"}).findAll("span")
        for l in good1:

            good_function = [x for x in l.get_text().split("；")]
            good_function0 = [x for x in good_function[0].split(' ')]
            good_cook = good_function0[0]
            if good_cook == '':
                good_cook = None
            good_function1 = good_function[-1]

            if good_function1 == '':
                good_function1 = None
            if good_cook is not None and good_function1 is not None:
                good_cook = good_cook.replace('和', '+')
                sql = "LET $good_cook = select name from v_Cookbook WHERE name = '%s';" \
                      "if($good_cook.size()<1){" \
                      "CREATE VERTEX v_Cookbook SET name='%s',cooking_method='一起吃';" \
                      "}" \
                      "LET $v_cookbook = select from v_Cookbook WHERE name = '%s';" \
                      "LET $good_function1 = select des from v_Function WHERE des = '%s';" \
                      "if($good_function1.size()<1){" \
                      "CREATE VERTEX v_Function SET des='%s';" \
                      "}" \
                      "LET $v_function = select from v_Function WHERE des = '%s';" \
                      "LET $edge = select expand(out('e_HasFunction')) from v_Cookbook WHERE name = '%s';" \
                      "if($edge.size()<1){" \
                      "CREATE EDGE e_HasFunction from $v_cookbook to $v_function;" \
                      "}" % (good_cook, good_cook, good_cook, good_function1, good_function1, good_function1, good_cook)

                print(sql)
                j = j + 1
                client.batch(sql)

        i = i + 1
    print(j)
get_good()


def get_good1():
    i = 0
    j = 0
    while i < len(pages1):
        html = urlopen(pages1[i]).read().decode("utf-8")
        bsobj = BeautifulSoup(html, "html.parser")

        good = bsobj.find("div", {"id": "dapeiyes"}).findAll("h5")
        for l in good:
            good_cook = l.get_text()
            foods = good_cook.replace(' ', '')
            food = [x for x in l.get_text().split(' + ')]
            food0 = food[0]
            food1 = food[-1]
            print(food[0])
            print(food1)
            if food1 == '':
                food1 = None
            if food1 is not None:
                sql = "LET $good_cook = select from v_Cookbook WHERE name = '%s';" \
                      "LET $food0 = select from v_Food WHERE name = '%s';" \
                      "LET $food1 = select from v_Food WHERE name = '%s';" \
                      "if($food1.size()<1){" \
                      "CREATE VERTEX v_Food SET name = '%s';" \
                      "}" \
                      "LET $food11 = select from v_Food WHERE name = '%s';" \
                      "LET $edge1 = select from e_CookWith where out in (select from v_Food WHERE name = '%s') and in in (select from v_Cookbook WHERE name = '%s');" \
                      "if($edge1.size()=0){" \
                      "create edge e_CookWith from $food0 to $good_cook;" \
                      "}" \
                      "LET $edge2 = select from e_CookWith where out in (select from v_Food WHERE name = '%s') and in in (select from v_Cookbook WHERE name = '%s');" \
                      "if($edge2.size()=0){" \
                      "create edge e_CookWith from $food11 to $good_cook;" \
                      "}" \
                      % (foods, food0, food1, food1, food1, food0, foods, food1, foods)

                print(sql)
                j = j + 1
                client.batch(sql)

        i = i + 1
    print(j)
get_good1()

