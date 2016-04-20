# -*- encoding: utf-8 -*-

"""
class HouseItem(scrapy.Item):
    crawl_time    = scrapy.Field()  # 截取信息的时间
    area          = scrapy.Field()  # 面积(m^2)
    price         = scrapy.Field()  # 单价
    total_price   = scrapy.Field()  # 总价
    xiaoqu_id     = scrapy.Field()  # 小区ID
    xiaoqu_name   = scrapy.Field()  # 小区名称
    url           = scrapy.Field()  # 链家URL
    house_id      = scrapy.Field()  # 房子的uuid
"""

import sys
import json
import codecs

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        houses = json.load(f)
    
    houses.sort(lambda a, b: cmp(a['xiaoqu_name'], b['xiaoqu_name']))
    
    with codecs.open(sys.argv[2], "w", "utf-8") as f:
        f.write(u"<html>\n")
        f.write(u'<head><title>House Info</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head>\n')
        f.write(u"<body>")
        f.write(u'  <table border="1">\n')
        f.write(u"    <tr>\n")
        f.write(u"      <th>时间</th>\n")
        f.write(u"      <th>小区名称</th>\n")
        f.write(u"      <th>面积</th>\n")
        f.write(u"      <th>总价</th>\n")
        f.write(u"      <th>单价</th>\n")
        f.write(u"      <th>URL</th>\n")
        f.write(u"    </tr>\n")
        for house in houses:
            f.write(u"    <tr>\n")
            f.write(u"      <td>%s</td>\n" % house['crawl_time'])
            f.write(u"      <td>%s</td>\n" % house['xiaoqu_name'])
            f.write(u"      <td>%s</td>\n" % house['area'])
            f.write(u"      <td>%sw</td>\n" % house['total_price'])
            f.write(u"      <td>%s</td>\n" % house['price'])
            f.write(u'      <td><a href="%s">%s</a></td>\n' % (house['url'], house['house_id']))
            f.write(u"    </tr>\n")
        f.write(u"  </table>\n")
        f.write(u"</body>")
        f.write(u"</html>")
        