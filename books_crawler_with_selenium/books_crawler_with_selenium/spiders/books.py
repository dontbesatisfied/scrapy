# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from selenium import webdriver
from scrapy.selector import Selector

class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('/Users/ian/Desktop/ian/chromedriver')
        self.driver.get('http://books.toscrape.com/')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()

        for book in books:
            yield Request("http://books.toscrape.com/"+book,callback=self.parse_custom)

    def parse_custom(self, response):
        pass
