import json

# d = dict(name='杜佳迪',age=18)
# dd = json.dumps(d,ensure_ascii=False)
# print(dd)
# print(json.loads(dd))


class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return '%s的年龄为%s' % (self.name,self.age)

s = Student('杜佳迪',18)
j = json.dumps(s,default=lambda obj:obj.__dict__,ensure_ascii=False)
print(j)