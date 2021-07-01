#공공데이터 api- xml형태로 받음
#xml: 특정 목적에 따라 데이터를 태그로 감싸서 마크업하는 범용적인 포맷
#예) html
#xml의 기본 구조: <태그 속성="속성값">내용</태그>
#html과는 다르게 xml은 내가 특정 목적에 따라 임의로 태그를 정함(html은 약속된 태그들을 사용)
#예) <product id="1001" price="3000">32인치 LCD 모니터 </product>   -> 다른 태그 안에 들어갈 수도 있음 (아래 예시-item이라는 큰 태그 안에 그룹화됨)
#예) <item><product id="1001" price="3000">32인치 LCD 모니터 </product> <product id="1002" price="3100">34인치 LCD 모니터 </product> </item>


#xml 파싱하기 - html과 구조가 똑같으므로 html 파싱할 때와 똑같이 해주면 됨
import requests
from bs4 import BeautifulSoup

service_key='StHx15%2FPZFKIJvR5AtCu8uyowAtnEYHpAXR%2B5XYYN6OWDt%2BCz15z%2Fxn%2FDiV%2FLN9%2BY5YSPZUPUnCq982CiBupmw%3D%3D'
params='&returnType=xml&numOfRows=10&pageNo=1&year=2020&itemCode=PM10' #서비스 키 제외한 각종 params

open_api='http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?serviceKey='+service_key+params

res=requests.get(open_api) #naver open api와는 다르게 service key가 이미 open api의 url에 들어갔기 때문에, 별도로 headers에 넣지 않아도 됨
#print(res.text)  #문자열로 보기 좋게 반환. text()가 아님! 그냥 text #현재 xml로 반환됨

soup=BeautifulSoup(res.content,'html.parser')
data=soup.find_all('item')

for element in data:
    district=element.find('districtname').get_text()
    issue=element.find('issuegbn').get_text()
    print(district,issue)

