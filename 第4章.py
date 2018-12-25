######################字典############################

# ##4.2创建和使用字典(key必须唯一)##
# phonebox = {'dujiadi':'18088888888','dukedi':'18888888888','wangxiaoqing':'16666666666'}
# print(phonebox['dujiadi'])

# ##4.2.1 函数 dict（类。可把其他映射类型转换为字典）##
# items = [('name','dujiadi'),('age',18)]
# d = dict(items)
# print(d)
# print(d['name'])
# d = dict(name= 'dujiadi',age = 19)
# print(d['age'])
# print({})  ##空字典

# ##4.2.2 基本的字典操作 键的类型可以是任何不可变的类型
# d = {'name':'dujiadi','age':18 ,'info':'帅'}
# print(len(d))
# d['info'] = '很帅'
# print(d['info'])
# del d['info']
# if('age' in d) :
#     print('存在【age】键')
# else :
#     print('不存在【age】键')
# d['add'] = '键不存也可以直接赋值'
# print(d['add'])

# ##4.2.3 将字符串格式设置功能用于字典
# phonebox = {'dujiadi':'18088888888','dukedi':'18888888888','wangxiaoqing':'16666666666'}
# s = 'dukedi的号码是{dukedi}'.format_map(phonebox)
# print(s)
# s = 'dukedi的号码是{dukedi},第二个dukedi的号码是{dukedi}'.format_map(phonebox)
# print(s)

# ##4.2.4 字典方法
#  #clear copy（浅复制） deepcopy(深复制)
#  #fromkeys
# createDic = {}.fromkeys(['name','age']) ##同时创建多个key，值都为None
# print(createDic)
# createDic =dict.fromkeys(['names','ages'],'haha') ##一般用此方法创建,第二个参数值都为'haha'
# print(createDic)
#  #get(用键值获取字典时候，如果key不存在会报错，get方法不会报错)
# newDic = dict.fromkeys(['name','age'])
# # print(newDic['info']) ##会报错
# print(newDic.get('info')) ##没有返回None
# print(newDic.get('info','帅')) ##可给默认值
#  #items
# d = {'title':'baidu','url':'http://www.baidu.com'}
# print(d.items())
# it = d.items()
# print(len(it))
# if (('title','baidu') in it):
#     print('true')
# else :
#     print('false')
#  #keys
# print(d.keys)
#  #pop(获取值并删除)
# currentItem = d.pop('title')
# print(currentItem)
# print(d)
# d['title'] ='baidu'
# print(d.popitem()) ##popitem获取一个值，随机获取和list不同
#  #setdefault(与get不同的是此方法当键不存在时候回添加键)
# d = {}
# d.setdefault('name','dujiadi')
# print(d['name'])
# d.setdefault('name','哈哈哈') ##如果存在'name'键，第二个参数忽略
# print(d['name'])
#  #update
# d ={
#     'title':'baidu',
#     'url':'www.baidu.com',
#     'info':'没google牛逼(技术文章)'
# }
# x = {'title':'google','url':'http://www.google.com'}
# d.update(x) ##更新相同键
# print(d)
#  #values
# print(d.values)
