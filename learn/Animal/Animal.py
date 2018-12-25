# -*- codeing:utf-8 -*-

'动物'

__author__ = '杜佳迪'

class Animal(object):
    __slots__ = ('name') ##对象的属性只能为name
    def run(self):
        print('动物跑')

class Dog(Animal):
    def run(self):
        print('狗跑')

class Cat(Animal):
    def run(self):
        print('猫跑')

class Test(object):
    def run(self):
        print('未继承')

def run_twice(animal):
    animal.run();
    animal.run();

# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())
# run_twice(Test()) ##动态语言。。。

# print(type(Animal()))
# print(type(Dog()))
# print(type(Cat()))
# print(type(Test()))

# print(isinstance(Animal(),Animal))
# print(isinstance(Dog(),Animal))
# print(isinstance(Cat(),Animal))
# print(isinstance(Test(),Animal))

# print(dir(Animal))
# print(dir(Dog))
# print(dir(Cat))
# print(dir(Test))

# a = Animal()
# a.age = 1
# print(a.age)

# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')