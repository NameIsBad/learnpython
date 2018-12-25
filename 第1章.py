# x = input("x:") #接受输入值
# y=input("y:")
# print(int(x)*int(y))
# if x=="1" :print("牛逼") #if语句
# if x=="2" : print("傻逼")
# if 1==1 : print("牛逼")
# if 1!=2 : print("傻逼")

# import math #引用模块
# x = math.floor(32.9)
# print(x)

# from math import sqrt #引用模块 此方式调用函数时不用些模块前缀 此种方式容易和未知模块函数冲突 非完全确认情况尽量不用
# print(sqrt(10))
# print(sqrt(-10)) #错误

# import cmath
# print(cmath.sqrt(-10)) #上面报错处理方法

# name = input("who are you?")
# print("fuck,"+name)

# #画三角形（海龟绘图法）#
# from turtle import *
# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)

# penup()
# right(60)
# forward(300)
# pendown()
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# input("Press <enter>")

# print('who'' are you?') #原始字符(变量不行)拼接可省略+号
# x = 'who'
# y = ' are you?'
# print(x y) #报错

# #转移符用法
# print('你好，\n朋友')
# print('D:\nowhere')
# print('D:\\nowhere')
# print(r'D:\nowhere') #r原始字符串 正则 路径等
# print(r'Les\'s go')  #引号需要转义
# print(r'D:\Program Files\Python''\\')

# #Unicode 字符描述参阅：http:unicode-table.com
# print('\u00c6')
# print('\U0001F60A')
# print('这是一只猫：\N{Cat}')
# print('这个字符串的长度是？'+ str(len("这个字符串的长度是？".encode("UTF-8"))))

# print('这个字符串的长度是？'+ str(len("这个字符串的长度是？".encode("UTF-32"))))