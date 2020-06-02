# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest


class QuotesLoginStandaloneSpider(Spider):
    name = 'quotes_login_standalone'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath(
            '//*[@name="csrf_token"]/@value').extract_first()
        yield FormRequest('http://quotes.toscrape.com/login', formdata={
            'csrf_token': csrf_token,
            'username': 'scrapy',
            'password': 'pw'
        }, callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.xpath('//a[text()="Logout"]'):
            self.log('You logged in')
