# from contextlib import contextmanager

# class Query(object):
#     def __init__(self, name):
#         self.name = name
    
#     def query(self):
#         print('Query info about %s...',self.name)

# @contextmanager
# def creat_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')

# with creat_query('Bob') as q:
#     q.query()


# @contextmanager
# def tags(name):
#     print('<%s>' % name)
#     yield
#     print('</%s>' % name)

# with tags('h1') as t:
#     print('Hello')
#     print('Word')


from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line)
