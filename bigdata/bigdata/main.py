# 구현 방향
# 사용자로부터 항목 선택을 받아 명령 실행
# 1. 크롤링할 페이지 입력
# 2. Xpath 설정
# 3. 명령실행선택

# 변수부
# 1. root_page - 최상위 페이지 변수, sub_page
# 2. main_structure - Xpath 상위 구조, sub_structure1~7 - Xpath 하부 구조
main_structure = ''
sub_structure1 = ''
sub_structure2 = ''
sub_structure3 = ''
sub_structure4 = ''
sub_structure5 = ''
sub_structure6 = ''
sub_structure7 = ''
sub_arr = [sub_structure1, sub_structure2, sub_structure3, sub_structure4,
           sub_structure5, sub_structure6, sub_structure7]

# 실행부
print("="*50)

# 1단계
print("데이터 파싱을 위해 몇가지 단계가 필요합니다.")
root_page = input("1.1 크롤링할 루트페이지 입력 : ")   # 관계 없는 페이지로의 리다이렉트 방지
sub_page = input("1.2 크롤링할 서브페이지 입력 : ")    # 데이터를 추출할 세부 페이지 입력

# 2단계
main_structure = input("2.1 메인 Xpath 설정 :")
print("2.2 서브 Xpath 설정")
for i in range(1, 8, 1):
    xpath = input("%d번째 필드에 대한 Xpath 입력 : " % i)
    sub_arr[i-1] = xpath

# 크롤링 후 파일 생성
#cmdline.execute("scrapy crawl Web -o Web.csv".split())
#cmdline.execute("scrapy crawl Web -o Web.json".split())
#cmdline.execute("scrapy crawl Web -o Web.xml".split())