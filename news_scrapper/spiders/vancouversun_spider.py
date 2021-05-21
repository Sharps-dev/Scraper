import scrapy 
from news_scrapper.items import ContentItem
from news_scrapper.settings import ITEM_OUTPUT_PATH
import json

class VancouversunSpider(scrapy.Spider):
    name='vancouversun'

    def start_requests(self):
        urls = [
            'https://vancouversun.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_content)
        
    def parse_content(self , response):

        for a in response.css('article.article-card'):
            title = a.css('div.article-card__details a.article-card__link h3 span::text').get()
            url = a.css('div.article-card__details a.article-card__link').attrib['href']
            image_url = a.css('div.article-card__content a.article-card__image-link picture.article-card__image img').attrib['src']
            description = a.css('div.article-card__content div.article-card__details p.article-card__excerpt::text').get()
            yield ContentItem(title=title , url = url , image_url=image_url , description = description)
