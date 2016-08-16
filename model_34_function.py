# coding:utf-8
"""
题目：练习函数调用。
"""
import math

def hello_world():
	print "hello world"

def three_hellos(n):
	for x in range(n):
		hello_world()

three_hellos(3)

