import re
import requests
from bs4 import BeautifulSoup
import openpyxl

res=requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01')
soup=BeautifulSoup(res.content,'html.parser')

excel_file=openpyxl.Workbook()
excel_sheet=excel_file.active
excel_sheet.title="final_crawling" #굳이 안 해도 되긴 하지만, sheet 이름 지정해줌
excel_sheet.append(["순위","이름","가격","회사"]) #append는 반드시!! 리스트 형태로 추가해야함. 이거 까먹어서 에러났음

excel_sheet.column_dimensions['B'].width=100 #B열 크기 지정



items=soup.select('#gBestWrap > div > div > div > ul > li') #일단 전체 section


for index,item in enumerate(items):# 전체 section에서 또 하나의 section씩(하나의 상품씩) 가져옴
    if(item.select_one('a.itemname') is None):pass
    elif(item.select_one('div.s-price strong span')==None):pass # if경우와 elif경우를 |연산하지 않은 이유: None은 아예 그런 연산 자체가 불가능해서
    else:
        title=item.select_one('a.itemname').get_text()
        price=item.select_one('div.s-price strong span').get_text()
        href=item.select_one('a.itemname')['href']  ## 반드시 key값에 ' '해줘야함! key는 그냥 문자열임!
        #href는 태그가 아니라! 'a.itemname'안의 "속성"이므로 딕셔너리처럼 처리해줘야함
        resh=requests.get(href) #각 아이템에 연결되어있는 페이지(href)를 다시 각각 크롤링 ##크롤링 안에서 또 크롤링
        souph=BeautifulSoup(resh.content,'html.parser')
        company=souph.select_one('#container > div.item-topinfowrap > div.item-topinfo.item-topinfo--additional > div.item-topinfo_headline > p > span.text__seller > a').get_text()
        excel_sheet.append([index-4,title,price,company])
        print(index-4,title," ", price," ",company)


excel_file.save("final_crawling.xlsx")
excel_file.close()

''' 처음 다섯 줄에 nonetype이 나와서 get_text()로 얻기가 아예 불가능함
근데 이거는 너무 일일히? 제외하는 거 같아서 아예 위의 코드처럼 None인 경우만 뺌
index=0
for index, item in enumerate(items):
    if(index<5): index+=1
    else:
        title=item.select_one('a.itemname').get_text()
        price=item.select_one('div.s-price strong span').get_text()
        print(index-4,title," ", price)'''