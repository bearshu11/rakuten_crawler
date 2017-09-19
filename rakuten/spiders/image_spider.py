# -*- coding: utf-8 -*-
import scrapy
import datetime


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['https://app.rakuten.co.jp/']
    start_urls = ['https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404/']

    def start_requests(self):
        date = datetime.datetime.now.strftime('%Y%m%d')
        base_url = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/'
        url = base_url + date + '?'
        urls = [
            'https://app.rakuten.co.jp/services/api/BooksBook/Search/' + date,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
