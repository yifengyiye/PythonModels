# coding:utf-8
"""
题目：求100之内的素数
"""
from math import sqrt

if __name__ == "__main__":
	N=10
	a = range(0,N)
	for i in range(2,int(sqrt(N))):
		for j in range(i+1,N):
			if (a[i] != 0) and (a[j] != 0):
				if a[j] % a[i] ==0:
					a[j]=0
	print 
	for i in range(2,N):
		if a[i] != 0:
			print "%5d" % a[i]
			if (i - 2) % 10 == 0 :
				print 