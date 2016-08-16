# coding: utf-8
"""
题目：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
"""
# model_1:
n = 0 
s = 0 
t = 1 
for n in range(1,21):
	t *= n
	# print n,t
	s += t
	print (str("n")=%d,str("t")=%d,str("s")=%d) % (n,t,s)
# print "1!+2!+3!+...+20!=%d" % s
# print t,n,s




# model_2:
# s = 0
# l = range(1,21)
# def op(x):
# 	r = 1
# 	for i in range(1,1+x):
# 		r *= i 
# 		return r
# s = sum(map(op,1))
# print "1!+2!+3!+...+20!=%d" % s




















