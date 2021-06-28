import requests
from bs4 import BeautifulSoup

res=requests.get("https://finance.naver.com/")
soup=BeautifulSoup(res.content,'html.parser')

stocks100=soup.select('#_topItems1 > tr')

for item in stocks100:
    result=''
    result+=item.find('a').get_text()+' '
    statistics=item.find_all('td')
    for num in statistics:
        result+=num.get_text()
        result+=' '
    print(result)