#coding:utf-8
"""
题目：使用lambda来创建匿名函数。
"""
max = lambda x,y: (x>y)*x + (x<y)*y
min = lambda x,y: (x>y)*y + (x<y)*x

if __name__ == '__main__':
	a = 10
	b = 20 
	print "the larger one is %d" % max(a,b)
	print "the lower one is %d" % min(a,b)


#没看懂这函数的意义是什么？？？

