# -*- coding: utf-8 -*-
#
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class XiaoquItem(scrapy.Item):
    url           = scrapy.Field()  # url of house

class HouseItem(scrapy.Item):
    crawl_time    = scrapy.Field()  # 截取信息的时间
    area          = scrapy.Field()  # 面积(m^2)
    price         = scrapy.Field()  # 单价
    total_price   = scrapy.Field()  # 总价
    xiaoqu_id     = scrapy.Field()  # 小区ID
    xiaoqu_name   = scrapy.Field()  # 小区名称
    url           = scrapy.Field()  # 链家URL
    house_id      = scrapy.Field()  # 房子的uuid
