from datetime import datetime, timedelta
import sys

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


if __name__ == '__main__':
    print("""
        relationalstocks.com crawler

        Please select script to run:
        1. Insider scrapping
        2. Institution scrapping
    """)
    script = input('Please select number 1 or 2: ')

    if script == '1':
        print()
        print('Please type the days when you want to scrapping data')
        start_day = None
        end_day = None
        exit = False
        while True:
            try:
                start_day = input('From: (YYYY-MM-DD) or q to exit: ')
                if start_day == 'q':
                    exit = True
                    break
                end_day = input('To: (YYYY-MM-DD) or q to exit: ')
                if end_day == 'q':
                    exit = True
                    break

                start_day = datetime.strptime(start_day, '%Y-%m-%d')
                end_day = datetime.strptime(end_day, '%Y-%m-%d')
                break
            except:
                print('You enter wrong format. Please try again!')
            else:
                if start_day > end_day:
                    print('Make sure the end day is after the start day!')

        if exit:
            sys.exit(0)

        d = start_day
        delta = timedelta(days=1)
        days = []
        while d <= end_day:
            days.append(d.strftime("%Y-%m-%d"))
            d += delta

        process = CrawlerProcess(get_project_settings())
        process.crawl('insider', days)
        process.start()

    elif script == '2':
        print()
        id = input('Please input the ID want to scrapping data: ')
        process = CrawlerProcess(get_project_settings())
        process.crawl('institution', id)
        process.start()
    else:
        print('Please select either script 1 or 2 to run')
