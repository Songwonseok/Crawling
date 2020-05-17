from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요:')

url = baseUrl + quote_plus(plusUrl) # 한글을 ascii 코드로 변환

html = urlopen(url).read()
soup = BeautifulSoup(html,'html.parser') # 'html 분석
img = soup.find_all(class_='_img')

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open(plusUrl + str(n) + '.jpg','wb') as h : # 사과n.jpg 로 저장
            # w: 쓰기 , b : 이미지 -> 바이너리파일
            img = f.read() # imgUrl을 읽어옴
            h.write(img) # h로 저장
    n += 1

print('다운로드 완료')

