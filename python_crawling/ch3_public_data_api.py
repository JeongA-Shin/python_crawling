'''
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('serviceKey') : '인증키(URL Encode)', quote_plus('returnType') : 'xml', quote_plus('numOfRows') : '100', quote_plus('pageNo') : '1', quote_plus('year') : '2020', quote_plus('itemCode') : 'PM10' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body


key=StHx15%2FPZFKIJvR5AtCu8uyowAtnEYHpAXR%2B5XYYN6OWDt%2BCz15z%2Fxn%2FDiV%2FLN9%2BY5YSPZUPUnCq982CiBupmw%3D%3D
url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?Servicekey=StHx15%2FPZFKIJvR5AtCu8uyowAtnEYHpAXR%2B5XYYN6OWDt%2BCz15z%2Fxn%2FDiV%2FLN9%2BY5YSPZUPUnCq982CiBupmw%3D%3D&returnType=xml&numOfRows=10&pageNo=1&year=2020&itemCode=PM10'
'''