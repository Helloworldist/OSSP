import pypiwin32_system32
import scrapy
from bigdata.bigdata.items import Article

class WebSpider(scrapy.Spider):
    name = "Web"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Main_Page",
                  "https://en.wikipedia.org/wiki/Python_(programming_language)"
            ]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text(0)')[0].extract()
        print("Title is: "+title)
        item['title'] = title
        return item