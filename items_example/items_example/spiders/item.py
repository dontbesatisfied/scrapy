# -*- coding: utf-8 -*-
import scrapy
from items_example.items import ItemsExampleItem


class ItemSpider(scrapy.Spider):
    name = 'item'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        authors = response.xpath('//*[@itemprop="author"]/text()').extract()

        item = ItemsExampleItem()
        item['authors'] = authors
        return item
