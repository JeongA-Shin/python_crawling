#import requests
from bs4 import BeautifulSoup

html="""
<!DOCTYPE html>
<html>
    <head>
        <body>
            <h1 id="title">크롤링이란</h1>
            <p class='cssstyle'>웹 페이지에서 필요한 데이터만을 추출하는 것</p>
            <p id='body' align='center'>파이썬을 중심으로</p>
        </body>
    </head>
</html>
"""

soup=BeautifulSoup(html,'html.parser')
data=soup.find('h1') #태그로 검색하는 방법
#(태그가 같은 경우) 속성으로 추출하기 
data2=soup.find('p',class_='cssstyle') #1 클래스로 찾기, 객체 지향에서 말하는 class와의 혼동을 피하기 위해서 class_ 이렇게 underbar를 해줌
data3=soup.find('p','cssstyle') #2 클래스로 찾기, key값이 딱히 없으면 class로 인식함
data4=soup.find('p',attrs={'align':'center'}) #3 속성으로 찾기 attrs={'align':'center','id':'body'} 속성 여러 개를 지정해도 됨
data5=soup.find(id='body') #4 id로 찾기
print(data.get_text()) #data.string()으로도 가능
print(data2.get_text())
print(data3.get_text())
print(data4.get_text())
print(data5.get_text())

#해당되는 것 "모두" 가져오기: find_all(), ""리스트 형태""로 넘겨줌, 그냥 find면 해당되는 첫 번째만 가져옴
contents=soup.find_all('p')

for i in contents: #contents는 현재 리스트임
    print(i.get_text())  #i.string()으로 하면 오류남



