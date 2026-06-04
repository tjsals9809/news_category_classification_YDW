# 파일명은 naver_news_section.csv로 해주세요.
# 컬럼명은 titles, category로 해주세요.
# 00님이 정치, 경제
# 01님이 사회, 문화
# 02님이 IT, 세계
# 다 되면 PR부탁합니다
# 클릭 30번

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

import pandas as pd
import datetime

options = ChromeOptions()
options.add_argument('lang=ko_KR')
# 주석달면 홈페이지가 출력됌
options.add_argument('headless')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 크롬에서 'Developer Tools'에 들어가 Ctrl+Shift+C를 누르고
# 기사 더보기 영역을 누르고 복사하면 링크를 얻을 수 있음
button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]/a'

# 세계 뉴스 페이지 주소
df_titles = pd.DataFrame()
url = 'https://news.naver.com/section/104'
driver.get(url)

for i in range(30):
    driver.find_element(By.XPATH, button_xpath).click()
    time.sleep(0.5)

print('')
print('세계 뉴스 헤드 라인')
print('')

for i in range(1, 180):
    print('------------------------------------')
    for j in range(1, 7):
        try:
            title_xpath = '//*[@id="newsct"]/div[4]/div/div[1]/div[{}]/ul/li[{}]/div/div/div[2]/a/strong'.format(i, j)
            title = driver.find_element(By.XPATH, title_xpath).text
            titles = []
            titles.append(title)
            print(title)
            df_section_titles = pd.DataFrame(titles, columns=['titles'])
            df_section_titles['category'] = 'World'
            df_titles = pd.concat([df_titles, df_section_titles], ignore_index=True)
        except:
            print('error', i, j)

df_titles.info()
# 수집한 뉴드 헤드라인들을 CSV파일로 저장
df_titles.to_csv('./data/naver_news_section_World.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)

# 세계 뉴스 페이지 주소
df_titles = pd.DataFrame()
url = 'https://news.naver.com/section/105'
driver.get(url)

for i in range(30):
    driver.find_element(By.XPATH, button_xpath).click()
    time.sleep(0.5)

print('')
print('IT 뉴스 헤드 라인')
print('')

for i in range(1, 180):
    print('------------------------------------')
    for j in range(1, 7):
        try:
            title_xpath = '//*[@id="newsct"]/div[4]/div/div[1]/div[{}]/ul/li[{}]/div/div/div[2]/a/strong'.format(i, j)
            title = driver.find_element(By.XPATH, title_xpath).text
            titles = []
            titles.append(title)
            print(title)
            df_section_titles = pd.DataFrame(titles, columns=['titles'])
            df_section_titles['category'] = 'IT'
            df_titles = pd.concat([df_titles, df_section_titles], ignore_index=True)
        except:
            print('error', i, j)

df_titles.info()
# 수집한 뉴드 헤드라인들을 CSV파일로 저장
df_titles.to_csv('./data/naver_news_section_IT.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)