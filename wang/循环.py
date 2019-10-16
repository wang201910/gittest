#!/usr/bin/python
#-*-coding:utf-8-*-
# a=[12,34,123,4545,23,123,['qweq','wqeq','qweqw',123],'qweqw','qweqweas']
# for s in a:
#     print(a[6])
# a=0
# # b=0
# # for s in range(101):
# #     if s%2!=0:
# #         a+=s
# #     else:
# #         b+=s
# # print(a)
# # print(b)
# a=[12,13,14,54,465,3432]
# for a in enumerate(a):
#     print(a)
# a={'name':'sdas','age':12,'sex':'man'}
# for s,n in a.items():
#     print(s,n)
# a=[23,43,33,52,12,13,25]
# for s in a:
#     if s<25:
#         continue
#     else:
#        print(1232)
# a='abcd'
# # for s in a:
# #     print('asdwq')
# # else:
# #     print('asds')
# while True:
#     for s in range(int(input('>>>'))):
#         a={'a','b','c','d'}
#         print(a.pop())
# import random
# a=random.randrange(10)
# for i in range(3):
#     c=
#     print(a)print('asdawerfeasfkiopklm,bnhghh')
# print('aaaaaaaaaaaaaaaaaaaaaaaaaaaqqqqqqqqqqqqaaaaaaaaaaaaaazsdafdsadqdqwdsadasdwqdswdsaffasdfsadqwdwqdasdqwdasdasdqwdsadesdasdqwdsadqwdasdqwdaaaaaaaaaaaaaaaaaaaaaakjjhjhjhhhhhhhhhhhhhhhhhhhdwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
# print()
#                                                                                               a=0w
# a=0
# while a<3:
#     a+=1
# continue
    # print('你好')
    # if a>1:
    #     print('中国')
    # else:
    #     print('河南')
    # a+=1
# else:
#     print('结束')
# a=0
# # b=0
# while a<3:
#     b=0
#     a+=1
#     while b<3:
#         b+=1
#         print('你好')
# a=0

#while a<1:
    # a+=1
# b=0
# while b<3:
#  b+=1
#  print('* '*b,end=' ')
#  print()
# i=0
# while i<3:
#     j=4
#     while j>i+1:
#         j-=1
#         print('*',end=' ')
#     print()
#     i+=1
# a = 0
# for i in range(100):
#     for j in range(100):
#         if i%j!=0:
#             #a+=i
#         print(a)
## else:
#     print('请重新输入')
# e=[]
# b=[]
# for c in range(10):
#     import random
#     a=random.randrange(20)
#     e.append(a)
# print(e)
# for r in e:
#     if r not in b:
#         b.append(r)
# #print(b)
#         for s in range(10):
#             for x in range(s+1,10):
#                 if b[s]>b[x]:
#                  b[s],b[x]=b[x],b[s]
#
#print(b)
#z='sdasdsf'
#print(z.strip('sf'))
#a=int(input('>>>'))
# a=0
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         a+=i
#         print(i)
# print(a)
# i=0
#
# while i<9:
#     i+=1
#     j=0
#     while j<i:
#         j+=1
#        # i+=1
#     #print(j)
#     #print(i)
#         print('{}*{}={}'.format(j,i,i*j),end=' ')
#     print()
#         #j+=1
# #print(e)
# a=input('>>>').split(',')
# b=[]
# for j in a:
#      j=int(j)
#      b.append(j)
# # print(b)
# print(b)
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10%10
#     if a**3+b**3+c**3==i:
#         print(i)
# a=[]
# b=int(input('>>>'))
# for i in range(1,b+1):
#     if b%i==0:
#         a.append(i)
# print(sum(a))
# a=[25,24,35,0,12,36,48,67,89,78,45]         #  i=0 j=1 [24,25,35,0] j=2 [24,25,35,0] j=3 [24,25,0,35]
#                        i=1  j=1 [24,25,0,35]  j=2 [24,0,25,35] j=3[24,0,25,35]
                       #  i=2
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#     print(a)
'''
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        #print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)
'''
def nian():
    y=int(input('年:\n'))
    m=int(input('月:\n'))
    d=int(input('日:\n'))
    i=0
    a=[0,31,59,90,120,151,181,212,243,273,304,335]
    if 1<=m<=12:
        i=a[m-1]+d
    else:
        print('请重新输入')
    if y%400==0 or y%4==0 and y%100!=0:
        if m>2:
            print('第%d天'%(i+1))
        else:
            print('第%d天'%(i))
    else:
        print('第%d天' % (i))


# d=[]
# e=[]
# z=''
# k=''
# j = int(input('请输入金额:'))
# e.append(j)
# v=int(input(''))
# while z!='1':
#     b = []
#     c = []
#     while True:
#         while True:
#             a = [['电视', 3900], ['电脑', 4999], ['手机', 4000]]
#             print(a)
#             i = int(input('请选择商品（退出选择请输入负数）:\n'))
#             if 0<=i<len(a):
#                 c.append(i)
#                 b.append(a[i])
#             else:
#                 break
#         print(b)
#         while True:
#             l=int(input('请输入要删除的商品（退出删除请输入负数）：\n'))
#             if l>=0:
#                 b.pop(l)
#                 c.remove(l)
#                 print('删除成功')
#             else:
#                 break
#         print(b)
#         p=input('是否确认购买(请输入是或否)')
#         if p=='是':
#             for s in c:
#                 d.append(a[s][1])
#             if sum(e)>=sum(d):
#                 print('购买成功')
#                 print('你还剩%d元'%(sum(e)-sum(d)))
#
#             else:
#                 while sum(e) < sum(d):
#                     print('请充值')
#                     f=int(input('请输入金额：\n'))
#                     e.append(f)
#                     print(e)
                    # if sum(e)>=sum(d):
                    #      print('购买成功')
                    #      print('你还剩%d元'%(sum(e)-sum(d)))
# z = input('是否继续购买？（按任意键继续购买输入1退出）\n')

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
#     print('第%d天' % (i))
# aa=input('>>>')
# b = []
# c = []
# for i in aa:
#     if i not in b:
#         b.append(i)
# for l in b:
#     a = aa.count(l)
#     print(f'{l}有{a}个')
#     c.append(a)
# a=[23,13,14,11,6,4]
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[j]<a[j-1]:
#             a[j-1],a[j]=a[j],a[j-1]
# print(a)
# a=[23,13,14,11,6,4]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

















