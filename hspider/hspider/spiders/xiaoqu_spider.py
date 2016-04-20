# -*- encoding: utf-8 -*-
#
# 抓出页面中所有 house url

import re
import json
import datetime
from hspider.urls import XIAOQU_URLS
from hspider.items import XiaoquItem
from scrapy import Spider

class XiaoquSpider(Spider):
    name = "xiaoqu_spider" 
    allowed_domains = ["lianjia.com"] 
    start_urls = XIAOQU_URLS
    
    pattern = re.compile(r'http://gz.lianjia.com/ershoufang/GZ[0-9]*.html')

    def parse(self, response):
        urls = list(set(re.findall(self.pattern, response.body)))
        for url in urls:
           item = XiaoquItem()
           item['url'] = url
           yield item
        
