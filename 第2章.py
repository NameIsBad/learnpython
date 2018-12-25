# ##2.2.1索引##
# 'Beautiful'[0]
# 'Beautiful'[-1] #从右边第一个(最后一个元素)开始

# ##将以数指定年月日的日期打印出来##
# months = ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
# endings = ['st','nd','rd'] + 17 * ['th'] \
#           + ['st','nd','rd'] + 7 * ['th'] \
#           + ['st']

# year = input('年:')
# month = input('月:')
# day = input('日:')

# month_number = int(month)
# day_number = int(day)

# print(year + '年' + months[month_number] + day + endings[day_number])

# ##2.2.2切片##
numbers = [1,2,3,4,5,6,7,8,9,10]
# n1 = numbers[3:6]
# print(n1)
# n2 = numbers[7:10]
# print(n2)
# n3 = numbers[3:100]
# print(n3)
# tag = '<a href="http://www.python.org">Python web site</a>'
# url = tag[9:30]
# print(url)

# ## 1.绝妙的简写
# print(numbers[-3:-1])
# print(numbers[-6:-2]) ##负数索引从-1开始？
# print(numbers[-3:0])  ##0不嗯那个包括最后一个，因为-3在0后面，而Python的切片第一个索引指定的元素位置要在第二个前面
# print(numbers[-3:])  ##切片结束于序列末尾，可省略第二个索引参数
# print(numbers[:4])
# print(numbers[:])  ##都为空则为所有

# ## 2.步长
print(numbers[0:10:1]) ##默认最后一个参数为1
print(numbers[0:10:2]) ##[1, 3, 5, 7, 9]
print(numbers[::4])
print(numbers[8:3:-1]) ##负数时将向左提取，结果为：[9, 8, 7, 6, 5]
print(numbers[::-1])
print(numbers[::-2])

#########################################################################################################################

# ##2.2.3序列相加##
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# print(l1 + l2)
# print("HELLO,"+"Python!")
# print(l1+"HELLO")  ##报错，一般而言，不能拼接不同类型的序列

# ##2.2.4序列乘法##
# ls1 = 'NB' * 6
# print(ls1)
# ls2 = [1,2,3] * 10
# print(ls2)
# lsNone = [None] * 10 #None代表Null
# print(lsNone)
# sentence = input("Sentence: ")
# screen_width = 80
# text_width = len(sentence)
# box_width = text_width + 6
# margin_width = (screen_width - box_width)//2
# print()
# print(' ' * margin_width + '+' + '-' * (box_width - 2) + '+')
# print(' ' * margin_width + '|' + ' ' * (box_width - 2) + '|')
# print(' ' * margin_width + '|' + ' ' * 2 + sentence + ' ' * 2 +  '|')
# print(' ' * margin_width + '|' + ' ' * (box_width - 2) + '|')
# print(' ' * margin_width + '+' + '-' * (box_width - 2) + '+')
# print()
# ##书上例子不知道为什么不对。。。
# print(' ' * margin_width + '+'  + '-' * (box_width - 2) + '+')
# print(' ' * margin_width + '| ' + ' ' * text_width     + ' |')
# print(' ' * margin_width + '| ' +       sentence       + ' |')
# print(' ' * margin_width + '| ' + ' ' * text_width     + ' |')
# print(' ' * margin_width + '+'  + '-' * (box_width - 2) + '+')

#########################################################################################################################

# ##2.2.5成员资格##
# permissions = 'rw'
# print('w' in permissions)
# print('a' in permissions)
# users = ['du','zhao','qian','sun']
# print('du' in users)
# print('li' in users)
# subject = '$$$ Get Money! !!!'
# print("$" in subject)
# print("$$$" in subject)
# user_password = [
#     ['du','123'],
#     ['zhao','456'],
#     ['qian','789']
# ]
# userName = input('用户名：')
# password = input('密码：')
# if [userName,password] in user_password : print('succeed') 
# else : print('fail')

#########################################################################################################################

# ##其他函数##
# numbers = [100,120,140]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(max(1,2,3,44,34))
# print(min(323,43,1,3))

#########################################################################################################################

# ##2.3列表##
# list1 = list('Hello')
# print(list1)
# print(''.join(list1))
# print(','.join(list1))

# ###2.3.2###
# ## 1.给元素赋值
# x = [1,2,3,4,5,6,7,8,9]
# x[1] = 100 ##给元素赋值
# x[2] = '32'##可以赋其他类型的值，没类型安全

# ## 2.删除元素
# x = [1,2,3,4,5,6,7,8,9]
# del x[0]
# print(x)

# ## 3.给切片赋值
# x = [1,2,3,4,5,6,7,8,9]
# x[3:5] = [100,200]
# print(x)
# x[3:5] = [100,200,200,200,200,200,200,200,200,200] ##数量可以不一样
# print(x)
# qlist = list('python')
# qlist[2:] = list('NETCORE')
# print(qlist)
# x[1:1] = [10,11,12,13] ##由于[1:1]序列为None，所以此赋值为在索引为1的后面添加元素
# print(x)
# x[1:10] = []  ##实际为删除操作，等：del x[1:10]
# print(x)

# ###2,3,3列表方法###
# mlist = [1,2,3,4]

# ## 1.append
# mlist.append(5)
# print(mlist)