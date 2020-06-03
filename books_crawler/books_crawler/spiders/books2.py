# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from books_crawler.items import BooksCrawlerItem


class Books2Spider(Spider):
    name = 'books2'
    allowed_domains = ['books.toscrape.com']

    def __init__(self, category):
        self.start_urls = [category]

    def parse(self, response):
        books_url = response.xpath(
            '//article[@class="product_pod"]/h3/a/@href').extract()
        for url in books_url:
            absolute_url = response.urljoin(url)
            yield Request(absolute_url, callback=self.parse_book)

        next_page_url = response.xpath(
            '//a[text()="next"]/@href').extract_first()
        absolute_next_url = response.urljoin(next_page_url)
        yield Request(absolute_next_url, callback=self.parse)

    def parse_book(self, response):
        l = ItemLoader(item=BooksCrawlerItem(), response=response)
        l.add_value('Title', response.xpath(
            '//*[@class="col-sm-6 product_main"]/h1/text()').extract_first())
        return l.load_item()

    def close(self, reason):
        print(reason, "!@#!@#!@#!@#@")
