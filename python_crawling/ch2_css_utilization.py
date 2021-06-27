import requests
from bs4 import BeautifulSoup

res=requests.get("https://www.naver.com/")
soup=BeautifulSoup(res.content,'html.parser')
data1=soup.find_all('li','category_item') #크롤링할 때, id로 찾는 게 아닌 이상은 태그도 반드시 표시해줘야 함!
data2=soup.find_all('strong','title elss') #태그를 먼저 표시해주고, 더 구체화시키도록 각종 속성들을 더 표시해주는 거임

for j in data1:
    print(j.get_text())

print('\n')
print('\n')

for i in data2:
    print(i.get_text())

