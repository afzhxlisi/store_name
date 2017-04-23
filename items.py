# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StoreNameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    comname = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    price =scrapy.Field()
    num = scrapy.Field()
    fangurl = scrapy.Field()
    comurl = scrapy.Field()
    totalNum = scrapy.Field()
    lastThreeMonSales = scrapy.Field()
    totalWatchNum = scrapy.Field()
    pass
