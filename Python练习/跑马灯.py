#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import Counter
from collections import namedtuple
from collections import defaultdict
s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()
c = Counter(s)
# 获取出现频率最高的5个字符
print (c.most_common(5))
print(c['s'])
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)
dd = defaultdict(list)
print( dd['key1'])
print (defaultdict.__missing__.__doc__)