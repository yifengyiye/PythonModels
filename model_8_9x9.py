# coding: utf-8

"""
题目：输出9*9乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""

for x in range(1,10):
	for y in range(1,10):
		result = x*y
		print "%d * %d = % - 3d" % (x,y,result)
	print "\n"

# for x,y in range(x,y):
# 	result = x*y
# 	print str("x") * str("y"),result





















