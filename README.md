# Relational Stocks Crawler

:exclamation: This only works with Python 3

## Disclaim:
I followed the `robots.txt` in the [site](http://relationalstocks.com/robots.txt)

```shell
User-agent: *
Crawl-delay: 120
Disallow: /cgi-bin/
```

There are 2 script which crawl 2 type of data from Relational Stock site: [/instshow.php](http://relationalstocks.com/showinsiders.php?date={day}&buysell=buysell)  and [/showinsiders.php](http://relationalstocks.com/instshow.php?id=1&op=port&sort=percentdesc&page=1)

## Crawled data example

Fields collected from `/showinsiders.php`

- Reported Time
- Transaction
- Company
- Ticker
- Insider
- Shares
- Traded
- Average Price
- Price
- Value

Output data is `CSV` format:

![Alt text](./relationalstocks_crawler/img/data.png?raw=true)

```
report_time,trans_date,company,ticker,insider,shares_trader,avg_price,value
09-29-2017,2017-09-28 ,PATRICK INDUSTRIES INC,PATK,"NEMETH ANDY L
President, Director","2,000",$84.95,"$169,900"
09-29-2017,2017-09-27 ,PATRICK INDUSTRIES INC,PATK,"NEMETH ANDY L
President, Director","5,000",$83.03,"$415,150"
09-29-2017,2017-09-27 ,PATRICK INDUSTRIES INC,PATK,"Cleveland Todd M
CEO, Director","10,000",$83.16,"$831,600"
09-29-2017,2017-09-08 ,INTERSECTIONS INC,INTX,"Osmium Partners, LLC
10% owner","19,286",$3.35,"$64,608"
```

## Install

1. Install virtualenv via pip
    ```bash
    pip install virtualenv
    ```
    Test your installation
    ```bash
    virtualenv --version
    ```

2. Create a virtual environment for a project and install `scrapy`

    ```bash
    cd my_project_folder
    virtualenv my_project
    source my_project/bin/activate
    pip install Scrapy
    ```

3. Clone and run
    ```bash
    git clone https://github.com/hscup/rs_crawler.git
    cd re_crawler

    python run.py
    ```
