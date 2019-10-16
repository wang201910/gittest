#!/usr/bin/python
#-*-coding:utf-8-*-
# a='asddsa'
# b=a[::-1]
# c=int(len(a)/2)
# if len(a)%2==0:
#     for i in range(c):
#         if a[i]==b[i]:
#             pass
#         else:
#             print('不是')
#     # print('是')
# else:
#     print('不是')
import requests
import re
class douban(object):
    def qing_qiu(self,page):
        url=f'https://movie.douban.com/top250?start={page}&filter='
        head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        res=requests.get(url=url,headers=head)
        #读取文件
        h=res.content.decode('utf8')
        return h
    def guolv(self,html):
        patt=re.compile('<img width="100" alt="(.*?)"',re.S)
        ht=re.findall(patt,html)
        daoyan=re.compile('导演:(.*?)&nbsp;&nbsp;&nbsp;')
        hh=re.findall(daoyan,html)
        return ht,hh
    def baocun(self,aa):
        with open('c.txt','w',encoding='utf8') as a:
            pass
dd=douban()
cc=dd.qing_qiu(25)
# print(cc)
aa=dd.guolv(cc)
print(aa)
b=aa[1]
c=[]
for i in b:
    print(i)
