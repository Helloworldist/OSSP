import pypiwin32_system32
import scrapy
import sys
from scrapy.spider import Spider
from scrapy.selector import Selector
#from APT2U.items import Apt2UItem
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
#sys.setdefaultencoding('utf-8')

from scrapy.item import Item, Field


class WebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area = scrapy.Field()    # 영화
    content = scrapy.Field()       # 평
    company = scrapy.Field()    # 평점
    pay = scrapy.Field()  # 작성자
    time = scrapy.Field()  # 날짜


class WebSpider(scrapy.Spider):
    name="alba"
    allowed_domains = ["www.albamon.com"]   # 크롤링할 최상위 도메인
    start_urls = ["http://www.albamon.com/list/gi/mon_area.asp?scd=E000&gcd=E000"] # 실제 크롤링 대상 주소

    def parse(self, response):
        hxs = HtmlXPathSelector(response)    # 지정된 주소에서 전체 소스코드를 가져옴
        sites = hxs.select('//tbody/td[@id="dev_preview__53572101"]')
        items = []   # 데이터를 item별로 구별해서 담을 리스트

        for site in sites:
            item = WebItem()
            item['area']= site.xpath('//*[@id="dev_preview__53572101"]/td[1]/text()').extract()[0]
            item['pay']=site.xpath('//*[@id="dev_preview__53572101"]/td[4]/text()').extract()
            items.append(item)
            return items

