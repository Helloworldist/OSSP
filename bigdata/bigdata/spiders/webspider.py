import pypiwin32_system32
import scrapy
import re
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
#sys.setdefaultencoding('utf-8')

from scrapy.item import Item, Field


class WebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    subject = scrapy.Field()
    category = scrapy.Field()
    condition = scrapy.Field()
    date = scrapy.Field()


class WebSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["www.incruit.com"]   # 크롤링할 최상위 도메인
    start_urls = ["http://job.incruit.com/jobdb_list/searchjob.asp?ct=3&ty=2&cd=15"] # 실제 크롤링 대상 주소

    #def start_requests(self):
     #   for i in range(1, 5, 1):
      #      yield scrapy.Request("http://movie.naver.com/movie/point/af/list.nhn?page=1" % i, self.parse)

    def parse(self, response):
        for select in response.xpath('//tbody/tr'):
            item = WebItem()
            item['company'] = select.xpath('th[@scope="row"]/div[@class="companys check_companys"]/div[@class="check_list_r"]/span[@class="links"]/a/text()').extract_first()
            item['subject'] = select.xpath('td[@valign="top"]/div[@class="subjects"]/span[@class="accent"]/a/text()').extract_first()
            item['category'] = select.xpath('td[@valign="top"]/div[@class="subjects"]/p[@class="details_txts firstChild"]/em/text()').extract_first()
            item['condition'] = select.xpath('td[@valign="top"]/div[@class="subjects termArea"]/p[@class="details_txts firstChild"]/em/text()').extract_first()
            item['date'] = select.xpath('td[@valign="top"]/div[@class="ddays"]/p/text()').extract_first()

            print( '='*50)
            print('기업명 : ' + item['company'])
            print('채용제목 : ' + item['subject'])
            print('분야 : ' + item['category'])
            print('근무조건 : ' + item['condition'])
            print('마감일 : ' + item['date'])
            print('='*50)
            yield item



        #hxs = HtmlXPathSelector(response)    # 지정된 주소에서 전체 소스코드를 가져옴
        #sites = hxs.select('//tbody/td[@id="dev_preview__53572101"]')
        #items = []   # 데이터를 item별로 구별해서 담을 리스트

        #for site in sites:
         #   item = WebItem()
          #  item['area']= site.xpath('//*[@id="dev_preview__53572101"]/td[1]/text()').extract()[0]
           # item['pay']=site.xpath('//*[@id="dev_preview__53572101"]/td[4]/text()').extract()
            #items.append(item)
            #return items

