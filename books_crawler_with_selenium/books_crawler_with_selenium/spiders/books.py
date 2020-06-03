# -*- coding: utf-8 -*-
from time import sleep
from scrapy import Spider, Request
from selenium import webdriver
from scrapy.selector import Selector
from selenium.common.exceptions import NoSuchElementException


class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        # Must install chrome webdriver
        # https://chromedriver.chromium.org/downloads
        CHROME_DRIVER_PATH = '/Users/ian/workspace/my/chromedriver'
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.get('http://books.toscrape.com/')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()

        for book in books:
            URL = "http://books.toscrape.com/"+book
            yield Request(URL, callback=self.parse_custom)

        while True:
            try:
                self.driver.find_element_by_xpath(
                    '//a[text()="next"]').click()
                sleep(1)
                sel = Selector(text=self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract()

                for book in books:
                    URL = "http://books.toscrape.com/catalogue/"+book
                    yield Request(URL, callback=self.parse_custom)
            except NoSuchElementException:
                self.driver.quit()
                break

    def parse_custom(self, response):
        yield {'Title': response.xpath('//*[@class="col-sm-6 product_main"]/h1/text()').extract_first()}
