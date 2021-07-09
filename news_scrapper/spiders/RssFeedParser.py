import scrapy
from scrapy.spiders import XMLFeedSpider
from news_scrapper.items import ContentItem
from news_scrapper.settings import  DELIM


class RssfeedparserSpider(XMLFeedSpider):
    name = 'RssFeedParser'
    # allowed_domains = ['cnn.com']
    
    start_urls = ['https://rss.nytimes.com/services/xml/rss/nyt/Arts.xml' , 'https://rss.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml'
    , 'https://rss.nytimes.com/services/xml/rss/nyt/Travel.xml','https://rss.nytimes.com/services/xml/rss/nyt/Jobs.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/RealEstate.xml','https://rss.nytimes.com/services/xml/rss/nyt/Automobiles.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/World.xml' ,
    'https://rss.nytimes.com/services/xml/rss/nyt/World.xml' , 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml','https://rss.nytimes.com/services/xml/rss/nyt/Health.xml']
    itertag='item'

    def parse_node(self, response , node):
        item = ContentItem()
        item['title'] = node.xpath('//title/text()').get() 
        item['url'] = node.xpath('//link/text()').get()
        item['description'] = node.xpath('//description/text()').get()
        l=node.xpath('//category/text()').getall()
        item['tags'] = DELIM.join(l) if len(l)>0 else None
            
        # print(item.title)
        yield response.follow(item['url'] , self.get_image , cb_kwargs=dict(item=item))
    
    def get_image(self , response , item):
        # print("hdasdasdi")
        item['image_url'] = response.css('img').xpath('@src').get()
        yield item