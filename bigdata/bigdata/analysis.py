# 구현 방향
# 1. 파일 선택
# 2. 분석, 시각화

from rpy2.robjects import r
import os
import rpy2.robjects.packages as rpackages
import rpy2.robjects as robj
# R 기본 패키지
utils=rpackages.importr('utils')
file_path = input("파일이 있는 경로를 입력하세요(양 끝에 \"입력) : ")
file_name = input("파일 이름을 입력하세요(양 끝에 \" 및 확장자 입력) : ")

# 경로 지정 및 관련 라이브러리 호출
robj.r('setwd('+file_path+')')
robj.r('Sys.setenv(JAVA_HOME="C:/Program Files (x86)/Java/jre1.8.0_161")')
r.library('rJava')
r.library('wordcloud')
r.library('RColorBrewer')
r.library('KoNLP')
#robj.r('useSejongDic()')

# 데이터 분석 - 파일 불러오기, 명사 추출, 및 기타 필터링
print("데이터 분석 중입니다...[파일 불러오기]")
robj.r('data1<-readLines('+file_name+', encoding = "utf-8")')
print("데이터 분석 중입니다...[명사 추출 및 필터링]")
robj.r('data2<-sapply(data1, extractNoun, USE.NAMES = F)')
robj.r('data3<-unlist(data2)')
robj.r('data3<-Filter(function(x){nchar(x)>=2}, data3)')
robj.r('data3<-gsub("\\\\d+","",data3)')
robj.r('data3<-gsub("\\\\(","",data3)')
robj.r('data3<-gsub("\\\\)","",data3)')
robj.r('data3<-gsub("\\\\[","",data3)')
robj.r('data3<-gsub("\\\\]","",data3)')
robj.r('data3<-gsub("오전","",data3)')
robj.r('data3<-gsub("오후","",data3)')
robj.r('data3<-gsub("사진","",data3)')
robj.r('data3<-gsub("kr","",data3)')

# 데이터 분석 - 공백 제거 및 단어 빈도 확인
print("데이터 분석 중입니다...[공백 제거 및 빈도 카운트]")
robj.r('write(unlist(data3), "tmp_eData.txt")')
robj.r('data4<-read.table("tmp_eData.txt")')
robj.r('wordcount<-table(data4)')
robj.r('palette<-brewer.pal(9,"Set1")')

# 데이터 시각화 - 워드클라우드 생성 및 저장
print("데이터 시각화 중입니다...[워드클라우딩]")
robj.r('png(filename="E:/wordcloud.png", bg="white")')
robj.r('wordcloud(names(wordcount), freq=wordcount, scale=c(6,2), rot.per = 0.1, min.freq = 1, random.order = F, random.color = T, colors = palette)')
robj.r('dev.off()')
print("데이터 분석 및 시각화 완료")
