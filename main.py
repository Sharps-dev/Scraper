from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news_scrapper.spiders.techcrunch_spider import TechCrunchSpider
from news_scrapper.spiders.eastasiaforum_spider import EastasiaforumSpider
from news_scrapper.spiders.thepostmillennial_spider import ThepostmillennialSpider
from news_scrapper.spiders.RssFeedParser import RssfeedparserSpider
from news_scrapper.spiders.vancouversun_spider import VancouversunSpider
from news_scrapper.spiders.unnews_spider import UnNewsSpider



process = CrawlerProcess(get_project_settings())
process.crawl(UnNewsSpider)
process.start()