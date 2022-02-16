# Define here the models for your scraped items
#
# See documentation in:
#https://docs.scrapy.org/en/latest/topics/items.html

#from xml.dom.pulldom import parseString

import scrapy


class ItemsSpider(scrapy.Spider):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = "items"
    allowed_domains =['politico.com']
    start_urls = ['https://www.politico.com/search?s=&userInitiated=true&q=NFT']

    def parse(self, response):
        for article in response.css('article.story-frag.format-ml'):
            yield{
                'Title' : article.css('img').attrib['alt'],
                'Link'  : article.css('a').attrib['href'],
                'Intro' :  article.css('div.tease').css('p::text').get(),
                'Category' : article.css('p.category::text').get(),
                'DateandTime': article.css('time').attrib['datetime'],

   }


        for button in response.css('a.button'):
            if button.css('::text').get()  == 'Next page »':
                 next_page = button.attrib['href']
                 print(" \n Next Page:" + next_page + "\n" )
                 yield response.follow(next_page, callback = self.parse)
