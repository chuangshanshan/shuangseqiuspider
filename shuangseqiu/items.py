# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShuangseqiuItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    qiuH1 = scrapy.Field()
    qiuH2 = scrapy.Field()
    qiuH3 = scrapy.Field()
    qiuH4 = scrapy.Field()
    qiuH5 = scrapy.Field()
    qiuH6 = scrapy.Field()
    qiuL = scrapy.Field()
    pass
