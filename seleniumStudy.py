from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl='https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome("C:/ssafy/Webdriver/chromedriver.exe")
driver.get(url)

# html = driver.page_source
# soup = BeautifulSoup(html)
#
# r = soup.select('.r') # list 형식
# print(type(r))
# for i in r :


