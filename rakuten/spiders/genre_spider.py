# -*- coding: utf-8 -*-
import scrapy
import os
from .model.auth import auth


class GenreSpider(scrapy.Spider):
    name = 'genre'
    allowed_domains = ['app.rakuten.co.jp']

    def start_requests(self):
        base_url = 'https://app.rakuten.co.jp/services/api/BooksGenre/Search/20121128?format=json&booksGenreId=001'
        applicationId = auth.Auth().get_applicationId()
        url = base_url + '&applicationId=' + applicationId
        urls = [
            url,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file_name = os.path.dirname(__file__) + '/model/genre/genre.json'
        with open(file_name, 'w') as f:
            f.write(response.text)
