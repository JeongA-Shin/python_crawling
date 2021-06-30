#json : JavaScript Object Notation의 줄임말
#웹 환경에서 서버와 클라이언트 사이에 데이터를 주고 받을 때 많이 사용(REST API가 주요 예제)
#{key:value,key:value ... } value에 데이터 자료형은 상관 없음, 리스트가 들어가도 됨

# jason 자료형 파싱하는 방법
import json
'''
data='''
{
    "id":"01","language":"Java","edition":"third","author":"Herbert Schildt",
    "history":
    [{
        "date":"2015-03-11",
        "item":"iPhone"
    },
    {
        "date":"2016-03-11",
        "item":"ANDROID"
    }]
}
'''

json_data=json.loads(data) #json.loads(json자료)를 하면 파싱이 된 결괏값이 변수(json_data)에 담아진다
# .loads()를 통해 파싱이 된 후에는 딕셔너리처럼 쓰면 됨 - key값으로 value를 찾음
print(json_data) #{'id': '01', 'language': 'Java', 'edition': 'third', 'author': 'Herbert Schildt', 'history': [{'date': '2015-03-11', 'item': 'iPhone'}, {'date': '2016-03-11', 'item': 'ANDROID'}]}
print(json_data["id"]) # 01
print(json_data["language"]) #Java
print(json_data["history"]) #[{'date': '2015-03-11', 'item': 'iPhone'}, {'date': '2016-03-11', 'item': 'ANDROID'}]
print(json_data["history"][1]) #리스트 안의 리스트  #{'date': '2016-03-11', 'item': 'ANDROID'}
print(json_data["history"][0]) # {'date': '2015-03-11', 'item': 'iPhone'}
print(json_data["history"][0]["date"]) #리스트 안의 리스트 안에 있는 딕셔너리 요소  #2015-03-11

'''

#실전 활용 
# 네이버 검색에서, 뉴스 파트에서 android라는 키워드로(query=android) 요청하고 받은 결과
data='''
{
    "lastBuildDate": "Thu, 01 Jul 2021 01:50:07 +0900",
    "total": 24842,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "Turn Your Phone Into a Fitness Coach",
            "originallink": "https://www.nytimes.com/2021/06/30/technology/personaltech/turn-your-phone-into-a-fitness-coach.html?partner=naver",
            "link": "https://www.nytimes.com/2021/06/30/technology/personaltech/turn-your-phone-into-a-fitness-coach.html?partner=naver",
            "description": "The Google Fit app works on the <b>Android</b> and iOS operating systems. (It can also import health... Most of the popular programs are available for both <b>Android</b> and iOS. These include the Jefit... ",
            "pubDate": "Wed, 30 Jun 2021 22:00:00 +0900"
        },
        {
            "title": "자동 점프 플랫포머 '바운싱 히어로' 스위치판 7월 1일 출시",
            "originallink": "http://www.epnc.co.kr/news/articleView.html?idxno=211364",
            "link": "http://www.epnc.co.kr/news/articleView.html?idxno=211364",
            "description": "시험해볼 수 있는 액션 게임 '바운싱 히어로'의 스위치 버전은 오는 7월 1일, 닌텐도 e샵을 통해 만나볼 수 있을 예정이다. 닌텐도 스위치 이외에도 iOS, <b>Android</b>, Steam 플랫폼을 통해 바운싱 히어로를 플레이할 수 있다.",
            "pubDate": "Wed, 30 Jun 2021 18:20:00 +0900"
        },
        {
            "title": "I Write About the Law. But Could I Really Help Free a Prisoner?",
            "originallink": "https://www.nytimes.com/2021/06/30/magazine/yutico-briley.html?partner=naver",
            "link": "https://www.nytimes.com/2021/06/30/magazine/yutico-briley.html?partner=naver",
            "description": "To hear more audio stories from publications like The New York Times, download Audm for iPhone or <b>Android</b>. It all started with an email I received from a retired librarian in Oregon. “Dear Ms.... ",
            "pubDate": "Wed, 30 Jun 2021 18:03:00 +0900"
        },
        {
            "title": "포르쉐 AG, 최고출력 650마력 고성능 SUV 모델 ''카이엔 터보 GT'' 공개",
            "originallink": "http://kr.aving.net/news/view.php?articleId=1611340&Branch_ID=kr&rssid=naver&mn_name=news",
            "link": "http://kr.aving.net/news/view.php?articleId=1611340&Branch_ID=kr&rssid=naver&mn_name=news",
            "description": "PCM 6.0은 이전과 마찬가지로 애플 카플레이(Apple CarPlay) 지원은 물론, 애플 뮤직과 애플 팟캐스트를 유기적으로 완벽하게 통합시켰다. 포르쉐 인포테인먼트 시스템은 안드로이드 오토(<b>Android</b> Auto)를 포함한다.",
            "pubDate": "Wed, 30 Jun 2021 17:34:00 +0900"
        },
        {
            "title": "Samsung Challenges Apple with 'One UI Watch'",
            "originallink": "http://www.businesskorea.co.kr/news/articleView.html?idxno=70701",
            "link": "http://www.businesskorea.co.kr/news/articleView.html?idxno=70701",
            "description": "and <b>Android</b> smartphones, and access to an even greater number of applications. Samsung further... management, <b>Android</b> and wear, Google. &quot;That certainly holds true for this new, unified platform... ",
            "pubDate": "Wed, 30 Jun 2021 15:56:00 +0900"
        },
        {
            "title": "발키리 커넥트, 애니메이션 '블리치' 콜라보 이벤트 개최",
            "originallink": "http://www.inven.co.kr/webzine/news/?news=258357",
            "link": "https://sports.news.naver.com/news.nhn?oid=442&aid=0000136370",
            "description": "자료제공- 에이팀 주식회사 에이팀(대표이사: 하야시 타카오)은 iOS/<b>Android</b>/Amazon/Steam에서 제공하는 하이 판타지 RPG [발키리 커넥트]에서 6월 30일(수)부터 TV 애니메이션 [블리치]와의 콜라보레이션 이벤트를 진행한다고... ",
            "pubDate": "Wed, 30 Jun 2021 15:48:00 +0900"
        },
        {
            "title": "[타보니]지프 랭글러 사하라 파워탑 80주년 에디션, 역시 매력적인 ‘아메리칸...",
            "originallink": "http://www.nspna.com/news/?mode=view&newsid=511686",
            "link": "http://www.nspna.com/news/?mode=view&newsid=511686",
            "description": "또 최신 Uconnect 내비게이션은 8.4인치 터치스크린을 탑재해 적시적소에 필요한 정보를 보여주며 내비게이션부터 차량 제어, Apple CarPlay 서포트 뿐만 아니라 <b>Android</b> Auto 까지 지원해 주행 시 주의를 분산시키지 않고... ",
            "pubDate": "Wed, 30 Jun 2021 15:10:00 +0900"
        },
        {
            "title": "증권통, 2021 하반기 개발·기획 인재 채용",
            "originallink": "http://www.newstomato.com/ReadNews.aspx?no=1055681&inflow=N",
            "link": "http://www.newstomato.com/ReadNews.aspx?no=1055681&inflow=N",
            "description": "채용직군은 △<b>Android</b> 개발 △iOS 개발 △Server 개발 △서비스 기획 총 4개 직군이다. 채용 절차는 서류전형, 면접전형, 최종합격순이며 전형별 일정은 7월까지 진행될 예정이며 적합한 인재를 채용시 마감된다.... ",
            "pubDate": "Wed, 30 Jun 2021 14:54:00 +0900"
        },
        {
            "title": "포르쉐, 고성능 SUV 카이엔 터보 GT 올해 말 국내 출시.. 가격 2억 3410만원",
            "originallink": "http://kbench.com/?q=node/222811",
            "link": "http://kbench.com/?q=node/222811",
            "description": "PCM 6.0은 이전과 마찬가지로 애플 카플레이(Apple CarPlay) 지원은 물론, 애플 뮤직과 애플 팟캐스트를 유기적으로 완벽하게 통합시켰으며  포르쉐 인포테인먼트 시스템은 안드로이드 오토(<b>Android</b> Auto)를 포함한다.... ",
            "pubDate": "Wed, 30 Jun 2021 11:24:00 +0900"
        },
        {
            "title": "Black Desert Mobile by Pearl Abyss breaks into Chinese market",
            "originallink": "http://pulsenews.co.kr/view.php?year=2021&no=631104",
            "link": "https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=004&oid=009&aid=0004816788",
            "description": "Even after obtaining approval in late last year, Summoners War by Com2uS is banned from <b>Android</b>-based local app stores and is only being serviced on Apple’s app store. The release date of... ",
            "pubDate": "Wed, 30 Jun 2021 11:22:00 +0900"
        }
    ]
}
'''

json_data=json.loads(data)
#print(json_data["items"])
print(json_data["items"][0]["title"])

print("\n")
for item in json_data["items"]:
    print(item["title"],"\n")