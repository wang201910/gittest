#!/usr/bin/python
#-*-coding:utf-8-*-
# import wang.wew
#wang.wew.jiujiu()
#wang.wew.点名()
# def hanshu(a,b='qwas',*args,**kwargs):
#     print(a, b,*args,kwargs)
#     # a=int
#     # b=str
#     # c=set
#
#     # print(b)
#     # print(c)
# hanshu('12321',2321,12,3213,4,234353,5436,46,436,3,k=1232)
def zhishu(a,b):
  #  a=int(input('>>>'))
  #  b=int(input('>>>'))
    c=0
    if b>a:
        for i in range(a,b):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
               # print(i)
                c+=i
        print(c)
def yinshu(a,c=0):
    for i in range(1,a+1):

        if a%i==0:
            c+=i
    print(c)
def shuixianhua(a,b):
    for i in range(a,b):
        c=i//100
        d=i//10%10
        e=i%10
        if c**3+d**3+e**3==i:
            print(i)
def xuanze(*args):
    b=list(args)
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            if b[i]>b[j]:
                b[i],b[j]=b[j],b[i]
                print(b)
    print(b)
def maopao(*args):
    b=list(args)
    for s in range(len(b)):
        for i in range(len(b)):
            for j in range(i+1,len(b)):
                if b[i]>b[j]:
                    b[i],b[j]=b[j],b[i]
                    break
    print(b)
def jiecheng(a,b=0):
    for i in range(1,a+1):
        c=1
        for j in range(1,i+1):
            c=c*j
            print(c)
        b+=c
    print(b)
def quchong(*args):
    b=[]
    c=list(args)
    for i in c:
        if i not in b:
            b.append(i)
    print(b)
    return b
# def hanshu():
#     def han(x,y):
#         a=x+y
#         return a
#     return han
# a=hanshu()
# print(a(2,3))
# a=lambda x,y:('大于')if x>y else ('小于')
# print(a(6,5))
import random
# a=['%d*%d=%d'%(i,j,i*j) for i in range(1,10) for j in range(1,i+1) ]
# print(a)
# if __name__ == '__main__':
#     print('hello')
def mai():
    for i in range(34):
        for j in range(101):
            for s in range(100):
                if 2*i+j+0.5*s==100 and i+j+s==100:
                    print('公鸡有%d 母鸡有%d 小鸡有%d'%(i,j,s))
def hhhh(a):
    print(a)
def chengji(*args):
    b=list(args)
    for i in b:
        if i>0:
            a = sum(b) / len(b)
            if i<a:
                print(i)
        else:
            break
    assert  a==1060
# try:
#    a=[12,323,4,234]
#    a.split(',')
# except Exception as e:
#     print(e)
# a=(input(''))
# print(a.endswith('s'))
# i=int(input('>>>>'))
# # if i<=100000:
# #     a=i*0.1
# #     print(a)
# # elif 100000<i<=200000:
# #     print(10000+(i-100000)*0.075)
# # elif 200000<i<=400000:
# #     print(17500+(i-200000)*0.05)
# # elif 400000<i<=600000:
# #     print(27500+(i-400000)*0.03)
# # elif 600000<i<=1000000:
# #     print(33500+(i-600000)*0.015)
# # elif 1000000<i:
# #     print(39500+(i-1000000)*0.01)
# class Cat:
#     def __init__(self,newweiba,newcolor):
#         self.qwe=newweiba
#         self.qqq=newcolor
#
#     def __str__(self):
#         self.msg='有没有尾巴：'+self.qwe+'颜色'+self.qqq
#         return self.msg
# xiaoBaiMao=Cat('有','黑色')
# print(xiaoBaiMao)
# with open(r'1111.txt','r',encoding='utf-8') as a:
#     b=a.readlines()
#
#     import xlwt
#     xl=xlwt.Workbook(encoding='utf8')
#     sheet=xl.add_sheet('python_test')#添加一个标签页（括号里的是标签名可以随意)
#     for i in range(len(b)):

#         for j in range(len(b)):
#             for c in b:
#         # print(i)
#                 sheet.write(i,j,c)#向标签里添加内容，第一是行，第二是列，第三个是写入的内容
    # xl.save('a.xls')
# import xlrd
# xr=xlrd.open_workbook('a.xls')#打开我们要操作的文件，括号里的是文件名或路径
# #获取所有标签页
# a=xr.nsheets#获取总共有多少个标签页
# print(a)
# sheet=xr.sheets()[0]#通过索引来进入操作的标签页
# hangshu=sheet.nrows#获取标签页中有多少行
# print(hangshu)
# #2，通过名称来进入我们要操作的标签页
# name=xr.sheet_names()#获取所有标签页的名称
# print(name)
# sheet=xr.sheet_by_name('python_test')
# hangshu=sheet.nrows#获取标签页中有多少行
# print(hangshu)
# hang3=sheet.row_values(2)#获取标签页的第几行
# lieshu=sheet.ncols #获取标签页中有多少列
# lie3=sheet.row_values(2)#获取标签页中第几列的内容
# gezi=sheet.cell().value获取一个格子里的内容
# with open('1111.txt','r',encoding='utf8') as b:
#         import xlwt
#         xl = xlwt.Workbook(encoding='utf-8')
#         a=xl.add_sheet('121')
#         c=0
#         for i in b.readlines():
#             a.write(c,0,i)
#             c+=1
# xl.save('a.xls')
# import xlwt
# x=xlwt.Workbook(encoding='utf8')
# d=x.add_sheet('123')
# for g in range(1,10):
#     for h in range(1,g+1):
#         d.write(g-1,h-1,f'{h}*{g}={g*h}')
# x.save('c.xls')
# with open('123.txt','w',encoding='utf8') as s:
#     import xlrd
#     xr=xlrd.open_workbook('b.xls')
#     k=xr.sheets()[0]
#     v=xr.sheet_by_name('123')
#     p=[]
#     for j in range(k.nrows):
#         for z in range(j+1):
#             l=v.cell(j,z).value
#             s.write(l+' ')
#         s.write('\n')
import copy
# if __name__=='__main__':
#     a=[23,46,45,65,12]
#     j=a.copy()
#     a.sort()
#     b=a[-1]
#     c=a[0]
#     j.remove(c)
#     j.remove(b)
#     j.insert(0,c)
#     j.append(b)
#     print(j)
# import xlrd
# import xlwt
# with open('1111.txt','w',encoding='utf8') as a:
#     a.write(('a,b,c'+'\n')*10)
# with open('1111.txt','r',encoding='utf8') as a:
#     xl=xlwt.Workbook(encoding='utf8')
#     b=xl.add_sheet('123')
#     for i ,s in enumerate(a.readlines()):
#         s=s.split(',')
#         for j,m in enumerate(s):
#             b.write(i, j, m)
#     xl.save('b.xls')
# with open('111a.txt','w',encoding='utf8') as a:
#     rd=xlrd.open_workbook('b.xls')
#     aa=rd.sheet_by_name('123')
#     hangshu=aa.nrows
#     for i in range(hangshu):
#         h=','.join(aa.row_values(i))
#         a.write(h)
# b=0
# for i in range(3):
#     print('c')
#
#     if i==1:
#         print('a')
#         continue
#
#     # print('c')
# else:
#     print(b)
# a=['a','b','c']
# b=['x','y','z']
# c=[]
# for i in a:
#     for j in b:
#         c.append(i+j)
# for l in c:
#     if l=='ax' or l=='cx'or l=='cz':
#         c.remove(l)
# print(c)
zhishu(2,100)
