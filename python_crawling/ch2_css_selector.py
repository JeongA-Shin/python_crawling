import requests
from bs4 import BeautifulSoup

res=requests.get("https://davelee-fun.github.io/blog/crawl_test_css.html")
soup=BeautifulSoup(res.content,'html.parser')

items=soup.select('ul li') #select는 리스트로 반환함! 

for item in items:
    print(item.get_text())

'''select() 활용법에 따른 파라미터
1. 태그만 넣기 예)select('li')
2. 하위태그 선택 예) select('html body h1')
2-1. 바로 아래 하위태그인 경우 > 쓰기 예)select('ul > li')
2-3. css class이름으로 검색: .클래스 이름으로 검색 예) select('.course')
2-4. id이름으로 검색 예) select('#start')
2-5. 하나의 태그에 여러 클래스가 있는 경우 예)select(태그.클래스이름.클래스이름) select('li.course.paid')
2-6. 복합 예) select('ul#body_course_list li.course') body_course_list라는 클래스명이 있는 ul태그가 있고, 하위태그인 li태그 중 클래스 명이 course인 것
2-7. 리스트가 아니라 하나의 요소만 필요하면 select_one()을 써준다 예)select_one('ul#dev_course_list>li.course.paid')
     select()만 쓰면 리스트가 반환되고, select_one()을 쓰면 그 리스트 중 첫 번째 요소만 반환된다.

'''