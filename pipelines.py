# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb
class StoreNamePipeline(object):
    def __init__(self):
        self.file = codecs.open('tencent.json', 'a', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self,spider):
        self.file.close()

class StoreDbPipeline(object):
    def process_item(self,item,spider):
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='wang',db='test',port=3306,charset='utf8')
            cur=conn.cursor()
            cur.execute('select ifnull(max(id),0) id from tieba')
            result=cur.fetchone()
            idN = result[0]+1
            length = len(item['userId'])
            #print length
            #print idlength
            #print len(item['content'])
            values=[]
            insertStr =''
            contentIndex =0
            for i in range(length):
                #o = str(i)+'_'+str(contentIndex)
                #print i
                #print contentIndex
                while(item['content'][contentIndex].isspace()):
                    contentIndex=contentIndex+1
                #print str(i)+str(contentIndex)
                values.append((idN+i,item['userId'][i],item['content'][contentIndex]))
                #print item['content'][contentIndex]
                contentIndex=contentIndex+1

                #print idN+i
                #print item['userId']
                #print item['content']
                #values.append(item['userId'][i])
                #values.append(item['level'][i])
                #values.append(item['content'][i].encode("utf-8") )
                #contentStr = item['content'][i]
                #print contentStr
                #values.append(contentStr)
                #values.append(.decode('unicode_escape'))

                insertStr+='(%s,%s,%s),'
            insertStr = insertStr[0:len(insertStr)-1]
            #values.append((1,'糯米','糯米'))
            #print insertStr
            #print values
            #insertVal = [];
            #insertVal.append(('1','1','1'))
            #insertVal.append(values[0])
            #insertVal.append(values[1])
            #insertVal.append(values[2])
            #insertVal.append(values[3])
            #cur.executemany('insert into test values'+insertStr,values)
            #print values
            cur.executemany('insert into tieba(id,userId,content) values  (%s,%s,%s)',values)
            conn.commit()
            cur.close()

            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            #MySQLdb.connect("")
