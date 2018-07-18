from collections import deque

# deque双向队列，在对列表插入和更新时效率比列表更高
names = deque(['a','b','c','d'])
print(names.popleft())