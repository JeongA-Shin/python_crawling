#기존의 엑셀파일 읽기
import openpyxl

excel_file=openpyxl.load_workbook('result.xlsx')


print(excel_file.sheetnames) #상품정보 #sheet 이름을 확인할 수 있음

excel_sheet=excel_file['상품정보']#해당 엑셀 파일 안에 있는 특정 엑셀 시트만 가져오기

#sheet안의 데이터 읽기
for item in excel_sheet.rows: #각 item에는 한 row의 각 셀에 있는 데이터를 가져옴
    print(item[0].value, item[1].value) #각 행의 열은 [0],[1]처럼 인덱스를 통해 선택 #.value를 통해 실제 데이터를 가져올 수 있음


#파일 작업(읽고 쓰기)이 끝난 거니까 반드시 clsoe해줘야 함
excel_file.close()