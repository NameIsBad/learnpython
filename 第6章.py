######################抽象############################

# ##6.3 自定义函数##
# import math
# x = 1
# y = math.sqrt
# print(callable(x)) ##callable 判断对象是否可调用 
# print(callable(y))
# def Hello(name):
#     return '你好！'+name
# n = input('请输入姓名：')
# print(Hello(n))
# def fibs(num):
#     result = [0,1]
#     for i in range(num-2):
#         result.append(result[-2] + result[-1])
#     return result
# f = fibs(20)
# print(f)

# ##6.3.1 给函数编写文档
# def square(x):
#     '计算平方'
#     return x * x;
# print(square.__doc__)
# help(square)

# ##6.3.2 其实并不是函数的函数
# def test():
#     print(1)
#     return
#     print(2)
# x = test() ##即使没有return值，但也会返回None。因此函数都会返回值的
# print(x)

# ## 6.4 参数魔法 ##

# ## 6.4.2 我能修改参数吗
# def  try_to_change(name):
#     name = '哈哈'
# name  = 'dujiadi'
# try_to_change(name) ##string和元组是不可变的，每次赋值相当于替换新值
# print(name)

# def try_to_chage_list(n):
#     n[0] = '美女'
# names = ['dujiadi','dukedi']
# try_to_chage_list(names) ##结果['美女', 'dukedi']，改变了值
# print(names)
# names = ['dujiadi','dukedi']
# new_names = names[:]
# print(names is new_names)
# print(names == new_names)
# try_to_chage_list(new_names)
# print(names)

#  #1为何要修改参数
# def init(data):
#     data['first'] = {}
#     data['middle'] = {}
#     data['last'] = {}

# def lookup(data,table,name):
#     return data[table].get(name)

# def store(data,full_name):
#     names = full_name.split()
#     if len(names) == 2 : names.insert(1,'')
#     lables = ['first','middle','last']

#     for lable,name in zip(lables,names):
#         people = lookup(data,lable,name)
#         if people :
#             people.append(full_name)
#         else:
#             data[lable][name] = [full_name]

# storage = {}
# init(storage)
# store(storage,'du jia di')
# store(storage,'du ke di')
# print(lookup(storage,'first','du'))
# print(lookup(storage,'middle','jia'))

#  #2.如果参数是不可变的
# def inc(x) : return x + 1;
# foo = 3
# inc(foo)
# print(foo) ## 3
# print(inc(foo)) ## 4
#  #改变一下
# def inc2(x) : x[0] = x[0] + 1
# foo = [3]
# inc2(foo)
# print(foo[0]) ##4

# ##6.4.3 关键字参数和默认值(默认情况下参数与名称无关，和顺序有关。如果指定参数名称则与名称有关和顺序无关))
# def hello_1(name,greeting) :
#     print('{},{}!'.format(name,greeting))
# def hello_2(greeting,name) :
#     print('{},{}!'.format(greeting,name))
# hello_1('杜佳迪','帅')
# hello_1('杜佳迪','帅')
# hello_1(name = '杜佳迪',greeting = '帅')
# hello_2(name = '帅',greeting = '杜佳迪')
# def hello_3(name='杜佳迪',greeting = '帅'):
#     print('{},{}!'.format(name,greeting))
# hello_3() ##有默认值

# ## 6.4.4收集参数
# def print_params(*params): ##类似C#的param[] param_name
#     print(params) ##('dujiadi', 'dukedi')
# print_params('dujiadi','dukedi')

# def print_params1(title,*params):
#     print(title)
#     print(params)
# print_params1('参数：','dujiadi','dukedi')
# print_params1('参数：') ##params参数将返回空元组

#  #*参数同样可以放在中间位置（调用时需要显式指定参数名）
# def print_params2(x,*y,z):
#     print(x)
#     print(y)
#     print(z)
# print_params2('x','y1','y2',z='z')
# ##print_params2('x','y1','y2') #要报错 z 为必传参数

#  #【**】可收集关键字参数
# def print_params3(**params):
#     print(params)
# print_params3(x = 1,y=2,z=3) ##{'x': 1, 'y': 2, 'z': 3}
# print(1,2,3) ##1 2 3

#  #高级写法
# def print_params4(x,y,z=3,*pospar,**keypar):
#     print(x,y,z)
#     print('pospar:{}'.format(pospar))
#     print('keypar:{}'.format(keypar))
# print_params4(1,2,3,4,5,6,7) ##123  pospar:(4, 5, 6, 7)  keypar:{}
# print_params4(1,2,3,4,5,6,7,foo = 1,bar = 2) ##123  pospar:(4, 5, 6, 7)  keypar:{'foo': 1, 'bar': 2}

# ##6.4.5 分配参数
# def add(x,y):
#     print(x+y)
# param = (1,2)
# add(*param) ##相反同样适用

# def test(name,age):
#     print('姓名：{},年龄:{}'.format(name,age))
# param = {'name':'杜佳迪','age':18}
# test(**param)

# ## 6.4.6 练习使用参数
# def story(**kwds):
#     print('姓名：{name}，年龄：{age}，长得真是{info}！'.format_map(kwds))
# story(name='杜佳迪',age = 18,info='帅')
# story(**{'name':'杜克迪','age':18,'info':'帅'})

# def power(x,y,*others):
#     if others:
#         print('others',others)
#     print(pow(x,y))
# power(2,3)
# power(3,2)
# power(x = 2, y =3)
# params = (5,)*2
# print(params)
# power(*params)
# power(3,3,'Hello')

# def interval(start,stop = None,step = 1):
#     '模拟range()步数大于0'
#     if stop is None:
#         start,stop = 0,start
#     result = []

#     i = start
#     while i < stop:
#         result.append(i)
#         i+=step
#     print(result)
# interval(10)
# interval(1,5)
# interval(3,12,4)

# ## 6.5作用域##
# params = '杜佳迪'
# def test(params):
#     print(params)
#     print(globals()['params']) ##函数内部参数如果和全局变量一样，用此方法来获取全局变量
# test('杜克迪')

#  #改变全局变量
# x = 1
# def change_global():
#     global x  ##明确告诉py它是全局变量
#     x = x +1
# change_global()
# print(x)
 
#  #作用域嵌套
# def multiplier(factor):
#     def multiplyByFactor(number):
#         return number * factor
#     return multiplyByFactor ##返回一个内部函数
# double = multiplier(2)
# print(double)
# result = double(5) ##调用的为 multiplyByFactor(number)
# print(result)

# ##6.6 递归
# ##6.6.1 阶乘和幂
# def factorial(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
# r1 = factorial(1)
# r2 = factorial(3)
# print(r1,r2)

# def factorial1(x):
#     if x == 1:
#         return 1
#     return x * factorial1(x -1)
# r1 = factorial1(1)
# r2 = factorial1(3)
# print(r1,r2)
#  #幂
# def pow(x, y):
#     if x == 0:
#         return 1
#     return x * pow(x,(y-1))

# ##6.6.2 二分查法 模块bisect提供了标准二分查找实现
# def search(sequence, number,lower = 0,upper = None):
#     if upper is None: upper = len(sequence) - 1
#     if lower == upper:
#         assert number == sequence[upper]
#         return upper
#     else:
#         middle = (lower + upper ) // 2
#         if number > sequence[middle]:
#             return search(sequence,number,middle+1,upper)
#         else:
#             return search(sequence,number,lower,middle)

# seq = [34,67,8,123,4,100,95]
# seq.sort()
# print(seq)
# s1 = search(seq,100)
# print(s1)

#  #函数式编程 map filter reduce
l1 = list(map(str,range(10)))
print(l1)
# l2 = [str(i) for i in range(10)]
# print(l2)

#  #filter
# def test(x):
#     return x.isalnum()
# seq = ['foo','bar','re32','##','#$%','@$#dfs32']
# seq1 = list(filter(test,seq))
# print(seq1)

#  #filter==列表推导,列表推导 不用创建自定义函数了
# seq = ['foo','bar','re32','##','#$%','@$#dfs32']
# l3 = [str(i) for i in seq if i.isalnum()]
# print(l3)

#  #lambda
# seq = ['foo','bar','re32','##','#$%','@$#dfs32']
# l4 = list(filter(lambda x:x.isalnum(),seq))
# print(l4)

#  #lambda + reduce 计算列表的和. reduce详解：https://www.cnblogs.com/lonkiss/p/understanding-python-reduce-function.html
# numbers = [91,54,159,13,15,4,489,453,4,1,65,7,6,786,46,44]
# from functools import reduce
# sum1 = reduce(lambda x,y:x + y,numbers)
# print(sum1)
