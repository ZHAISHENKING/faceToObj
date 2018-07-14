import copy
# copy.copy 修改嵌套列表的值浅拷贝 修改列表值为深拷贝
a = [1,2,[3,4]]
b = copy.copy(a)
b[0] = 3
print(a,b)
print(id(a),id(b))
print('--------------')
c = copy.copy(a)
c[2][0] = 1
print(a,c)
print(id(a),id(c))
print('--------------')
# copy.deepcopy
aa = [1,2,[3,4]]
bb = copy.deepcopy(aa)
bb[2][0] = 7
print(aa,bb)
print(id(aa),id(bb))