import scrapy
from scrapy.spiders import XMLFeedSpider
from news_scrapper.items import ContentItem


class RssfeedparserSpider(XMLFeedSpider):
    name = 'RssFeedParser'
    # allowed_domains = ['cnn.com']
    start_urls = ['https://rss.nytimes.com/services/xml/rss/nyt/World.xml']
    itertag='item'

    def parse_node(self, response , node):
        title = node.xpath('//title/text()').get() 
        url = node.xpath('//link/text()').get()
        description = node.xpath('//description/text()').get()

        yield ContentItem(title=title , url = url , description = description)