import csv

from relationalstocks_crawler.exporters import FixLineCsvItemExporter

class InsiderCrawlerPipeline(object):

    def __init__(self):
        self.file = open('insider.csv', 'wb')
        self.exporter = FixLineCsvItemExporter(self.file, fields_to_export=['report_time', 'trans_date', 'company', 'ticker', 'insider', 'shares_trader', 'avg_price', 'value'])
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def create_valid_csv(self, item):
        for key, value in item.items():
            is_string = (isinstance(value, str))
            if (is_string and ("," in value)):
                item[key] = "\"" + value + "\""

    def process_item(self, item, spider):
        # self.create_valid_csv(item)
        self.exporter.export_item(item)
        return item



class InstitutionCrawlerPipeline(object):

    def __init__(self):
        self.file = open('institution.csv', 'wb')
        self.exporter = FixLineCsvItemExporter(self.file, fields_to_export=['company', 'ticket', 'value_on', 'no_of_shares', 'percent_of_portfolio'])
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def create_valid_csv(self, item):
        for key, value in item.items():
            is_string = (isinstance(value, str))
            if (is_string and ("," in value)):
                item[key] = "\"" + value + "\""

    def process_item(self, item, spider):
        # self.create_valid_csv(item)
        self.exporter.export_item(item)
        return item