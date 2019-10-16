#!/usr/bin/python
#-*-coding:utf-8-*-
import requests
import re
# a='http://www.quanshuwang.com/book/44/44683/15379610.html'
# b=requests.get(a)#请求网址
# print(b)
#接收相应内容第一种text
# c=b.text#以文本接收内容
# print(c)
#第二种是content：一字节的方式接收
# e=b.content.decode('gbk')
# print(e)
# for l in range(6971193,10153072):
#     i='http://www.quanshuwang.com/book/0/470/%d.html'%l
#     j=requests.get(i)
#     print(j)
#     z=j.content.decode('gbk')
#     # print(type(z))
#     # print(z)
#     guolv=re.compile('<script type="text/javascript">style5(.*?)<script type="text/javascript">style6',re.S)
#     aaa=re.findall(guolv,z)
#     print(aaa)
#     # g=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
#     # b=g.findall(str(aaa))
#     # print(b)
#     with open('11112.txt','a',encoding='utf8') as v:
#             for i in aaa:
#                 v.write(str(i).replace('<br />\r\n<br />\r\n&nbsp;&nbsp;&nbsp;&nbsp;',' \n')+"\n")
# import json
# with open('a.txt','w',encoding='utf8') as d:
#     url='https://map.baidu.com/?qt=subwayscity&t=1569031947814'
#     head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#     a=requests.get(url,headers=head)
#     geshi=a.text
#     b=json.loads(geshi)
#     c=len(b['subways_city']['cities'])
#     for i in range(c):
#       d.write(b['subways_city']['cities'][i]['cn_name']+'\n')
# a='https://movie.douban.com/chart'
# b=requests.get(a)
# print(b)
# # c=b.content.decode('utf8')
# # d=re.compile('<p class="pl">(.*?)</p>')
# # e=re.findall(d,c)
# # print(e)
# # with open('1111.txt','w',encoding='utf8') as f:
# #     for i in e:
# #         f.write(i+'\n')
# # g=re.compile(' <img src="(.*?)" width="75"')
# # h=re.findall(g,c)
# # for s in range(len(h)):
# #     with open('%d.jpg' % s, 'wb') as l:
# #             a = requests.get(h[s])
# #             b = a.content
# #             l.write(b)
import requests
import re
import json
import time
import xlwt
import xlrd
# from xlutils.copy import copy
# yuan = xlrd.open_workbook('aaa.xls')
# new=copy(yuan)
# e=new.get_sheet(0)
# j=0
# for l in range(7):
#
#     xl = xlwt.Workbook(encoding='utf8')
#     e = xl.add_sheet('智联')
#     time.sleep(3)
#     a=f'https://fe-api.zhaopin.com/c/i/sou?start={j}&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.56843482&x-zp-page-request-id=cfe77fb052454e8481cd04b48a154e3a-1569205773582-496299&x-zp-client-id=3c7d0936-0c19-488c-8fe0-f1cc816645c4'
#     j+=90
#     head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
#     b = requests.get(a,headers=head)
#     print(b)
#     c=b.text
#     d=json.loads(c)
#     print(d['data']['results'])
#     s=len(d['data']['results'])
#     for i in range(s):
#         print(d['data']['results'][i]['company']['name'])
#         e.write(i+1,0,d['data']['results'][i]['company']['name'])
#         e.write(i+1,1, d['data']['results'][i]['company']['type']['name'])
#         e.write(i+1,2,d['data']['results'][i]['jobName'])
#         e.write(i+1,3,d['data']['results'][i]['company']['size']['name'])
#         e.write(i+1,4,d['data']['results'][i]['salary'])
#         e.write(i+1,5,d['data']['results'][i]['eduLevel']['name'])
#         e.write(i+1,6,d['data']['results'][i]['welfare'])
#         xl.save(f'{l}.xls')


# url='https://www.nowcoder.com/discuss/82568'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# a=requests.get(url)
# b=a.content.decode('utf-8')
# gg=re.compile(' <br> </div> <div>(.*?)<br> </div> <div>',re.S)
# zz=re.findall(gg,b)
# print(zz)
# aa=str(zz).split('<br>')
# print(aa)
# with open('asd.txt','w',encoding='utf8') as  l:
#     for i in aa:
#         i=i.split('</div> <div> ')
        # i=i.replace('<br> <span>', ' ')
        # i=str(i).split('<span>')
        # i=str
        #
        # l.write(str(i) + '\n')
        # print(i)
    # for j in i :
    #     j=j.split('</span> </div> <div>')
    #     print(j)
    # l.write(i+'\n')
    # l.write('\n')
# from urllib.request import urlopen ,Request
# from http.client import HTTPResponse
# url='http://www.bing.com'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# aa=Request(url,headers=head)
# a=urlopen(aa,timeout=5)
# print(a.closed)
# with a:
#     print(type(a))
#     print(a.read())
#     print(a.geturl())
#     print(a.status)
#
# print(a.closed)
url = 'http://www.quanshuwang.com/book/9/9055/9674697.html'
pp=requests.get(url)
aa=pp.content.decode('gbk')
req = re.compile(' id="content">(.*?)<script type="text/javascript">style6',re.S)
gg=re.findall(req,aa)
print(gg)
