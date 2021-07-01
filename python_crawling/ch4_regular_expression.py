#regular expression(정규 표현식):복잡한 문자열을 처리할 때 사용하는 기법으로, 파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다
#특수 문자를 써서 특정 패턴을 나타낸다.
''' 예제)
import re
string="(Dave)"
re.sub('[^A-Za-z0-9]','',string) # (주어진 string문자열에서) 문자, 숫자가 아닌 데이터를 찾아서 ''로 대체해라(즉 삭제해라) #'Dave'
[^A-Za-z0-9] 해석: 대문자 A-Z까지(A-Z), 소문자 a부터 z까지(a-z), 그리고 0부터 9까지(0-9)가 아닌!(^는 not의 의미) 문자들은 ''로 바꿔라(sub)
따라서 (Dave)에서 (는 대문자 A-Z까지(A-Z), 소문자 a부터 z까지(a-z), 그리고 0부터 9까지에 해당되지 않으므로!''로 대체됨-->')'도 마찬가지

string.replace('(','').replace(')','')이렇게 해도 되긴 하는데, 위의 정규 표현식이 더 간단하게 표현됨, 그리고 일일히 replace로 처리 못하는 경우가 
더 많으므로 정규 표현식을 쓰는 거임

1)문자열
[a-zA-Z] : 알파벳 모두
[0-9] : 숫자

\d - 숫자와 매치, [0-9]와 동일한 표현식이다.
\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.
(대문자로 사용된 것은 소문자의 반대임)

2)Dot(.)
정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미한다.
a.b ==> "a + 모든문자 중 단 하나 + b"  ----> .자리에 다른 문자가 2개 이상은 들어가면 안 되고, 아예 아무것도 안 들어가는 것도 안 됨. 무조건 하나
ex)aab,abb,acb,a0b
만약 정규표현식의 Dot이 아니라 그냥 문자 그대로 .을 하고 싶으면 [.] 혹은 \.으로 표시한다.
ex) a[.]b은 그냥  "a.b" 문자열과 매치되고, "a0b" 문자열과는 매치되지 않는다.
즉, 문자 클래스([]) 내에 Dot(.) 메타 문자가 사용된다면 이것은 "모든 문자"라는 의미가 아닌 문자 . 그대로를 의미한다. 혼동하지 않도록 주의하자.

import re
pattern=re.compile('D.A')
pattern.search("DAA") #DAA가 D.A에(pattern변수와) 들어 맞는지를 확인, 불일치면 아무것도 나오지 않고, 맞으면 <_src ..... match="DAA">라는 값이 출력됨

string="DDA DIA DDA DA"
re.sub('D.A','Dave',string)  # string 안에서 D.A에 해당되는 것(정규 표현식 D.A 패턴으로 표현되는 것)은 Dave로 바꾸기(sub)


3)반복 ?,*,+
3-1)? 
ab?c 의 의미: "a + b(는 있어도 되고 없어도 된다) + c"  ex)ac,abc
3-2)*
앞문자가 0번 또는 그 이상 반복되는 패턴 
ex) ca*t  여기에서 사용한 *은 * 바로 앞에 있는 문자 a가 0부터 무한대로 반복될 수 있다는 의미이다. ex)ct,cat,caaat
3-3)+
+는 최소 1번 이상 반복될 때 사용(). 즉 *가 반복 횟수 0부터라면 +는 반복 횟수 1부터)
ex) ca+t의 의미: "c + a(1번 이상 반복) + t"  ex) ct는 매치 안 됨,cat,caat

import res
pattern=res.compile('DA?C') 
pattern.search('DA') -> pattern과 match됨


4)또다른 반복 표현:{n},{m,n}
{ }메타 문자를 사용하면 반복 횟수를 고정할 수 있다. {m, n} 정규식을 사용하면 반복 횟수가 m부터 n까지 매치할 수 있다. 
!! m 또는 n을 생략할 수도 있다. 만약 {3,}처럼 사용하면 반복 횟수가 3 이상인 경우이고 {,3}처럼 사용하면 반복 횟수가 3 이하를 의미한다. 
생략된 m은 0과 동일하며, 생략된 n은 무한대(2억 개 미만)의 의미를 갖는다.
({1,}은 +와 동일하고, {0,}은 *와 동일하다.)
4-1) {m}
ca{2}t 의미: "c + a(반드시 2번 반복) + t" // a가 반드시 2개
ex)cat은 match되지 않음, caat은 match됨
4-2){m,n}
ca{2,5}t 의미: "c + a(2~5회 반복) + t"
ex)cat은 match되지 않음, caat은 match,caaat도 match됨

5)[]괄호: 괄호 안에 들어가는 문자가 해당 패턴에 들어있는지
pattern=re.complie('[abcdefgABCDEFG]') a or b or c or d or....g or A or B or C or....G 중 하나라도 있으면 search하면match됨
pattern.search("a1234") :a가 있으므로 match

6)하이픈(-)을 이용하면 전체범위를 나타낼 수 있음
[a-d]는 a,b,c,d 중 하나가 들어있는 패턴임
pattern=re.compile('[a-z]')  : a~z 중 하나라도 들어있으면 match되게끔하는 거임
pattern.search("k1234") #k때문에 match됨
[a-zA-Z0-9] :대문자 전체, 소문자 전체, 숫자 0에서 9에 하나라도 해당되면 됨
문자 클래스([ ]) 안에는 어떤 문자나 메타 문자도 사용할수 있지만 주의해야 할 메타 문자가 1가지 있다. 
그것은 바로 ^인데, 문자 클래스 안에 ^ 메타 문자를 사용할 경우에는 반대(not)라는 의미를 갖는다. 
예를 들어 [^0-9]라는 정규 표현식은 숫자가 아닌 문자만 매치된다.
#한글이 있는지 확인하려면?
pattern=re.compile('[가-힣]') 가-힣: 한글의 전체 범위
pattern.search("안abc") '안'때문에 match 됨

7) 각종 Method
Method	    목적
match()	    문자열의 처음부터 정규식과 매치되는지 조사한다.(전체가 완전히 match되어야 함)
            (예)pattern=re.compile('[a-z]+')인데 pattern.match('Dave')이면 D때문에 MATCH안 됨
search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다.(한 글자라도 범위에 match되는 게 있기만 하면 됨) 
            (예)pattern=re.compile('[a-z]+')인데 pattern.match('Dave')이면 ave 때문에 match됨
findall()	정규식과 매치되는 모든 문자열(substring)을 "리스트로" 돌려준다.
            예)  import re   
            p = re.compile('[a-z]+') 
            result = p.findall("Life is too Short")
            print(result)
            ##['ife', 'is', 'too', 'hort']
finditer()	정규식과 매치되는 모든 문자열(substring)을 "반복 가능한 객체"로 돌려준다.
split()     import re
            p = re.compile(':') 
            result = p.split("I:human")
            print(result)
            ##['I','human']
sub()       1)import re
              pattern2=re.compile('-')
              subed=pattern2.sub('*','9876-9876') #sub(바꿀 문자열, 본래 문자열)
            2)subed=re.sub('-','*','9876-9876') #sub(정규표현식, 바꿀문자열,본래 문자열)
            

'''

import openpyxl
import re #정규 표현식을 위해 import해야하는 라이브러리

regex=re.compile(' [A-Za-z]+\.')

#엑셀파일 열기
work_book=openpyxl.load_workbook('train.xlsx')
#현재 active sheet 열기
work_sheet=work_book.active
#work_sheet.rows는 해당 시트의 모든 행을 객체로 가지고 있음
for each_row in work_sheet.rows:
    print(each_row[3].value) #each_row[3]은 승객의 이름에 해당됨
    print(regex.findall(each_row[3].value))

work_book.close()