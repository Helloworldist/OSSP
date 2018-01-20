import pypiwin32_system32
import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field
from bigdata.bigdata import main
from bigdata.bigdata import items
from bigdata.bigdata.main import f_count
from bigdata.bigdata.main import page

class WebSpider(scrapy.Spider):
    name = "web"    # 고유 스파이더 명
    allowed_domains = [main.root_page]   # 크롤링할 최상위 도메인
    #start_urls = [main.sub_page] # 실제 크롤링 대상 주소

    # 크롤링 대상 주소 범위
    def start_requests(self):
       for i in range(1, int(page+1), 1):
          yield scrapy.Request(main.sub_page + str(i), self.parse)

    def parse(self, response):
        for select in response.xpath(main.main_structure):  # 파싱할 부분의 상위 구조
            item = items.WebItem()      # 컨테이너 호출
            for i in range(1, int(f_count+1)):
                if main.sub_arr[i-1] is '':
                    item['record'+str(i)] = ''
                else:
                    item['record'+str(i)] = select.xpath(main.sub_arr[i-1]).extract_first()

            print('=' * 50)
            for i in range(1, int(f_count+1)):
                print('레코드'+str(i)+" : "+item['record'+str(i)])
            print('=' * 50)
            yield item
