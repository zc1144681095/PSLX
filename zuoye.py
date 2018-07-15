'''
num1,num2 = eval(input("输入俩个数字"))
if num1>=num2:
	print ("{}>={}" .format(num1,num2))
else:
	print("{} < {}".format(num1,num2))
'''

# 输入字符串
zfc1,zfc2 = eval(input("输入俩个字符串"))
i = 0
#循环
while i< len(zfc1):
	for i in range(len(zcf1)):
	#比较首字母大小
		if ord('zfc1[i]')== ord('zfc2[i]'):
			i += 1
			continue
		elif ord('zfc1[i]')<ord('zfc2[i]'):
			b = zfc1<zfc2
			print(b)
			break
		else:
			print('zfc1>zfc2')
			break


'''
s = input("输入字符串")
#首字母大小，其他字母小写，python字典
a1 = s.title()
#分割
a2 = a1.split(' 'maxsplit=1)
print(a2)
‘’‘
'''
'''
s = input("输入一个字符串")
i = 0
r = 0 
e = 0
g = 0
f = 0
while i<len(s):
	#遍历所有的字符
	print(s[i])
	i += 1
for r in s:
#大写个数
	if r.isupper()== True:
		e += 1
#小写个数
	if r.islower()== True:
		g += 1
#数字个数
	if r.isdigit() == True:
		f += 1
print("大写字母有{}个，小写有{}个，数字有{}个" .format(e ,g,f))
'''
