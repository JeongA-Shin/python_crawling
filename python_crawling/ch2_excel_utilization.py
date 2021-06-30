import openpyxl
import requests
from bs4 import BeautifulSoup

# ch2_crawling_excel.py 참고

def write_excel_template(filename,sheetname,listdata): #(저장하고 싶은 엑셀 파일이름,저장할 sheet name, 저장할 data(리스트의 요소들이 리스트인 형태))
    #listdata: [[list1],[list2],[list3]....] 이런 형태
    excel_file=openpyxl.Workbook()
    excel_sheet=excel_file.active

    excel_sheet.column_dimensions['A'].width=100 #A열 크기 지정
    excel_sheet.column_dimensions['B'].width=40


    if sheetname !='': #딱히 sheet이름 지정 안 한거면 그냥 default로 넘어가고, 지정한 게 있으면 그걸로 바꿔줌
        excel_sheet.title=sheetname

    for item in listdata:
        excel_sheet.append(item) #item도 하나의 리스트임
    
    excel_file.save(filename)
    excel_file.close()

    

product_lists=list() #리스트 생성

for page_num in range(0,10):
    if page_num==0: res=requests.get("https://davelee-fun.github.io/")
    else:
        res=requests.get("https://davelee-fun.github.io/page"+str(page_num+1))
    
    soup=BeautifulSoup(res.content,'html.parser')
    data=soup.select('div.card') #select는 리스트로 반환

    for item in data:
        product_name=item.select_one('div.card-body h4.card-text')
        product_date=item.select_one('div.wrapfooter span.post-date')
        product_info=[product_name.get_text().lstrip(),product_date.get_text().lstrip()] #각 상품마다 그에 해당되는 정보의 list를 각각 생성
        product_lists.append(product_info)

write_excel_template('result.xlsx','상품정보',product_lists)