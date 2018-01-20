# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from webcrawl.main import f_count

class WebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    if f_count is int(1):
        record1 = scrapy.Field()
    elif f_count is int(2):
        record1 = scrapy.Field()
        record2 = scrapy.Field()
    elif f_count is int(3):
        record1 = scrapy.Field()
        record2 = scrapy.Field()
        record3 = scrapy.Field()
    elif f_count is int(4):
        record1 = scrapy.Field()
        record2 = scrapy.Field()
        record3 = scrapy.Field()
        record4 = scrapy.Field()
    elif f_count is int(5):
        record1 = scrapy.Field()
        record2 = scrapy.Field()
        record3 = scrapy.Field()
        record4 = scrapy.Field()
        record5 = scrapy.Field()
    elif f_count is int(6):
        record1 = scrapy.Field()
        record2 = scrapy.Field()
        record3 = scrapy.Field()
        record4 = scrapy.Field()
        record5 = scrapy.Field()
        record6 = scrapy.Field()
    elif f_count is int(7):
        record1 = scrapy.Field()
        record2 = scrapy.Field()
        record3 = scrapy.Field()
        record4 = scrapy.Field()
        record5 = scrapy.Field()
        record6 = scrapy.Field()
        record7 = scrapy.Field()
    else:
        print("범위 초과")

