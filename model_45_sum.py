# coding:utf-8
"""
题目：统计 1 到 100 之和。
"""
num = 0 
for i in range(1,101):
	num += i
	print num
print 'The sum is %d' % num

#最后两行的结果print，前面有没有缩进区别很大，有缩进，每一次的循环结果都需要打印，没有缩进，只输出最后的结果；