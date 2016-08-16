# coding: utf-8
"""
题    目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
"""
import numpy as np

l = []
sum = 0

for i in range(5):
	x = float(raw_input("integer:"))
	l.append(x)
	sum = sum + x
	mean = np.mean(x)
l.sort()
print l
print sum
print mean

# 怎样对任意个数进行排序？？？
# 怎样对任意个复数进行排序？？？
# mean怎么计算？






























