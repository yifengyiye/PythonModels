 # encoding=utf8  
import sys  
  
reload(sys)  
sys.setdefaultencoding('utf8') 

import urllib2
import json
urlBase="https://api.douban.com/"
urlBody="v2/movie/subject/"

for x in xrange(1293000,1293100):
	url=urlBase+urlBody+str(x)
	print url
	a=urllib2.urlopen(url).read()
	print a.decode("unicode_escape")

