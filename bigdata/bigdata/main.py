# 구현 방향
# 사용자로부터 항목 선택을 받아 명령 실행
#
#

from scrapy import cmdline

# 크롤링
cmdline.execute("scrapy crawl Web".split())

# 크롤링 후 파일 생성
cmdline.execute("scrapy crawl Web -o Web.csv".split())
cmdline.execute("scrapy crawl Web -o Web.json".split())
cmdline.execute("scrapy crawl Web -o Web.xml".split())