# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class JobsSpider(Spider):
    name = 'jobs'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/jjj']

    def parse(self, response):
        for list in response.xpath('//li[@class="result-row"]'):
            title = list.xpath(
                './/a[@class="result-title hdrlnk"]/text()').extract_first()
            link = list.xpath(
                './/a[@class="result-title hdrlnk"]/@href').extract_first()
            date = list.xpath(
                './/*[@class="result-date"]/@datetime').extract_first()
            yield Request(url=link, callback=self.parse_list, meta={
                'date': date,
                "title": title,
                "link": link
            })

        # next_page_url = response.xpath(
        #     '//*[@title="next page"]/@href').extract_first()

        # if next_page_url:
        #     yield Request(url=response.urljoin(next_page_url), callback=self.parse)

    def parse_list(self, response):
        yield {
            'date': response.meta['date'],
            "title": response.meta['title'],
            "link": response.meta['link'],
            "compensation": response.xpath('//*[@class="attrgroup"]/span[1]/text()').extract_first(),
            "type": response.xpath('//*[@class="attrgroup"]/span[2]/text()').extract_first()
        }
