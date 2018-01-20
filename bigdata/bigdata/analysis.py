import rpy2.robjects.packages as rpackages  # rpy2의 패키지 모듈 임포트
from rpy2.robjects.vectors import StrVector # R 스트링 벡터
import rpy2.robjects as robj
from rpy2.robjects import r
import os

utils=rpackages.importr('utils')    # R 기본 utils 패키지 임포트
utils.chooseCRANmirror(ind=1)   # 리스트에서 첫번째 미러 선택

packname=('wordcloud', 'ggplot2')   # 다운로드 할 패키지

# utils.install_packages(StrVector(packname))     # R 유틸리티 패키지로 packname의 패키지 설치

# 구현 방향
# 1. 파일 선택
# 2. 분석, 시각화

#base_dir = 'E:\webcrawl\webcrawl'
#input_file = 'news_test'
#output_file = 'test.png'
#input_mat = utils.read_csv(os.path.join(base_dir, input_file +'.csv')
#                           , fileEncoding="euc-kr")
#print(input_mat)

robj.r('setwd("E:/")')
robj.r('data<-read.csv("news2.csv", header=TRUE, fileEncoding="euc-kr", sep=",")')
#print(robj.r('data'))

a=robj.r('hi<-c(4214,312,234,551)')
b=robj.r('no<-c("Cat", "Dog", "Mouse", "Bear")')
robj.r('library(wordcloud)')
robj.r('library(RColorBrewer)')

robj.r('png(filename="E:/wc.png", bg="white")')
robj.r('wordcloud(no, hi, color="green3")')
robj.r('dev.off()')
print(a, b)

