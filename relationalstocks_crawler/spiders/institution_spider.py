import scrapy
from relationalstocks_crawler.items import InstitutionCrawlerItem


class InstitutionSpider(scrapy.Spider):
    name = 'institution'
    allowed_domains = ['relationalstocks.com']

    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [f'http://relationalstocks.com/instshow.php?id={id}&op=port&sort=percentdesc&page=1']

    custom_settings = {
        'ITEM_PIPELINES': {'relationalstocks_crawler.pipelines.InstitutionCrawlerPipeline': 700},
        'LOG_FILE': 'logs/institution.log',
        'LOG_LEVEL': 'ERROR'
    }

    def parse(self, response):
        rows = response.xpath('.//thead/tr')
        item = InstitutionCrawlerItem()

        for row in rows:
            company = row.xpath('.//td[1]/a/text()').extract_first()
            if company is None:
                continue

            company = company.replace(u'\xa0', u' ')
            ticket = row.xpath('.//td[2]/a/text()').extract_first()
            value_on = row.xpath('.//td[3]/text()').extract_first()
            no_of_shares = row.xpath('.//td[4]/text()').extract_first()
            percent_of_portfolio = row.xpath('.//td[5]/text()').extract_first()

            item['company'] = company
            item['ticket'] = ticket
            item['value_on'] = value_on
            item['no_of_shares'] = no_of_shares
            item['percent_of_portfolio'] = percent_of_portfolio

            yield item

        next_page_url = response.xpath(
            '//a[contains(text(),"Next")]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
