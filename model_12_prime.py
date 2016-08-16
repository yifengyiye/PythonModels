# coding: utf-8
"""
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　
"""
# h = 0 
# leap = 1

from math import sqrt
from sys import stdout

# for m in range(101,201):
# 	k = int(sqrt(m + 1))
# 	for i in range(2,k + 1):
# 		if m % i == 0:
# 			leap =0 
# 			break
# 	if leap == 1:
# 		print "%-4d" % m
# 		h += 1
# 		if h % 10 == 0:
# 			print ""
# 	leap = 1
# print "The total is %d" % h

def is_prime(n):                                            
    list_num = []    
    for i in range(101, n):        
        for num in range(2, int(sqrt(n))+1):            
            if i % num == 0 and i != num:                
                break            
            elif i % num != 0 and num == int(sqrt(n)):                
                list_num.append(i)    
    return list_num

print is_prime(201)
# for x in range(101,201):


# 定义的函数只能判断界定范围之内数值的素数，不能判断自定义范围内数据是否是素数，怎么解决？？？




