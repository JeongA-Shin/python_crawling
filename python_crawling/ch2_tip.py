import requests
from bs4 import BeautifulSoup

res=requests.get("https://davelee-fun.github.io/blog/crawl_test")
soup=BeautifulSoup(res.content,'html.parser')

section=soup.find('ul',id='dev_course_list') #태그와 id로 추출

titles=section.find_all('li','course') #태그와 class

''' 내가 한 것 : split함수 활용을 제대로 못 함
for i in titles:
    data=i.get_text().split() #split된 결과가 리스트로 반환됨
    length=len(data)
    sentence=''
    for j in range(2,length-1):
        sentence+=data[j]
        sentence+=' '
    print(sentence)
'''


''' split, strip함수 활용한 것
for title in titles:
    #title.get_text().split('[') : [ 를 기준으로 문장이 두 부분으로! 나뉘게 됨
    #title.get_text().split('[')[0] 따라서 [0]이므로 []이전의 문장만 해당되게 됨
    print(((title.get_text().split('[')[0]).split('-')[1]).lstrip())
    '''

#그런데 위의 내용에서 출력된 제목들에 번호를 매기고 싶다면? -- 1부터 시작하도록
for index,title in enumerate(titles):
    print(index+1,((title.get_text().split('[')[0]).split('-')[1]).lstrip())


