# coding: utf-8
"""
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。
"""
# for x in xrange(1,a):
# 	for y in xrange(1,a-x):
# 		print " ",
# 	for z in xrange(1,2*a-1):
# 		print '*'
# 	print ""
from sys import stdout

a=5
s='*'
p='/'
for i in range(a):
    for j in range(3 - i + 1):
        stdout.write(p)
    for k in range(2 * i + 1):
        stdout.write(s)
    print

for i in range(a-1):
    for j in range(i + 1):
        stdout.write(p)
    for k in range(4 - 2 * i + 3):
        stdout.write(s)
    print




