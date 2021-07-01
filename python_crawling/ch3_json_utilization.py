#네이버 open api활용하기 - postman이 아니라 코드로 json받아오기

import requests
import pprint  #json을 사람이 보기 편한 형태로 출력함(한 줄로만 쭉 출력하는게 아니라, postman에서 볼 수 있는 것처럼 출력해줌)
from bs4 import BeautifulSoup
from requests import status_codes

client_id="YqapK6EjxIBuZXwS8XoW"
client_secret="35Owa_sX5Q"

naver_open_api="https://openapi.naver.com/v1/search/news.json?query=android"
header_params={"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret} # 이것도 json임.
#네이버 오픈 api를 쓰기 위해 필요한 id와 secret을 header변수에 한 번에 넣어줌
res=requests.get(naver_open_api,headers=header_params) #headers=header_params # http 프로토콜에서는 프레임에 header부분이 있음 (header와 body)
#그런데 그 header 부분에 특정한 정보가 필요한데, 여기서는 client id와 clinet secret임


if(res.status_code == 200): #서버에서 정상적인 답을 줄 때
    #print(res.content)  #이렇게 하면 인코딩 때문에 사람이 해석하기 어렵고, 정리가 되지 않은 형태임

    data=res.json()#이렇게하면 json포맷으로 보기 좋게 정돈됨 #json을 받아오기

    #print(data["items"][0]["title"])
    '''pprint.pprint(data)  # pprint로 해주면 json을 사람이 보기 좋게 출력해줌'''
    for index,item in enumerate(data["items"]):
        print(index)
        print(item["title"])
        print(item["link"])
        print("\n")
else:
    print("Error code: ",status_codes)