import scrapy 
from news_scrapper.items import ContentItem
from news_scrapper.settings import ITEM_OUTPUT_PATH
import json

class EastasiaforumSpider(scrapy.Spider):
    name='eastasiaforum'

    def start_requests(self):
        print("here")
        urls = [
            'https://www.eastasiaforum.org/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_content)
        
    def parse_content(self , response):
        print(response.url)
        for a in response.css('div[id="posts"] div.post '):
            title = a.css('header a::text').get()
            url = a.css('header a').attrib['href']
            image_url = a.css('img.attachment-frontpage.size-frontpage.wp-post-image ').attrib['src']
            description = a.css('section.content p::text').getall()[1]
            yield ContentItem(title=title , url = url , image_url=image_url , description = description)
