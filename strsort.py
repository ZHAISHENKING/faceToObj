a = '1234abc'

def fsort(str):
	"""字符串反转函数"""
	result = ''
	for i in str:
		result = i+result
	return result

print(fsort(a))