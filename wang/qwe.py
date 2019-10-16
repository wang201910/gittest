#!/usr/bin/python    #指定解释器的位置（python代码使用哪一个解释器来解释）会被读取
#-*-coding:utf-8-*-  #
# print ('你好，中国') #打印括号内容  先执行内容，在执行打印
#print(input('>>>')) #输入内容  括号里的是提示语  输入的都是字符串
#注释行的方法
#1，#和快捷方式CTRL+ ？注释发
#2，'''单引号注释
#3，"""双引号注释
# print('hell')
# import keyword
# a=keyword.kwlist
# print(a)
# #name=input('请输入你的名字')
# #print(name)
# name='王茂才'
# #print(name)
# name='王'
# print(name)
# print(name)
# a,b,c=1,2,3
# print(a)
# print(b)
# a="i'm a boy "
#print(a[2::4])
'''字符串的内置函数'''
#1，upper：将字符串小写变大写
# print('home'.upper())
# # a=a.upper()
#print(a)
# print('HOME'.lower())
# a='HOME'
# a=a.lower()
# print(a)
# print(input('>>>').lower
#print('name is zhangfei asdada'.title())
# a='qweqqq'
# b=a.replace('q',' 1',2)
# print(b)
# print('151617'.split('5'))
# # b='asdaqdsaddc'
# # b=b.startswith('s')
# print(typ
#print(type(qdsadd))
# while True:
#     a=input('请输入你的名字\n')
#     b=a.startswith('梁\n')
#     c=a.endswith('斌\n')
#     print(b,a,c)
# str = 'Runoob'
#
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# b='asd'
# c=123
# x='xc'
# a=f"12{x}34%s56%d789"
# print(a%(b,c))

# a='qw,ewre.ret'
# c=a.split(',')
# print(c)
# b= '+'.join(c)
# print()
# a='asdasdasdfasdfawqasdqw'
# # #b=a.replace(' ','')
# # print(a.index('as'))
# b=a.upper().replace('A','123')
# c=len(a)
# print('-'*5,'a','-'*5)
# a=123456
# b=len('a')
# print(b)
#整数
# a = 4
# print(type(a))
# a = [12,'qwewe',44,123,[12,4234,6546,676]]
# print(a.count(12))
# a = "151617"
# a=a.split('1')
# a='-'.join(a)
# print(a)
# a = (12,13,12,15,12,14,12)
# b=('qwasdas','dswqdasd')
# c=a+b
# print(c)
# a = ['ads','wqet',123,3412,12,13]
# b = ['dsadq',12,123,12,'asdad','tyhyujgh',123,]
# #a.extend(b)
# b.clear()
# print(b)
# print(a+b)
# b=a.index(12)
# print(b)

#a = {12,13,123,45}
# print(a)
# a.add(54)
# print(a)
# a.remove(12)
# print(a)
#b=a.pop()
#print(b)
# a.pop()
# print(a)
# a={'name':'斌斌','age':'20'}
# #a['sex']='男'
# #a['se']='女'
# print(a.items())
# for c,d in a.items():
#     print(c,d)
# a={'name':'斌斌','age':'20'}
# b={'sex':'men'}
# a.update(b)
# print(a)
#print(min([1,2,3,4,5]))
# a=[12,23,14,15]
# b=12
# c=b not in a
# print(c)
# a=input('请输入那你的名字')
# if a.startswith('lang') and a.endswith('bin'):
#     print('trule')
# else:
 #   print('fales')
# while True:
#     a=int(input('请输入成绩'))
#
#     if 90<=a<=100:
#         print('优秀')
#     elif 80<=a<90:
#         print('良好')
#     elif 60<=a<=80:
#         print('及格')
#     elif a<60:
#         print('不及格')
# # a='asdsad%sasdad%d'
# print(a%('qwe',123))
# while True:
#     a = int(input('>>>'))
#     if a%2==0 and a%3==0:
#         print('helloworld')
#     elif a%2==0:
#         print('hello')
#     elif a%3==0:
#         print('world')
#     else:
#         print('123')
# while True:
#     a=str(input('>>>'))
#     if (a.startswith('A') or a.startswith('a')):
#         if a.endswith('c'):
#             print('110')
#         elif a.startswith('a'):
#             print('120')
#         elif a.startswith('c'):
#             print(130)
#         else:
 #           print('250')
# a='abcd'
# for s in a:
#      for n in a:
#          print(n
# c=3
# for i in range(3):
#     a=int(input('>>>'))
#     import  random
#     b=random.randrange(10)
#     print(b)
#     if a>b:
#         print('赢')
#     else:
#         print('输')
#
#     count
    #    print(2)

# sum = 0
#
# for i in range(1, 10):
#     k = 2
#     if i >= 2:
#         while i % k != 0:
#             k += 1
#         if i == k:
#             sum += i
#             print(i)
# #print(sum)
# while True:
#     a=int(input('>>>'))
#     b=1
#     d=1
#     c=[]
#     while a>=b:
#         d=d*b
#         b+=1
#         #print('{}*{}'.format(b,b+1),end='')
#    # print(d)
#         c.append(d)
#     print(sum(c))
#     print(c)
        #print(c)
       # b+=1
#print(c)
#print(sum(c))
def 猜大小():
    import random
    a=random.randrange(10)
    #print(a)
    for i in range(3):
        b=int(input('>>>'))

        if b>a:
            print('猜大了还剩%d次'%(2-i))

        elif b<a:
            print('猜小了还剩%d次'%(2-i))
        elif b==a:
            print('猜对了')
            break
# a=0
# b=0
# while a<=100:
#     b+=a
#     print(a)
#     a+=2
#
# print(b)
# a=[12,12,12,16,18]
# b=[]
# for i in a:
#     if i
def chengji(*args):
    b=list(args)
    for i in b:
        if i>0:
            a = sum(b) / len(b)
            if i<a:
                print(i)
        else:
            break
    print(a)
def qwe(b,*args):
    a=list(args)
    b=int(b)
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j:
                if a[i]+a[j]==b:
                    print(a[j],a[i])
            else:
                break

#import random
#a=random.randrange(10)
# def zushuzi(*args):
#     if 0<=a<=9:
# a=[0,1,2,3]
# b=[]
# c=[]
# for i in a:
#     if i>0:
#         for j in a:
#             for s in a:
#                 if i!=j and i!=s and j!=s:
#                   #  print(i,j,s)
#                     b.append(i * 100 + j * 10 + s)
# for z in b:
#     if z not in c:
#         c.append(z)
# print(c)
# a=int(inp>>>'))
# if divmod(a,2)ut('=(i,j):
#     if i>2:
# a='1,1,1,0'
#
# b=''.join(a.split(','))
# print(b)
# import wang.函数
# wang.函数.xuanze(98,99,64,35,31,35,34,382,81,21)
# from wang.函数 import *
# a=int(input('>>>'))
# if a>15:
#     while a>=16:
#         c=a%16
#         a=a//16
#         print(c)
#         if a<10 and c<10:
#             print(a,c,end='')
#         elif a<10 and c>=10:
#             if a<10 and c==10:
#                 print(a,'a',end='')
#             elif a<10 and c==11:
#                 print(a,'b',end='')
#             elif a<10 and c==12:
#                 print(a,'c',end='')
#             elif a<10 and c==13:
#                 print(a,'d',end='')
#             elif a<10 and c==14:
#                 print(a,'e',end='')
#             elif a<10 and c==15:
#                 print(a,'f',end='')
#         elif a>=10 and c >= 10:
#             if a < 10 and c == 10:
#                 print(a, 'a', end='')
#             elif a < 10 and c == 11:
#                 print(a, 'b', end='')
#             elif a < 10 and c == 12:
#                 print(a, 'c', end='')
#             elif a < 10 and c == 13:
#                 print(a, 'd', end='')
#             elif a < 10 and c == 14:
#                 print(a, 'e', end='')
#             elif a < 10 and c == 15:
#                 print(a, 'f', end='')
# class Sweetpotato:
#     def __init__(self):
#         self.cookedLevel=0
#         self.cookedSting='生的'
#         self.condiments=[]
#     def __str__(self):
#         msg='地瓜的生疏程度：'+self.cookedSting
#         msg+='\n地瓜的等级：'+str(self.cookedLevel)
#         msg+='\n添加的作料是：'
#         for i in self.condiments:
#             msg+=i+','
#         msg=msg.strip(',')
#         return msg
#     def Cook(self,times):
#         self.cookedLevel+=times
#         if self.cookedLevel>8:
#             self.cookedSting='木炭'
#         elif self.cookedLevel>5:
#             self.cookedSting='烤好了'
#         elif self.cookedLevel>3:
#             self.cookedSting='半生不熟'
#         else:
#             self.cookedSting='生的'
#     def addcondiment(self,temp):
#         self.condiments.append(temp)
# d=Sweetpotato()
# d.Cook(3)
# d.Cook(5)
# d.addcondiment('辣椒')
# d.addcondiment('芥末')
# print(d)
# class Asd:
#     def qqq(self):
#         print(111)
#     def hanshu(self):
#         print(2222)
#
# class Student:
#     def __init__(self):
#         self.name='空的'
#     def  hanshu(self):
#         print(123)
# class Kkkk(Student):
#     pass
# class Qqq(Asd,Kkkk):
#     pass
# qq=Qqq()
# qq.hanshu()
# class Animal():
#     def talk(self):
#         pass
# class people(Animal):
#     def talk(self):
#         print('say hello')
# class pig(Animal):
#     def talk(self):
#         print('hengheng')
# class dog(Animal):
#     def talk(self):
#         print('汪汪')
# dog().talk()
# people().talk()
#方法重写
# class Student:
#     def hanshu(self):
#         print('你好')
# class KdStudent(Student):
#     def hanshu(self):
#         print('asdasdqwd')
# aa=KdStudent()
# aa.hanshu()
# class Home:
#     def __init__(self,newarea):
#         self.area=newarea
#         self.containsItems=[]
#     def __str__(self):
#         msg='家当前可用面积：'+str(self.area)+'平方米'
#         msg+='\n当前家具有：'
#         for i in self.containsItems:
#             msg+=i.name+','
#             msg=msg.strip(',')
#         return msg
#     def additems(self,item):
#         if self.area>item.area:
#             self.containsItems.append(item)
#             self.area-=item.area
# class Ded:
#     def __init__(self,newname,newarea):
#         self.name=newname
#         self.area=newarea
#     def __str__(self):
#         msg='床的面积为：'+str(self.area)+'平方米'
#         msg+='\n床的样式：'+self.name
#         return msg
#
# home=Home(100)
# print(home)
# ded=Ded('板床',4)
#
# print(ded)
# home.additems(ded)
# print(home)
# a='123456'
# print(a[::1])
# qwe(12,9,3,10,6,6,87,8,976,)
# a=[1,2,3,4]
# b=a[::-1]
# print(a)
# print(b)
chengji()