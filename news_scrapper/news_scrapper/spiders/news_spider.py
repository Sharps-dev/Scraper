import scrapy 

class NewsSpider(scrapy.Spider):
    name='news'

    def start_requests(self):
        urls = [
            'https://www.nytimes.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
        
    def parse(self , response):
        filename = 'test.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')