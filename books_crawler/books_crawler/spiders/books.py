# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # follow=True 일 경우 응답에 박혀있는 링크도 타고 들어간다.
    rules = (Rule(LinkExtractor(allow='music'), callback='parse_page', follow=True),)

    def parse_page(self, response):
        pass
