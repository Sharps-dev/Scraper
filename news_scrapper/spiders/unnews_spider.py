import scrapy
from scrapy.spiders import XMLFeedSpider
from news_scrapper.items import ContentItem
from news_scrapper.settings import  DELIM


class UnNewsSpider(XMLFeedSpider):
    name = 'UnParser'
    # allowed_domains = ['cnn.com']
    start_urls = [    'https://news.un.org/feed/subscribe/en/news/all/rss.xml','https://news.un.org/feed/subscribe/en/news/topic/health/feed/rss.xml' , 'https://news.un.org/feed/subscribe/en/news/topic/human-rights/feed/rss.xml' , 'https://news.un.org/feed/subscribe/en/news/topic/culture-and-education/feed/rss.xml','https://news.un.org/feed/subscribe/en/news/topic/economic-development/feed/rss.xml'
            ,'https://news.un.org/feed/subscribe/en/news/topic/peace-and-security/feed/rss.xml']

    itertag='item'

    def parse_node(self, response , node):
        item = ContentItem()
        item['title'] = node.xpath('//title/text()').get() 
        item['url'] = node.xpath('//link/text()').get()
        item['description'] = node.xpath('//description/text()').get()
        l=node.xpath('//category/text()').getall()
        item['tags'] = "peace||security"
        item['image_url'] = node.xpath('//image/url/text()').get()  
        # print(item.title)
        # yield response.follow(item['url'] , self.get_image , cb_kwargs=dict(item=item))
        yield item
    
    def get_image(self , response , item):
        # print("hdasdasdi")
        item['image_url'] = response.css('img').xpath('@src').get()
        yield item