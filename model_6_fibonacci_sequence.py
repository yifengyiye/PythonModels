# coding: utf-8
"""
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。在数学上，费波那契数列是以递归的方法来定义：
F0 = 0                (n=0)
F1 = 1                (n=1)
Fn = F[n-1]+F[n-2]    (n>1)
"""


"""
# model_1:
def fib(n):
	a=1
	b=1
	for i in range(n-1):
		a,b=b,a+b
	return a

print fib(10)
"""


"""
# model_2:
def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1) + fib(n-2)

print fib(10)
"""


# model_3:
def fib(n):
	if n ==1:
		return [1]
	if n ==2: 
		return [1,1]
	fibs = [1,1] 
	for i in range(2,n):
		fibs.append(fibs[-1] + fibs[-2])
		return fibs

print fib(4)

# model_3中fib函数不执行循环，怎么解决？？？




















