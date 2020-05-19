from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:/ssafy/Webdriver/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('http://www.python.org')

# title에 Python이라는 단어가 있으면 밑에 실행
assert "Python" in driver.title

elem = driver.find_element_by_name("q")
# 키 이벤트 전송
elem.send_keys(("python"))

# 엔터 입력
elem.send_keys((Keys.RETURN))
# elem.clear()

# 결과물이 안나오면 중지
assert "No results found." not in driver.page_source

# 명시적으로 일정시간을 기다릴 수 있음(2초)
time.sleep(2)

h3s = driver.find_elements_by_tag_name("h3")
for h3 in h3s:
    print(h3.text)

driver.quit() #브라우저 닫음





