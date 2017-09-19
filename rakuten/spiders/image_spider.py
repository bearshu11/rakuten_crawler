# -*- coding: utf-8 -*-
import scrapy
from .model.genre import genre
from .model.auth import auth


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['https://app.rakuten.co.jp/']

    def start_requests(self):
        base_url = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?'
        applicationId = auth.Auth().get_applicationId()
        booksGenreId = genre.Genre().get_booksGenreId()
        url = base_url + "applicationId=" + applicationId + "&booksGenreId=" + booksGenreId
        urls = [
            url,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
