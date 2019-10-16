#!/usr/bin/python
#-*-coding:utf-8-*-
def erjinzhi(a):
    b=[]
    while a>=1:
        c=a%2
        a=a//2
        b.append(str(c))
    b.reverse()
    b=''.join(b)
    print('0b%s'%(b))
    # q=str(b).strip('[]')
    # i=''.join(q.split(', '))
    # print('0b%s'%(i))
# a=int(input('>>>'))
# if a>15:
#     while a>=16:
#         c=a%16
#         a=a//16
#         print(c)
# if a>9:
#     if a==10:
#         print('a')
#     elif a==11:
#         print('b')
#     elif a==12:
#         print('c')
#     elif a==13:
#         print('d')
#     elif a==14:
#         print('e')
#     elif a==15:
#         print('f')
# else:
#     print(a)
# erjinzhi(123456789)
# print(bin(123456789))
# import re
#
# file = open('d:\\pycharm\\chen\\cj\\111.txt','r',encoding='utf-8', errors='ignore')
#
# def readed(file):
#     line = file.readlines()
#     json = {}
#     real_num = 0
#     notes_num = 0
#     null_num = 0
#     for item in line:
#         if item.strip() == '':
#             null_num += 1
#         if re.match('//[^\r\n]*|/\*.*?\*/|<!--', item.strip()):
#             notes_num += 1
#     real_num = len(line) - notes_num - null_num
#     json = {'注释行': notes_num, '空行': null_num, '代码行': real_num}
#     return json
# a=[{'电脑':3000,'序号':0},{'电视':2000,'序号':1},{'手机':1000,'序号':2}]
# for i in a[0].items():
# print(a[0].items()[0])
# v=['a','b','c']
# j=['x','y','z']
# l=[]
# for q in v:
#     for w in j:
#         l.append(q)
#         l.append(w)
# print(l)
# class Nme:
#     def eat(self):
#         print('12345')
#     def ddd(self):
#         print('6789')
# qwe = Nme()
# qwe.ddd()
# qwe.eat()
# print(qwe)
class Person:
    def __init__(self,name,tizhong):
        self.name = name
        self.tizhong = tizhong
    def __str__(self):
        return '我的名字叫%s 体重%.2f公斤'%(self.name,self.tizhong)
    def run(self):
        print('%s爱跑步'%self.name)
        self.tizhong-=0.5
    def eat(self):
        print('%s是个吃货爱吃东西'%self.name)
        self.tizhong+=1
# xiaoming = Person('小明',75)
# xiaoming.run()
# xiaoming.eat()
# print(xiaoming)
# xiaomei = Person('斌斌',75)
# xiaomei.eat()
# xiaomei.run()
# print(xiaomei)
# while True:
#     print('-'*20+'猜拳游戏'+'-'*20)
#     c=str(input('请输入（石头，剪刀，布）:\n'))
#     a=['石头','剪刀','布']
#     import random
#     b=random.randrange(3)
#     e=a[b]
#     print('电脑出的是：%s'%(e))
#     if(c=='石头' and e=='剪刀') or (c=='剪刀'and e=='布') or (c=='布' and e=='石头'):
#         print('赢了')
#     elif (e=='石头' and c=='剪刀') or (e=='剪刀'and c=='布') or (e=='布' and c=='石头'):
#         print('输了')
#     elif c==e:
#         print('平局')
#     else:
#         print('请重新输入')
#     print('-'*20+'游戏结束'+'-'*20)
# a=[12,33,43,33,43,12]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# a=int(input('>>>'))
# if a%2==0 or a%3==0:
#     if a%2==0 and a%3==0:
#         print('hello word')
#     elif a%2==0 and a%3!=0:
#         print('hello')
#     elif a%2!=0 and a%3==0:
#         print('word')
# else:
#     print('123')
# a=input('>>>')
# b=a[::-1]
# if a==b:
#     print('是')
# else:
#     print('不是')
# a=input('>>>')
# b=a[::-1]
# c=0
# for i,j in enumerate(a):
#     if j==b[i]:
#         c=1
#         break
# else:
#     c=0
# print(c)
# if c==1:
#     print('是')
# else:
#     print('不是')
# print(int(2.5))
# a='I love this Game'
# b=a.split(' ')
# b.reverse()
# c=' '.join(b)
# print(c)
def dd(*args):
    b=list(args)
    c=[]
    for i in b:
        if i not in c:
            c.append(i)
    c.sort()
    for j in b:
        if j==c[-1] or j==c[-2]:
            print(j,end=' ')
def xinshu(a,b=0):
    for i in range(1,a):
        if a%i==0:
            b+=i
    if b==a:
        print('满足')
    else:
        print('不满足')
def shu(*args,b=0):
    a=args
    c=a[::-1]
    for i in range(len(a)):
        for j in range(10):
            if c[i]==str(j):
                b+=j*10**i
    print(b)

def shiliu(i):
    d=[]
    a=[str(i) for i in range(10)]+[chr(j) for j in range(97,103)]
    while i>0:
        b=i%16
        i=i//16
        d.append(a[b])
    d.reverse()
    e=''.join(d)
    print('0x%s'%e)
def zushu(*args):
    a=args
    c=[]
    for i in a:
        for j in a:
            for s in a:
                if i//10==0 and j//10==0 and s//10==0:
                    if i!=0:
                        if i!=j and i!=s and j!=s:
                            b=100*i+10*j+s
                            c.append(b)
    print(len(c))
    print(c)
# a = 1
# b = 0
# while a<=100:
#     b += a
#     a += 1
# zushu(0,2,3,4,5)
# def ll(*args):
#     a=list(args)
#     b=[]
#     for i,j in enumerate(a):
#         b.insert(i-1,j)
#     print(b)
# import requests
# import re
# import json
# url='https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3637489548,2215770189&fm=26&gp=0.jpg'
#     # "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2859607507,4290510034&fm=26&gp=0.jpg"
# a=requests.get(url)
# b=a.content
# with open('b.jpg','ab') as c:
#     c.write(b)
a=45
s=[2]

while a<100:
    b = 1
    while b<a:
        b+=1
        if a%b==0:
            continue
    else:
        s.append(a)
        break
    a+=1
print(s)
# print('aaaa')