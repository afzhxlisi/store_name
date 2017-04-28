# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb
import datetime
class StoreNamePipeline(object):
    def __init__(self):
        self.file = codecs.open('tencent'+datetime.date.today().__str__()+'.json', 'a', encoding='utf-8')
        #self.numfile = codecs.open('num'+datetime.date.today().__str__()+'.json', 'a', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        #if(item.get('totalNum')!=None):
            #self.numfile.write(line)
        return item
    def spider_closed(self,spider):
        self.file.close()
        #self.numfile.close()

class StoreDbPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='12345678', db='test', port=3306, charset='utf8')
        self.cur = self.conn.cursor()
    def process_item(self,item,spider):
        try:

            cur = self.cur
            cur.execute('select ifnull(max(id),0) id from lianjia')
            result=cur.fetchone()
            idN = result[0]+1

            values=[]

            values.append((idN + 1, item['name'], item['comname'],item['type'],item['area'],item['price'],item['fangurl'],item['comurl']))

            cur.execute('insert into lianjia(id,name,comname,type,area,price,fangurl,comurl,time) values  (%s,%s,%s,%s,%s,%s,%s,%s,now())',values[0])
            self.conn.commit()



        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    def spider_closed(self,spider):
        self.cur.close()
        self.conn.close()