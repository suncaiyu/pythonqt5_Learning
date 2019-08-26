
import requests
import re
import os


def getHTMLText(url):
    with open('cookie.txt', encoding='utf-8') as file_obj:
        contents = file_obj.read()
    kv = {'cookie':contents
          ,'user-agent':'Mozilla/5.0'}                                   #伪造游客
    try:
        r = requests.get(url, headers=kv,timeout=30)
        r.raise_for_status()                                             #不是200，产生异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)              #以列表类型返回形如  "view_price":"186.2" ,反斜杠\" \"表示"view_price"
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)                   #以列表类型返回形如  "raw_title":"小米手机"(最小匹配，输出最短字符串)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])                 #详见淘宝商品信息爬虫（1）
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])                          #在列表后新增一个元素
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


# def main():
#     goods = '马里奥制造2'
#     depth = 4
#     start_url = 'https://s.taobao.com/search?q=' + goods
#     infoList = []
#     for i in range(depth):                                    #循环3次
#         try:
#             url = start_url + '&s=' + str(44 * i)             #淘宝商品页面列表从0,44,88。
#             html = getHTMLText(url)                          #两个函数
#             parsePage(infoList, html)
#         except:
#             continue
#     printGoodsList(infoList)


# main()