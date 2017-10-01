from datetime import datetime

import scrapy

from relationalstocks_crawler.items import InsiderCrawlerItem


class InsiderSpider(scrapy.Spider):
    name = 'insider'
    allowed_domains = ['relationalstocks.com']
    
    start_urls = [
        'http://relationalstocks.com/showinsiders.php?date=2017-09-29&buysell=buysell']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['report_time', 'trans_date', 'company', 'ticker', 'insider', 'shares_trader', 'avg_price', 'value']
    }

    def parse(self, response):
        rows = response.xpath('.//tbody[@id="insidertab"]/tr')

        item = InsiderCrawlerItem()

        for row in rows:
            report_time = row.xpath('.//td[1]/text()').extract_first()
            if report_time:
                report_time = datetime.strptime(
                    report_time, '%Y-%m-%d %H:%M:%S')
                report_time = report_time.strftime('%m-%d-%Y')

            trans_date = row.xpath('.//td/font[1]/text()').extract_first()
            company = row.xpath('.//td[3]/a/text()').extract_first()
            ticker = row.xpath('.//td[4]/a/text()').extract_first()
            insider = '\n'.join(row.xpath('.//td[5]/a/text()').extract())
            shares_trader = row.xpath('.//td[6]/text()').extract_first()
            avg_price = row.xpath('.//td[7]/text()').extract_first()
            value = row.xpath('.//td[8]/text()').extract_first()

            item['report_time'] = report_time
            item['trans_date'] = trans_date
            item['company'] = company
            item['ticker'] = ticker
            item['insider'] = insider
            item['shares_trader'] = shares_trader
            item['avg_price'] = avg_price
            item['value'] = value

            yield item
