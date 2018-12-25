# from collections import namedtuple

# point = namedtuple('point',['x','y'])
# p = point(1,2)
# print(p.x,p.y)

# from collections import deque
# q = deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)

# from collections import defaultdict
# dd = defaultdict(lambda:'None')
# dd['key1'] = 'key1'
# print(dd['key1'])
# print(dd['key2'])

# from collections import OrderedDict
# d = OrderedDict([('a',1),('b',2),('c',3),('d',4)])
# print(list(d))

from collections import Counter
c = Counter()
for ch in 'dujiadidukedi':
    c[ch] = c[ch] + 1
print(c)