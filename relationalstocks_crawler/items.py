# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RelationalstocksCrawlerItem(scrapy.Item):
    report_time = scrapy.Field()
    trans_date = scrapy.Field()
    company = scrapy.Field()
    ticker = scrapy.Field()
    insider = scrapy.Field()
    shares_trader = scrapy.Field()
    avg_price = scrapy.Field()
    value = scrapy.Field()
