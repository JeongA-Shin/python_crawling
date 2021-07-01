import requests
import pprint
from bs4 import BeautifulSoup

import openpyxl


excel_file=openpyxl.Workbook()
excel_sheet=excel_file.active
excel_sheet.column_dimensions['B'].width=100
excel_sheet.column_dimensions['C'].width=100
excel_sheet.append(["랭킹","제목","링크"])#이렇게 행으로 저장됨 (a1,b1,c1) #엑셀의 append는 반드시! """리스트"""가 파라미터로 들어가야 함!!

client_id="YqapK6EjxIBuZXwS8XoW"
client_secret="35Owa_sX5Q"

start=1
num=0
for index in range(10):
    start_number=start+(index*100)
    naver_open_api="https://openapi.naver.com/v1/search/shop.json?query=bag&display=100&start="+str(start_number)
    header_params={"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret} 
    res=requests.get(naver_open_api,headers=header_params)
    if res.status_code==200:
        data=res.json()
        items=data["items"]
        for item in items:
            num+=1
            #print(num,item["title"],item["link"])
            excel_sheet.append([num,item["title"],item["link"]])  #이렇게 그대로 엑셀에 행으로 추가되는 것
    else: print("ERROR CODE: ",res.status_code)

excel_file.save("bag_rate.xlsx")
excel_file.close()

