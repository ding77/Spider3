# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

import MySQLdb
from pandas._libs import json


class Spider3Pipeline(object):
    def process_item(self, item, spider):
        return item
class doubanPipeline(object):#创建写入文本
    def __init__(self):
        self.file= codecs.open('taobao.json', 'w', 'utf-8')
    def process_item(self,item,spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(lines)
        return item
    def close_spider(self, spider):
        self.file.close()
class MysqlPipline(object):
    def __init__(self):
        self.conn = MySQLdb.connect("127.0.0.1", "ding", "", "test", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
              insert into jo(title,img)
              VALUES(%s,%s)
        """
        self.cursor.execute(insert_sql,(item["title"],item['img']))
        self.conn.commit()


