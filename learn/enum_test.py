
# -*- coding:utf-8 -*-

__author__ = '杜佳迪'

from enum import Enum, unique

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)

@unique
class WeekDay(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name,member in WeekDay.__members__.items():
    print(name,'=>',member,',',member.value)

# day1= WeekDay.Mon
# print(day1)
# print(WeekDay(1))
# print(WeekDay.Fri.value)
# print(Weekday['Tue'])

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


def fun(self):
    print('你好')
Hello = type('Hello',(object,),dict(hello = fun))
h = Hello()
h.hello()