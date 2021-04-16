# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from news_scrapper.settings import ITEM_OUTPUT_PATH

import json

class JsonWriterPipeline:

    def open_spider(self , spider):
        self.file = open(ITEM_OUTPUT_PATH , 'w')

    def close_spider(self , spide):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + '\n'
        self.file.write(line)
        return item
