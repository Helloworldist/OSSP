import rpy2.robjects.packages as rpackages  # rpy2의 패키지 모듈 임포트
from rpy2.robjects.vectors import StrVector # R 스트링 벡터
import rpy2.robjects as robjects
from rpy2.robjects import r
import os

utils=rpackages.importr('utils')    # R 기본 utils 패키지 임포트
utils.chooseCRANmirror(ind=1)   # 리스트에서 첫번째 미러 선택

packname=('wordcloud', 'ggplot2')   # 다운로드 할 패키지

utils.install_packages(StrVector(packname))     # R 유틸리티 패키지로 packname의 패키지 설치

wc=rpackages.importr('wordcloud')

obj=robjects.r('c("hi", "bye", "no")')
num=robjects.r('c(1,32,4)')

base_dir = 'E:\webcrawl\webcrawl'   # 파일의 위치
input_file = 'info' # 파일 명
output_file = 'test.png'    # 출력 파일 명
input_mat = utils.read_csv(os.path.join(base_dir,
                                        input_file +'.csv'),
                           fileEncoding="euc-kr", fill=False)   # .csv 형식의 파일 읽어오기

print(input_mat)
