import scrapy


class PoliticalNewsSpider(scrapy.Spider):
    name = 'political_news'
    allowed_domains = ['https://www.politico.com/search?s=']
    start_urls = ['http://https://www.politico.com/search?s=/']

    def parse(self, response):
        pass
