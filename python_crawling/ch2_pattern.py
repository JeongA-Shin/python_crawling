# 크롤링 핵심 코드 패턴

#1. 라이브러리 임포트
import requests # requests:웹페이지 가져오기 라이브러리
from bs4 import BeautifulSoup #bs4(BeautifulSoup):requests 라이브러리로 가져온 웹 페이지를 분석/추출하는 라이브러리
#bs4라이브러리에서 BeautifulSoup라는 클래스를 가져와서 쓰는 것

#2. 웹페이지 가져오기-request 라이브러리에서 get메서드를 쓴 것 // 해당 url의 html이 특수한 형태로 res변수에 넣어지는 것
res=requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%8C%80%ED%95%99%EA%B5%90') 
#3. 웹페이지 파싱하기 -bs4를 쓰면 html을 바로 파싱 가능 - soup에서는 parser로 분석한 정보들(구조화된 정보들)이 들어가 있음
soup=BeautifulSoup(res.content,'html.parser')  #여러가지 parser 중에 웹 페이지가 html로 구성되어있으므로 html.parser을 적용
#4. 필요한 부분의 데이터만 추출하기
mydata=soup.find("title") #원하는 부분 지정  #<title>대학교 : 네이버 통합검색</title> 이렇게 태그까지 mydata 안에 들어간 거임
#5. 추출한 데이터 활용하기
print(mydata.get_text())  # get_text()를 통해 태그를 떼고, text만 추출