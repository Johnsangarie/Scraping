import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['https://www.politico.com/search?s=']
    start_urls = ['http://https://www.politico.com/search?s=/']

    def parse(self, response):
        pass
