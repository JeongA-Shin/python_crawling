import requests
from bs4 import BeautifulSoup

'''
res=requests.get('https://search.shopping.naver.com/best100v2/main.nhn')
soup=BeautifulSoup(res.content,'html.parser')

top100=soup.select('#popular_srch_lst li span.txt')

for i in top100:
    print(i.get_text())
    '''

res=requests.get('https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000')
soup=BeautifulSoup(res.content,'html.parser')


clothes=soup.select('#productListArea > ul > li > p > a')

for item in clothes:
    print(item.get_text())