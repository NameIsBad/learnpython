######################条件、循环及其他语句############################

# ##5.1 再谈print和import##
# print('你好','dujiadi','今年',18,'岁了！',sep='_',end='&&')
# print('没换行')

##5.2 魔法赋值##

# ##5.2.1 序列解包
# x,y,z = 1,2,3
# print(x,y,z,sep=',')
# x,y = y,x ##666666
# print(x,y,z,sep=',')
# values = 3,2,1
# x,y,z = values
# print(x,y,z,sep=',')

dic = {'name':'dujiadi','age':18}
key , value = dic.popitem()
print(key,value)
key , value = dic.popitem()
print(key,value)
print('dic的值',dic)

# #x,y,z = 1,2,3,4 ##数量不匹配要报错
# a,b,*c = 1,2,3,4 ##c会把剩下的一起赋值 c = [3,4]
# print(c)
# name = 'dujiadi 太 帅 了'
# a,*b,c = name.split() ##b=['太', '帅']
# print(b)
# name = 'dujiadi 很 帅'
# a,*b,c = name.split() ##b扔为list b=['很']
# print(b)

# ##5.2.2 链式赋值
# x = y = 1
# print(x,y)

# ##5.2.3 增强赋值
# x = 2
# x+=1
# print(x)
# x*=2
# print(x)

# s = 'foo'
# s += 'bar'
# print(s)
# s *= 2
# print(s)

# ##5.4条件和条件语句

# ##5.4.1
# print(True+1) ##True为1 False0
# print(False+1)
# print(True+False+2)
# print(bool('有值'))
# print(bool(''))
# print(bool(0))
# print(bool({}))
# print(bool([]))
# print(bool(()))

# ##5.4.2、3、4
# name = input('what\'s your name?');
# if name.endswith('dujiadi'):
#     print("你很帅！")
# else:
#     print('你是谁？')
# status = '你是真的帅！' if name.endswith('dujiadi') else '你是哪个？' ##三目运算
# print(status)
# num = input('输入一个数字:')
# if num == '1': 
#     print('第一')
# elif num == '2':
#     print('第二！')
# else:
#     print('垃圾！')

# ##5.4.6 更复杂的条件
# '''
# x == y; 
# x < y; 
# x > y ; 
# x <= y ; 
# x >= y ; 
# x != y ; 
# x is y ;
# x is not y;
# x in y ;
# x not in y;
# '''
#  #is
# x = y = [1,2,3]
# z = [1,2,3]
# print(x == y)
# print(x == z) 
# print(x is y)
# print(x is z) ##false is判断的是引用 ==判断是值；不要将is用于数和字符串等不可变的基本值，结果不可预测（鉴于python内部处理对象的方式）
#  #in
# name = '杜佳迪真的帅！'
# if '杜佳迪' in name:
#     print('帅！')
# else:
#     print('丑')
# print('abc'<'def')
# print('a'<'B') ##大写与小写需要区分，此处返回False
# print('a'.lower() < 'B'.lower())
#  #布尔值运算
# number = int(input('输入一个数：'))
# if number>1 and number<=10: ##and(&&) or(||)
#     print('厉害')
# else:
#     print('垃圾')

# ##5.4.7 断言(可对某些位置添加限制条件，直接导致报错)
# age = 10
# assert 0 < age <=130
# age = -1
# assert 0 < age <=130,'年龄不在0-120之间，骗鬼呢？'

# ##5.5循环##

# ##5.5.1 while循环
# x = 1
# while x<=10:
#     print(x)
#     x+=1
# name = ''
# while not name :#and name.isspace() and name.strip():
#     name = input('请输入名称：')
# print('你好，{}'.format(name))

# ##5.5.2 for循环
# words = ['du','jia','di','shuai']
# for word in words:
#     print(word)
# for n in range(0,10): ##range(start,end) 内置数字循环
#     print(n)
# print(list(range(0,10)))

# ##5.5.3 迭代字典
# d = {'x':1,'y':2,'z':3}
# for k in d:
#     print(k,d[k],sep='=')

# ##5.5.4 一些迭代工具
#  #1.并行迭代
# names = ['dujiadi','dukedi','duyou']
# ages = [18,19,21]
# for i in range(len(names)):
#     print("{}的年龄是{}".format(names[i],ages[i]))
# print(list(zip(names,ages)))
# for name,age in zip(names,ages): ##zip函数 以最小数量序列为准
#     print('{}的年龄是：{}'.format(name,age))
# print(list(zip(range(5),range(100000)))) ##结果为：[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

#  #2.迭代时获取索引
# names = ['dujiadi','dukedi','duyou']
# for index,name in enumerate(names):
#     if 'you' in name:
#         names[index] = '杜佳迪'
# print(names)

# #3.反向迭代和排序后再迭代
# names = ['dujiadi','dukedi','duyou']
# for name in sorted(names,key = str.lower,reverse = True):
#     print(name)
# for name in reversed(names):
#     print(name)

# ##5.5.5 跳出循环
#  #1.break
# from math import sqrt
# for n in range(99,0,-1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break
#  #2.continue
# for n in range(10):
#     if n%2 == 0: