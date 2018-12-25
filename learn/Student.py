# -*- coding:utf-8 -*-

'学生类'

__author__ = '杜佳迪'

class Student(object):
    print(1)
    def __init__(self, name,score,gender):
        print('__init__')
        self.name = name
        self.score = score
        self.__gender = gender

    print(2)
    def __str__(self):
        return '%s的分数是%s' % (self.name,self.score)
    
    def __repr__(self):
        return '%s的分数是%s' % (self.name,self.score)

    def __getattr__(self,attr):
        return '%s的新属性是%s' % (self.name,attr)

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender

    def print_score(self):
        print('%s : %s' % (self.name,self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def __call__(self):
        return '%s居然调用自己'%self.name
    print(3)

bart = Student('Bart',20,'21')
# bart.print_score()
# print(bart)
# print(bart.abc)
# print(bart())