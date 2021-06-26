'''
#출력
print("hello world!");
# // 이 몫임 % 는 나머지

# 파이썬에서의 입력

data=input("how old are you?")
str1=int(data)
print(str1)



# 문자열 다루기
# 파이썬은 한 줄이 넘어가면 " " 만으로 처리 못 함. """ """ 으로 처리해줘야 함
lyrics="""We don't talk anymore
We don't talk anymore
We don't talk anymore
Like we used to do
We don't love anymore
What was all of it for?
Oh, we don't talk anymore
Like we used to do
I just heard you found the one you've been looking
"""
# 문자열 관련 함수
print(lyrics.count("anymore")) # lyric이라는 문자열 안에 anymore이라는 문자열(단어)가 얼마나 나오는지
print(len(lyrics)) #띄어쓰기 포함
print(lyrics.find('W')) # 문자열에서 s가 언제 제일 처음 나오는지( s의 제일 첫 인덱스)
print(lyrics.find('don\'t')) #  find는 단어도 찾을 수 있음( 단어를 이루는 글자 중 제일 첫 글자의 인덱스)
print(lyrics.replace("love","hate")) # 문자열의 특정 단어를 원하는 단어로 바꾸기(love를 hate로 바꾸기)

a = "Life is too short"
a.split() # 결과:['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':') # 결과: ['a', 'b', 'c', 'd']

",".join('abcd') # 결과: 'a,b,c,d'
",".join(['a', 'b', 'c', 'd']) # 문자열을 튜플로 처리한 것, 결과:'a,b,c,d'

a = "hi"
a.upper() # 대문자로 바꾸기 #'HI'

a = "HI"
a.lower() # 소문자로 바꾸기 #'hi'

# 특정 문자열 출력(slicing)
string1="python"
print(string1[0:3])

#특정 문자열 없애기
string2=" ... computer   "
print(string2.strip( )) # 공백 없앰 #rstrip(오른쪽 공백 없앰), lstrip(왼쪽 공백 없앰)있음

#출력 포맷과 입력
sentence="I have a {}, I have an {}."
print(sentence.format("pen","apple"))
print("I have a {0}, I have an {0}.".format("pen","apple")) # 이러면 모두 모두 0에 해당되는 pen만 들어가서 출력된다.

#format함수 자체를 활용하기
interest=0.087 
print(format(interest,".2f"))  #나는 해당 데이터를 소수 둘째자리까지만 보고 싶을 때

'''

'''
#데이터 구조 - 1.list
### 리스트 요소들은 여러가지 자료형들이 모두 섞일 수 있음 ### 문자열, int ,boolean 모두 한 리스트에서 요소가 될 수 있음 ["안녕",1,True]
location=[]# 빈 리스트 선언 location=list() 이렇게해도 같음
location=['서울시','경기도','인천시']
print(location) #['서울시','경기도','인천시'] 이렇게 그대로 출력됨
location.append("대전시")
location.append('부산시') # 요소 추가. 한 번에 하나만 가능
#특정 위치에 요소를 추가하고 싶을 때:insert
print(location)
location.insert(1,"대구시") #1번 인덱스자리에 대구시가 들어가고 기존 것들은 뒤로 다 밀림
print(location)
print(location[0]) # 서울시
print(location[0:2]) #['서울시','경기도'] 리스트 형태로 출력됨
location.remove('경기도') # 삭제
del location[0] # 삭제함수(삭제 명령어)
del location[2: ] # 슬라이싱을 통해 여러개를 한 번에 삭제 가능
print(location)
#리스트데이터 정렬: sort(), 역순으로 정렬:reverse()
# 리스트의 요소 바꾸기(수정)
list=["안녕","자두야"]
list[1]="앵두야" # 해당리스트변수[인덱스번호]=바꿀 데이터
print(list)
#리스트 더하기, 곱하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) #[1, 2, 3, 4, 5, 6]

a = [1, 2, 3]
print(a * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
len(a) #리스트의 길이

a = [1,2,3]
a.index(3) #2 #index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
a.index(1) #0
a.pop() # 3 #pop()은 리스트의 맨 "마지막" 요소를 돌려주고, 그 요소는 '삭제'한다.
a = [1,2,3]
a.pop(1) #2 단, pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다.
'''
a = [1,2,3,1]
a.count(1) #2 #count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수이다.

a = [1,2,3]
a.extend([4,5]) #a는 [1, 2, 3, 4, 5], extend는 +역할
b = [6, 7]
a.extend(b) #a는 [1, 2, 3, 4, 5, 6, 7] # a.extend([4, 5])는 a += [4, 5]와 동일하다.


#데이터구조- 2.tuple
t1 = ()
t2 = (1,) # 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다
t3 = (1, 2, 3)
t4 = 1, 2, 3 #괄호( )를 생략해도 무방
t5 = ('a', 'b', ('ab', 'cd'))
#튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
print(t3[1]) #2
#리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
#리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
#그 값이 항상 변하지 않기를 바란다면 튜플을 사용해야 한다. 수시로 그 값을 변화시켜야할 경우라면 리스트를 사용
#실제 프로그램에서는 값이 변경되는 형태의 변수가 훨씬 많기 때문에 평균적으로 튜플보다는 리스트를 더 많이 사용한다.
#튜플을 통해 swapping이 간단해짐
(x,y)=(y,x) # 이렇게만 해주면 x랑 y가 swapping됨

#데이터구조 -3.dictionary
dictionary1={}#dict() #선언
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'} #Key에는 변하지 않는 값을 사용하고, Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다
dic[name] #pey 이렇게 key를 통해 원하는 정보만 알 수 있음
dic[address]='kr'#이렇게 넣고 싶은 key와 value를 선언해주기만 하면 dic에 추가되는 거임
del dic[adress] #삭제는 del로 함
dic[name]='Shin' #수정하고 싶은 value가 있으면 이렇게 대입해서 수정하면 됨
#딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 ""않고""" Key를 통해 Value를 얻는다. 
#baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는 것이 아니라 baseball이라는 단어가 있는 곳""만"" 펼쳐 보는 것이다.
#관련함수
dic.keys()#딕셔너리의 키들만 리스트 형태로 반환함
dic.values()#value들만 리스트 형태로 반환함
dic.items()# 각각의 key와 value를 튜플로 묶은 것을 요소들로 하는 리스트로 반환함
dic.clear()#딕셔너리 안의 모든 요소들을 삭제함, 빈 것이 되게 함
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a.get('name')#'pey' #키로 value 얻기
a.get('phone')#'0119993323' #key로 value 얻기
a.get('foo', 'bar') # get(x, '디폴트 값')으로 해두면 키인 x가 없으면 디폴트값을 반환해줌
# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
'name' in a #True
'email' in a #False

#데이터구조 - 4. set ,얘도 { }임
s1 = set([1,2,3]) #선언, 괄호 안에 리스트를 넣어서 선언
print(s1) #{1, 2, 3}
s2 = set("Hello") #리스트 말고 그냥 문자열만 넣어도 됨
print(s2) #{'e', 'H', 'l', 'o'}
#중복을 허용하지 않는다.
#순서가 없다(Unordered).
#만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한후 해야 한다.
s= set() #빈 집합 선언

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2 #교집합 #{4, 5, 6}
s1.intersection(s2)#이렇게 표현도 가능{4, 5, 6}


s1 | s2 #합집합 #{1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.union(s2) #합집합은 이렇게도 가능

s1 - s2 #차집합 #{1, 2, 3}
s2 - s1 #차집합 {8, 9, 7}
s1.difference(s2)#차집합의 다른 표현 #{1, 2, 3}
s2.difference(s1) #{8, 9, 7}

s1 = set([1, 2, 3])
s1.add(4) #집합s1에 하나의 요소만 추가
s1 #{1, 2, 3, 4}

s1 = set([1, 2, 3])
s1.update([4, 5, 6]) #집합 s1에 여러 개의 요소를 추가할 땐 update씀
s1 #{1, 2, 3, 4, 5, 6}

s1 = set([1, 2, 3])
s1.remove(2) # 집합에서 특정값만 제거
s1#{1, 3}



#조건문
age=input("당신의 나이는?") # 묻는게 문자열로 물었으니까 age에 저장되는 대답도 문자열이 됨
answer=int(age) #따라서 원하는 형태로 형변환
if (answer<20):
    print("당신은 미성년자입니다")
else:
    print("당신은 성인입니다")


pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass  #가끔 조건문의 참, 거짓에 따라 실행할 행동을 정의할 때, 아무런 일도 하지 않도록 설정하고 싶을 때가 있다.
else:
    print("카드를 꺼내라")


pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시를 타고가라")
elif card: 
     print("택시를 타고가라") # else if를 파이썬에선은 elif으로 활용 #즉 elif는 이전 조건문이 거짓일 때 수행된다
else:
     print("걸어가라")

# 수행할 문장이 한 줄일 때 c++ 처럼 그냥 한 줄로 콜론 뒤에 써줘도 됨. 예) else: print("걸어가라")


#반복문
#for
sum=0
for i in range(1,11): # 1부터 10까지임
    sum+=i
print(sum)

list=[1,2,3]
for item in list:
    print(item)

#while
temp=100
while temp>0:
    temp/=10;
    print(temp)


#함수
def sum(a,b):
    c=a+b
    return c

print(sum(1,2))


#파이썬 - 클래스 만들기
class Quad:
    #attribute(멤버 변수) 선언
    height=0
    width=0
    color=''
    name=''

    #method(멤버 함수) 선언
    def get_area(self): # 함수에 별도의 파라미터가 필요 없어도! self는 반드시 넣어줘야 한다. self는 선언 시에만 신경쓰면 됨
        return self.height*self.width
    
    def quard_name(self): #객체의 name 반환
        return self.name #name은 멤버변수이므로 self.을 붙여줘야 함

    #함수의 파라미터가 존재하는 경우에도 self는 반드시 써줘야 한다.
    def quad_attribute(self,arg1,arg2):
        return arg1+agr2; # arg1,arg2는 그냥 단순 변수(파라미터)일 뿐 별도로 멤버 변수나 그런게 아니므로 self.arg1 이렇게 표현할 필요 없음

#객체의 생성
quad1=Quad()

#객체의 기능(속성,메서드)호출
quad1.height=30 # 속성을 직접 지정 가능
quad1.name="hello"
quad1.quard_name()#self는 호출시에 고려하지 않음
quad1.quad_attribute(1,2); #self는 호출시에 고려하지 않음


#라이브러리
#예: 수학함수들을 모아놓은 라이브러리가 있음- math 라이브러리
#사용법1
import math
num=math.pow(3,3) #라이브러리에서의 특정 기능(메서드)를 호출
print(num)
num=math.factorial(5) #math 라이브러리의 팩토리얼 기능


#사용법2
from math import sqrt,factorial #라이브러리 모두를 import하지 않고, "내가 원하는 특정 메서드만" import함
num1=sqrt(6) #바로 함수 호출만 하면 됨
num2=factorial(3)

#사용법 2-2(사용법1+사용법2) - 딱히 권장 안 함
from math import * #math 라이브러리에서 모든 함수들을 import
num=sqrt(3)+sqrt(3) # from~을 해줬으므로 math.으로 호출할 필요 없음

#사용법 3 -라이브러리에 있는 함수명이 길거나해서 다른 이름으로 쓰고 싶을 때
import math as d
num=d.factorial(2)

#사용법 3-1
from math import factorial as f
num=f(3) # factorial(3)이랑 같은 거임
