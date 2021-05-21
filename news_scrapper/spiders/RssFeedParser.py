import scrapy
from scrapy.spiders import XMLFeedSpider
from news_scrapper.items import ContentItem


class RssfeedparserSpider(XMLFeedSpider):
    name = 'RssFeedParser'
    # allowed_domains = ['cnn.com']
    start_urls = ['https://rss.nytimes.com/services/xml/rss/nyt/World.xml']
    itertag='item'

    def parse_node(self, response , node):
        item = ContentItem()
        item['title'] = node.xpath('//title/text()').get() 
        item['url'] = node.xpath('//link/text()').get()
        item['description'] = node.xpath('//description/text()').get()
        # print(item.title)
        yield response.follow(item['url'] , self.get_image , cb_kwargs=dict(item=item))
    
    def get_image(self , response , item):
        # print("hdasdasdi")
        item['image_url'] = response.css('img').xpath('@src').get()
        yield item