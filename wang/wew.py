#!/usr/bin/python
#-*-coding:utf-8-*
# for i in range(1,10):
#     for c in range(1,i+1):
#             print('%d*%d=%d'%(i,c,i*c),end=' ')
#     print()

# for i in range(10):
#     import random
#     a=random.randrange(20)
#     break
# print(a)
# import random
# a=random.randrange(100)
# b=random.randrange(100)
# print(a,b)
# if a>b:
#     print(b,a)
# else:
#     print(a,b)
# while True:
#     c=0
#     a=int(input('请输入数字'))
#     for b in range(1,a+1):
#         if a%b==0:
#             c+=b
#     print(c)
# print('-'*5,'求水仙花数','-'*5)
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10%10
#     if a**3+b**3+c**3==i:
#         print(i)
# print('-'*5,'求水仙花数','-'*5)
# while True:
#     a=(int(input('输入边长')))
#     b=(int(input('输入边长')))
#     c=(int(input('输入第三边边长')))
#     q=[a,b,c]
#     q.sort()
#     a=q[0]
#     b=q[1]
#     c=q[2]
#     if a+b>c:
#         if a**2+b**2==c**2:
#             print('直角三角形')
#         elif a**2+b**2>c**2:
#             print('锐角三角形')
#         elif a**2+b**2<c**2:
#             print('钝角三角形')
#         #elif a==b==c:
#           #  print('等边三角')
#     else:
#         print('不是三角形')
# for i in range(2,2):
#     print(i)
# a=0
# b=0
# while a<=99:
#     a+=1
#     b+=a
# print(b# b=[]
# for c in range(10):
#     import random
#     a=random.randrange(100)
#     b.append(a)
# print(b)
# b=[12,1,78,45,35]
# for i in range(len(b)):
#     for s in range(len(b)):
#         for x in range(s+1,len(b)):
#             if b[s]>b[x]:
#                 b[s],b[x]=b[x],b[s]
#                 #break
# print(b)
def jiujiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d*%d=%d'%(j,i,i*j),end=' ')
        print()


    #print(b)
#
#
# han()

# a.write('nihao''\n'*100)
# def han():
#     a = open(r'1111.txt', 'w', encoding='ansi')
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             a.write(' %d*%d=%d' % (j, i, i * j ) )
#         a.write('\n')
#     a.close()
# han()
# b=a.readline()
# x=a.readline()
# c=[]
# for i in range(len(b)):
#     z=b[i].strip('\n')
#     c.append(z)
# print(c)
# for j in range(len(b)):
#     s=b[j].split('\n')
#     c.append(s)
# a.write('nihao')
# with open(r'1111.txt','w',encoding='utf-8') as a:
#     b='今天晚上，妈妈带我到油田的外婆家玩'+'\n'+'到了外婆家，妈妈就一直在和外婆谈话。我觉得很无聊，于是，我就叫了几个小伙伴拿着瓶子一起去附近的田野里捉蛐蛐。'+'\n'+'走近田野，我们就听见了蛐蛐的“大合唱”。于是，我们拿着各自的瓶子，轻手轻脚地寻找着蛐蛐的下落。''\n''过了一会儿，我发现，在前方一米处，有一只乌黑油亮的蛐蛐正在忘我地高声歌唱着。''\n''我高兴极了，就蹑手蹑脚地走了过去。但是，那只蛐蛐似乎察觉到了我的存在，还没等我迈开第一步，''\n''它就轻轻地跳了好几下，眨眼间，它就从我的视野里消失了。“唉！它干嘛要这么机灵呢？”我自言自语道。'+'\n'+'忽然，有一个小伙伴大叫道：“我抓到了！我抓到了！”我们往他的瓶子里一看，''\n''果然，他的瓶子里有一只乌黑油亮的大蛐蛐。我羡慕极了，心想：我一定也要抓一只更大的蛐蛐。于是，我就继续去寻找蛐蛐。'+'\n'+'突然，我发现有一只特别大的蛐蛐正在悠闲地唱着歌。我怕它再逃跑了，于是，我不管三七二十一，猛地扑上去，抓住了它。'+'\n'+'时间不早了，我才恋恋不舍地离开了田野。'+'\n'+'捉蛐蛐真有趣啊！'+'\n'+'文| 李梓铭'
#     a.write(b)
# with open(r'1111.txt','r',encoding='utf-8') as c:
#     print(len(c.readlines()))
    # print(len(a.readlines()))
# a.close()
# for i in range(100):
#     for j in range(101):
#         for s in range(100):
#             if 2*i+j+0.5*s==100 and i+j+s==100:
#                 print(i,j,s)
# a=[f'{j}*{i}={i*j}' for i in range(1,10)for j in range(1,i+1)]
# print(a)
# import pymysql#用来连接与操作数据库的,charset是数据库统一编码
# conn=pymysql.connect(host='192.168.2.145',port=3306,user='root',passwd='123456',db='pachong')
# 创建游标
# cusor=conn.cursor()
# 执行语句
# cusor.execute('create database ng;')
# cusor.execute('create table bb(name char);')
# cusor.execute('show tables;')
# cusor.execute('show databases;')
# print(cusor.fetchmany(4))#默认只显示结果的第一个值
# conn.commit()#提交数据
# conn.close()#
# from time import sleep
# a=[1,23,4,54,6765,7676,878,79,898,9,80,9,10,98,9,9]
# for i,j in enumerate(a):
#     if 5<i<=12:
#         print(j)
# with open('11112.txt','r',encoding='utf8') as a:
#     for i,j in enumerate(a.readlines()):
#         if 16<i<22:
#             print(j)

from wang.函数 import *
# jiujiu()
# a=0
# b=1
# while a<=9:
#     b=1
#     while b<a+1:
#         print(f'{b}*{a}={a*b}',end=' ')
#         b+=1
#     a+=1
#     print
# i
# y = int(input('年:\n'))
# m = int(input('月:\n'))
# d = int(input('日:\n'))
# i = 0
# a = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
# if 1 <= m <= 12:
#     i = a[m - 1] + d
# else:
#     print('请重新输入')
# if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
#     if m > 2:
#         print('第%d天' % (i + 1))
#     else:
#         print('第%d天' % (i))
# else:
#     print('第%d天' % (i))\
# f= open('1111.txt','r')
# for i in f:
#     print(i.strip().split(','))
# f.close()
def qqq(*args):
    a=args
    b=[]
    for i in a:
        if i not in b :
            b.append(i)
    b.sort()
    # print(b[-1])
    for i in a:
        if i==b[-1] or i==b[-2]:
            print(i,end=' ')

qqq(12,34,34,16,16,18,18)