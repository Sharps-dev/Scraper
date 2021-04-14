from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news_scrapper.spiders.news_spider import NewsSpider

process = CrawlerProcess(get_project_settings())
process.crawl(NewsSpider)
process.start()