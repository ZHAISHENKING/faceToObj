# 简单装饰器
def outside(func):
	"""
	参数是函数，返回值也是函数
	"""
	def inside():
		func()
		print('cde')
	return inside
# 带参数的
def hello():
	print('abc')

outside(hello)()

def out(f):
	def ins(str):
		f(str)
		print(str)
	return ins
def he(str):
	print(str)

out(he)('abc')

# 复杂装饰器
def ou(func):
	def insi(str):
		func(str)
		print(str)
	return insi

@ou
def hel(str):
	print(str)

hel('789')
