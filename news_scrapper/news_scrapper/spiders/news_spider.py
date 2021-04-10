import scrapy 
from news_scrapper.items import ContentItem
class NewsSpider(scrapy.Spider):
    name='news'

    def start_requests(self):
        urls = [
            'https://english.elpais.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_content)
        
    def parse_content(self , response):
        for a in response.css('a::text').getall():
            yield ContentItem(title=a)
