# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class ShuangseqiuPipeline(object):

    def __init__(self):
        self.connect = mysql.connector.connect(user='default', password='123456', host='localhost', port='3306',
                                               database='python', auth_plugin='mysql_native_password'
                                               )
        self.cur = self.connect.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connect.close()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO shuangseqiu Values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (item['date'],item['qiuH1'], item['qiuH2'], item['qiuH3'], item['qiuH4'],item['qiuH5'],item['qiuH6'],item['qiuL']))
        self.connect.commit()