# -*- coding:utf-8 -*-  

"""    
#mysqldb    
import time, MySQLdb    

#连接    
conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="test",charset="utf8")  
cursor = conn.cursor()    

#写入    
sql = "insert into user(name,created) values(%s,%s)"   
param = ("aaa",int(time.time()))    
n = cursor.execute(sql,param)    
print n    

#更新    
sql = "update user set name=%s where id=3"   
param = ("bbb")    
n = cursor.execute(sql,param)    
print n    

#查询    
n = cursor.execute("select * from user")    
for row in cursor.fetchall():    
    for r in row:    
        print r    

#删除    
sql = "delete from user where name=%s"   
param =("aaa")    
n = cursor.execute(sql,param)    
print n    
cursor.close()    

#关闭    
conn.close()
"""

import MySQLdb
import webbrowser
import urllib
import json

ff = open('errlist.txt','w')

i=0
j=0

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'M7eHC8UDLyWo9qrzeLOAXeBihg8v0GOP'
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    temp = urllib.urlopen(uri)
    t = json.loads(temp.read())    
    s3 = t["status"]
    
    if s3 == 0:
       s1 = t["result"]["location"]["lng"]
       s2 = t["result"]["location"]["lat"]


       ssss = str(s1) + ',' + str(s2)

       return ssss
       
  
#库名：easylife;表名：el_mall_order  
  
conn = MySQLdb.connect(host="127.0.0.1",user="easylife",passwd="easylife",db="easylife",charset="utf8")  
cursor = conn.cursor()

markers = ""

count = cursor.execute("select consignee_address from el_mall_order where pay_time like '2016-08-25%'")
for row in cursor.fetchall():    
    for r in row:
        

        if(getlnglat(r.encode('utf8'))!=None):
            ss1 = getlnglat(r.encode('utf8'))
            markers = markers + ss1 + "|"
            j=j+1
        else:
            i=i+1
            ff.write(r.encode('utf8'))
            ff.write("\n")
            print(r.encode('utf8'))

ff.close()

conn.close()


print "error:" + str(i)
print "done:" + str(j)


apiurl = 'http://api.map.baidu.com/staticimage/v2'
output = 'json'
ak = 'M7eHC8UDLyWo9qrzeLOAXeBihg8v0GOP'
uri = apiurl + '?' + 'ak=' + ak + '&width=900' + '&height=600' + '&center=121.621391,38.919345' + '&zoom=12&markerStyles=s' + '&markers=' + markers

print uri

webbrowser.open(uri, new=0, autoraise=True, )



