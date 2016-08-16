# coding: utf-8

"""
题目：暂停一秒输出。 
"""
import time 
"""
myD = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f"}
for key,value in dict.items(myD):
	time.sleep(3)
	print key,value
	time.sleep(3)
	
# 第一组数据没有延迟显示，怎么操作才能让第一组键值数据对也延迟显示？？？
"""
# 不暂停直接输出
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#暂停一秒钟，然后再输出
time.sleep(1)
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#暂停5秒钟，然后再输出
time.sleep(5)
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#暂停10秒钟，然后再输出
time.sleep(10)
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#暂停15秒钟，然后再输出
time.sleep(15)
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))












