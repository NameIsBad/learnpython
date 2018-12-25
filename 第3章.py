######################字符串############################

# ##3.1字符串基本操作##
# ###字符串是不可变的，索引，切片，乘法，成员资格检查(in)，长度，最小值和最大值都使用与字符串
# ###但由于字符串是不可变的，所以赋值操作都是非法的
# website = 'http://www.python.com'
# website[-3:] = 'cn' #报错

#########################################################################################################################

# ##3.2设置字符串的格式：精简版##
# formatStr = 'Hello,%s。你真的很%s！'
# values = ('杜佳迪','帅')
# print(formatStr % values)
# ##利用模板
# from string import Template
# tmpl = Template('Hello,$name!你真的很$description!')
# tmplStr = tmpl.substitute(name = '杜佳迪',description = '帅')
# print(tmplStr)
# ##format方法
# formatStr = 'Hello,{},你真的很{}!'.format('杜佳迪','帅')
# print(formatStr)
# formatStr = 'Hello,{0},你真的很{1}!'.format('杜佳迪','帅')
# print(formatStr)
# formatStr = 'Hello,{1},你真的很{0}!'.format('杜佳迪','帅') ##顺序不一定为0,1,2
# print(formatStr)
# from math import pi
# formatPiStr = '{name} 的值大约是{value:.2f}'.format(name='π',value=pi) ##指定格式
# print(formatPiStr)
# ##3.6新语法
# print(f'π的值大约是{round(pi,2)}') #与C#7.1中的【$"{}"】用法一样

#########################################################################################################################

# ##3.3设置字符串的格式：完整版##
# mixFormat = '{name},今年{}岁,而且很{},对吗？{descript}!'.format(18,'帅',name='杜佳迪',descript='对')
# print(mixFormat)
# fullName = ['dukedi','dujiadi']
# print('{name[1]},很帅！'.format(name = fullName))
# import math
# tmpl = 'The {mod.__name__} module defines the value {mod.pi} for π'
# tmplStr = tmpl.format(mod = math)
# print(tmplStr)

# # ## 3.3.2基本转换
# print('{pi!s},{pi!r},{pi!a}'.format(pi = 'pi'))
##宽度、精度、千位分隔符
# print('！！{num:10}！！'.format(num = 3))
# print('！！{name:10}！！'.format(name = '杜佳迪'))
# import math
# print("!!{pi:10.2f}!!".format(pi = math.pi))
# print("!!{:.5}!!".format("dujiadi shuai"))
# print('my money is {:,}'.format(10 ** 1000)) ##千位分隔符

# ## 3.3.3 符号、对齐和用0填充
# from math import pi
# print('{:022.2f}'.format(pi))
# print('!!{0:<10.2f}!!\n!!{0:^10.2f}!!\n!!{0:>10.2f}!!'.format(pi))
# print('{:$^9}'.format(' hello '))
# print('!!{0:10.2f}!!\n!!{1:10.2f}!!'.format(pi,-pi))
# print('!!{0:10.2f}!!\n!!{1:=10.2f}!!'.format(pi,-pi))  ##'='号将填充字符放在符号和数据之间
# print('{0:-.2f}\n{1:-.2f}'.format(pi,-pi)) ##默认符号为 -，结果第一个没'+'符号
# print('{0:+.2f}\n{1:+.2f}'.format(pi,-pi))
# print('{0: .2f}\n{1: .2f}'.format(pi,-pi))
# ## 示例
# header_fmt = '{{:{}}}{{:>{}}}'.format(10,20) ##结果{:10}{:>20} '{{'最终显示为'{'
# print(header_fmt)

#########################################################################################################################

##3.4字符串方法##
# ## string模块##
# import string
# print(string.digits) ##0~9常量
# print('\n')
# print(string.ascii_letters)
# print('\n')
# print(string.ascii_lowercase)
# print('\n')
# print(string.printable)
# print('\n')
# print(string.punctuation)
# print('\n')
# print(string.ascii_uppercase)

# ## 3.4.1 center
# print('杜佳迪，帅！'.center(10))
# print('杜佳迪，帅！'.center(10,'*'))
# print('杜佳迪，帅！'.ljust(10))
# print('杜佳迪，帅！'.ljust(10,'*'))
# print('杜佳迪，帅！'.rjust(10))
# print('杜佳迪，帅！'.rjust(10,'*'))
# print('杜佳迪，帅！'.zfill(10))

# ## 3.4.2 find（rfind(向右边查),index,rindex(向右边查),count,startwith,endwith）
# str_test = '杜佳迪很帅！'
# print(str_test.find("佳迪")) ##返回索引
# print(str_test.find("丑")) ##不存在 -1
# print(str_test.index("佳迪")) ##不存在会报错
# print(str_test.find('佳迪',2,3)) ## 2,3参数为：查找的起始位置和结束位置

# ## 3.4.3 join (与spit相反)
# sep = [1,2,3,4,5]
# print('+'.join(map(str,sep)))
# sep = ['1','2','3','4','5']
# print('+'.join(sep))
# dirs = '','usr','bin','env'
# print('\\'.join(dirs))

# ## 3.4.4 lower
# print('DUJIADI'.lower())
# print('DUJIADI'.islower()) ##所有字符都为小写则返回true，否则为false
# print('dujiadi'.islower())
# print('Dujiadi'.istitle()) ##首字母大写？
# print('dujiadi'.isupper())
# intab = "aeiou"
# outtab = "12345"
# deltab = "thw"
# trantab1 = str.maketrans(intab,outtab) # 创建字符映射转换表
# trantab2 = str.maketrans(intab,outtab,deltab) #创建字符映射转换表，并删除指定字符
# test = "this is string example....wow!!!"
# print(test.translate(trantab1))
# print(test.translate(trantab2))

# ## 3.4.5 replace
# print('杜佳迪很丑！'.replace('丑','帅'))
# print('杜佳迪很丑，不丑丑丑！'.replace('丑','帅',1))

# ## 3.4.6 split
# str_test = '1+2+3+4+5'
# print(str_test.split('+')) ##参数默认为空格

# ## 3.4.7 strip lstrip rstrip
# print('   杜佳迪很帅！  '.strip()) ##trim()
# print('*****杜佳迪很帅！**！*!*！'.strip('*！!'))

# ## 3.4.8 translate 转换表
# table = str.maketrans('杜佳迪','大帅哥')
# print(table) ##打印出来是Unicode码点之间的映射
# print('杜佳迪哈哈，杜，你好！佳，不错！迪，厉害'.translate(table))

## 3.4.9
#isspace、isdigit（是否为数字）、isupper（是否为大写）
