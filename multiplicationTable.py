# # def printMultiplicationTableFunA():
# #     for x in range(1,10):
# #         for y in range(x,10):
# #             result=" "+str(x*y) if x*y<10 else str(x*y)
# #             print str(x)+"*"+str(y)+"="+result,
# #         print ""
        
# # def printMultiplicationTableFunB():
# #     for x in range(1,10):
# #         for y in range(1,x+1):
# #             result=" "+str(x*y) if x*y<10 else str(x*y)
# #             print str(y)+"*"+str(x)+"="+result,
# #         print ""
        
# # printMultiplicationTableFunB()
# # print "------------------------------------------------------------------------------------------"
# # printMultiplicationTableFunA()


def printMultiplicationTableFunA():
    for x in range(1,10):
        for y in range(x,10):
            print'{0}*{1}={2}'.format(x,y,'{: >2}'.format(x*y)),
        print""
        
def printMultiplicationTableFunB():
    for x in range(1,10):
        for y in range(1,x+1):
            print'{0}*{1}={2}'.format(y,x,'{: >2}'.format(x*y)),
        print""
        
printMultiplicationTableFunB()
print("------------------------------------------------------------------------------------------")
printMultiplicationTableFunA()


# print '{:*^20}'.format("hello")


