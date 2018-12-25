# # -*- codeing:utf-8 -*-

# d = {(1,2,3)}
# print(d)
# d = {(1,[2,3])}
# print(d)
# s = set((1,2,3))
# print(s)
# s = set((1,[2,3]))
# print(s)


# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         # raise TypeError('类型错误！')
#         return '类型错误'
#     if x > 0:
#         return x
#     return -x

# while True:
#     i = input()
#     i = int(i)
#     print(my_abs(i))

# def triangles():
#     l = [1]
#     while True:
#         yield l
#         l = l + [0]
#         l = [l[i-1]+l[i] for i in range(len(l))]

# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# def reverseString(s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         return s[::-1]

# print(reverseString('杜佳迪'))


# def reverse(x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         i = 0
#         try:
#             if '-' in x:
#                 i = int('-' + x[1::][::-1])
#             else:
#                 i =  int(x[::-1])
#         except Exception as e:
#             print('i',e)
#             return i
#         return i


# t1 = reverse('123')
# t2 = reverse('-123')
# t3 = reverse('120')
# t4 = reverse('12345678912345678913245678945613461234567891234567891234567891324567894561346123456789')
# print(t1,t2,t3,t4,sep='\n')

# def f(x,y):
#     return x * y
# l = [1,2,3,4,5,6]
# l2 = [7,8,9,10,11,12,13,14]
# map_test = map(f,l,l2)
# for i in map_test:
#     print(i)
# # print([int(i) for i in map_test])

# from functools import reduce
# l = [1, 3, 5, 7, 9]
# def f(x,y):
#     return '{}{}'.format(x,y)
# reduct_test = reduce(f, l)
# print(reduct_test)

# ## 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
#     return '{}{}'.format(name[0].upper(),name[1:].lower())


# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# ##
# from functools import reduce
# def prod(L):
#     return reduce(lambda x,y: x * y, L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# # -*- coding: utf-8 -*-
# ## 把字符串'123.456'转换成浮点数123.456
# from functools import reduce

# def str2float(s):
#     dot_index = s.rfind('.')
#     s1 = s[0:dot_index]
#     s2 = s[dot_index+1:]
#     p1 = reduce(lambda x,y:x * 10 + y,map(int,s1))
#     p2 = reduce(lambda x,y:(x + y) * 0.1,map(int,reversed(s2)),0)
#     return p1 + p2

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# ## 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
# def is_palindrome(n):
#     return str(n)[::-1] == str(n)

# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     x,y = t
#     return -y
# L2 = sorted(L, key=by_name)
# print(L2)


# # 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# def createCounter():
#     i = 0

#     def counter():
#         nonlocal i
#         i = i + 1
#         return i
#     return counter


# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# def is_odd(n):
#     return n % 2 == 1


# L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
# print(L)


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log
# def now():
#     print('Hello')


# now()


# def log1(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s:%s' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# @log1('方法')
# def now1():
#     print('OK')


# log1('哈哈')(now1)()

# now1()

# import time
# import functools
# def metric(fn):
#     def wrapper(*args,**kw):
#         start_time = time.time()
#         result = fn(*args,**kw)
#         end_time = time.time()
#         print('%s executed in %s ms' % (fn.__name__, end_time - start_time))
#         return result
#     return wrapper


# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y


# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z


# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('f测试失败!%s' % f)
# elif s != 7986:
#     print('s测试失败!%s' % s)

# import functools
# int2 = functools.partial(int,base = 2)
# print(int2('1000000'))
# print(int2('1010101'))


# class Screen(object):
#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self,value):
#         self._height = value

#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self,value):
#         self._width = value

#     @property
#     def resolution(self):
#         return self._width * self._height
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')



# from functools import reduce

# def str2num(s):
#     if isinstance(s, float) == True:
#         return float(s)
#     else:
#         return int(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()

# import unittest

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if not 0 <= self.score <= 100:
#             raise ValueError('超了')
#         if self.score >= 80:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         return 'C'

# class TestStudent(unittest.TestCase):
    
#     def test_80_to_100(self):
#         s1 = Student('a',80)
#         s2 = Student('b',100)
#         self.assertEqual(s1.get_grade(),'A')
#         self.assertEqual(s2.get_grade(),'A')

#     def test_60_to_80(self):
#         s1 = Student('a',60)
#         s2 = Student('b',79)
#         self.assertEqual(s1.get_grade(),'B')
#         self.assertEqual(s2.get_grade(),'B')

#     def test_0_to_60(self):
#         s1 = Student('a',0)
#         s2 = Student('b',59)
#         self.assertEqual(s1.get_grade(),'C')
#         self.assertEqual(s2.get_grade(),'C')

#     def test_invalid(self):
#         s1 = Student('a',-1)
#         s2 = Student('b',101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
    
# if __name__ == '__main__':
#     unittest.main()


import re
m = re.search('?>=abc)def','abcdef')
print(m.group(0))
