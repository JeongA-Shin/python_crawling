# http 응답코드
'''
http 프로토콜 규격에 따라서, http에서 사용하는 프레임에 응답코드를 넣는 구역이 있음
http 프로토콜에 따라, 응답코드가 200이면 정상 응답, 그렇지 않다면 무언가 문제가 있음
requests라이브러리의 경우, requests.get()의 !!!!!리턴변수.status_code!!!!!에서 응답 코드를 확인할 수 있음
아래 코드는 그 예시임
'''
import requests
from bs4 import BeautifulSoup

res=requests.get("https://davelee-fun.github.io/xxxxx")

if res.status_code != 200: print("해당 페이지가 없거나 문제가 생김")
else: 
    soup=BeautifulSoup(res.content,'html.parser')
    data=soup.select('section.featured-posts > div.row > div> div > div > div.col-12.col-md-12.col-lg-7 > div > div > div.card-body > h4')

    for i in data:
        print(i.get_text())


print('\n')

# 여러 페이지를 한 번에 크롤링하는 기법 ex)글이 계속 추가되는 사이트의 게시판 긁어오기
# 여기서는 10페이지만 크롤링함
for page_num in range(0,10):
    if page_num==0: res=requests.get("https://davelee-fun.github.io/")
    else:
        res=requests.get("https://davelee-fun.github.io/page"+str(page_num+1))
    
    soup=BeautifulSoup(res.content,'html.parser')
    data=soup.select('h4.card-text')

    for item in data:
        print(item.get_text())