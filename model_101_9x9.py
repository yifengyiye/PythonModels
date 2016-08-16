# coding:utf-8

# print "\n[九九乘法表]"
# for x in range(1,10):
# 	for y in range(1,x+1):
# 		print str(y)+"*"+str(x)+"="+(" "+str(x*y) if x*y<10 else str(x*y))," ",
# 	print " "
# print "  "

print "\n[九九乘法表]"
for x in range(1,10):
	for y in range(x,10):
		print "{1}*{1}={2}".format(x,y,"{: >2}".format(x*y)),"  ",
		# print str(x)+"*"+str(y)+"="+(" "+str(x*y) if x*y<10 else str(x*y))," ",
	print " "
print "  "