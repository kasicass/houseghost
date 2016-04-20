# -*- encoding: utf-8 -*-
#
#<script>
#  require(['detail/newDetail'],function(init){
#    init({
#      isLoged:0,
#      houseType:'普通住宅',
#      isUnique:'暂无数据',
#      registerTime:'暂无数据',
#      area:'106.13',
#      totalPrice:'486',
#      price:'45793',
#      houseId:'GZ0001571784',
#      resblockId:'2111103317286',
#      resblockName:'理想蓝堡国际花园',
#      isRemove:0,
#      defaultImg:'http://static1.ljcdn.com/pc/asset/img/new-version/default_block.png?_v=20160407223720',
#      defaultBrokerIcon:'http://static1.ljcdn.com/pc/asset/img/jingjiren/noimg.jpg?_v=20160407223720',
#      resblockPosition:'113.363822,23.133652',
#      cityId:'440100'
#    });
#  });
#</script>

import os
import json
import datetime
from hspider.items import HouseItem
from scrapy import Spider

# detail/newDetail => validate json
def jsstr2jsonstr(jsstr):
    def filterit(s):
        s = s.strip().split(':')
        return len(s) == 2

    def makeit(s):
        s = s.strip().split(':')
        return '"' + s[0] + '":' + s[1].replace("'", '"') + '\n'

    tmp = jsstr.split('\n')
    tmp2 = [makeit(v) for v in tmp[1:-1] if filterit(v)]
    return '{' + ''.join(tmp2) + '}'

def generate_house_urls():
    try:
        f = open(r'house_urls.json')
        ret = json.load(f)
        f.close()
        ret = [v['url'] for v in ret]
    except:
        ret = []
    return ret

class HouseSpider(Spider):
    name = "house_spider" 
    allowed_domains = ["lianjia.com"] 
    #start_urls = [ 
    #    "http://gz.lianjia.com/ershoufang/GZ0001571784.html",
    #    "http://gz.lianjia.com/ershoufang/GZ0001535703.html",
    #    "http://gz.lianjia.com/ershoufang/GZ0001558387.html",
    #]
    start_urls = generate_house_urls()
    
    def parse(self, response): 
        a = response.xpath('//script').extract()
        b = [v for v in a if v.find('detail/newDetail') != -1]
        house_json_str = b[0].split('init(')[-1].split(');')[0].replace("'", '"')
        
        d = json.loads(jsstr2jsonstr(house_json_str))
        
        item = HouseItem()
        item['crawl_time']    = datetime.datetime.now()
        item['area']          = float(d['area'])
        item['price']         = int(d['price'])
        item['total_price']   = int(d['totalPrice'])
        item['xiaoqu_id']     = d['resblockId']
        item['xiaoqu_name']   = d['resblockName']
        item['url']           = response.url
        item['house_id']      = response.url.split('/')[-1].split('.')[0]
        yield item
