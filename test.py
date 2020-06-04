

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from quotes_login_standalone import QuotesLoginStandaloneSpider

settings = Settings()
settings.set('ROBOTSTXT_OBEY', False)

process = CrawlerProcess(settings=settings)
process.crawl(QuotesLoginStandaloneSpider)
process.start()
