import scrapy 
from news_scrapper.items import ContentItem
from news_scrapper.settings import ITEM_OUTPUT_PATH
import json
import sys


class ThepostmillennialSpider(scrapy.Spider):
    name='thepostmillennial'

    def start_requests(self):
        urls = [
            'https://thepostmillennial.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_content)
        
    def parse_content(self , response):

        for a in response.css('div.posts-list-item  '):
            try:
                title = a.css('div.headline h3::text').get()
                url = a.css('a.link ').attrib['href']
                image_url = a.css('div.cover-wrapper div.cover img.featured-image ').attrib['src']
                description = a.css('div.excerpt p::text').get()
                yield ContentItem(title=title , url = url , image_url=image_url , description = description)
            except:
                print(f'{a} can not get data')
                print(sys.exc_info()[0])
                continue

