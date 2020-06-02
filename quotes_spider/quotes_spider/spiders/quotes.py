# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy import Request


class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:

            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@class="keywords"]/@content').extract()

            yield {'Text': text, 'Author': author, 'Tags': tags}

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        full_next_page_url = response.urljoin(next_page_url)
        yield Request(full_next_page_url, callback=self.parse)