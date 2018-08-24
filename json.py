"""
数组与str转换
"""
import demjson

a = [{"a":1},{"b":2}]
print(type(a))
# <class 'list'>

b = str(a)

c = demjson.decode(b)
print(c)
# [{"a":1},{"b":2}]
