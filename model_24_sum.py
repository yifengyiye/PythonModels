# coding: utf-8
"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
"""
# # model_1:
# a = 2.0
# b = 1.0
# s = 0 
# for n in range(1,21):
# 	s += a/b
# 	t = a
# 	a = a+b 
# 	b = t
# print s 

# model_2:
a = 2.0
b = 1.0
s = 0
for n in range(1,21):
	s += a + b
	b,a = a, a+b
print s 

s = 0.0
for n in range(1,21):
	s += a+b
	b,a = a, a+b

# # model_3:
# a = 2.0
# b = 1.0
# l = []
# for n in range(1,21):
# 	b,a = a, a+b
# 	l.append(a/b)
# print reduce(lambda x,y : x+y,1)


