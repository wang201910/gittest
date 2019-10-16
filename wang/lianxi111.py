#!/usr/bin/python
#-*-coding:utf-8-*-
import requests
import re
url='http://www.quanshuwang.com/book/162/162238/44901629.html'
head={'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
aa=requests.get(url)
cc=aa.content.decode('gbk')
guolv=re.compile('<script type="text/javascript">style5(.*?)<script type="text/javascript">style6',re.S)
dd=re.findall(guolv,cc)
with open(r'1.txt','w',encoding='utf8') as a:
    for i in dd:
        i=i.replace(r'&nbsp;&nbsp;&nbsp;&nbsp;','')
        i=i.replace('<br />','')
        i=i.replace('();</script>','')
        a.write(i)
with open('1.txt','r',encoding='utf-8') as b:
    q=b.readlines()
    print(q)
    for i in q:
        if i=='\n':
            q.remove(i)
    print(q)
    # with open('11.txt','w',encoding='utf8') as ff:
    #     print(q)
    #     for i in q:
    #         if i =='\n':
    #             q.remove(i)
    #     for i in q:
            # print(i)