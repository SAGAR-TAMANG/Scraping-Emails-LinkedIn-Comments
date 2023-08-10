import time
import datetime

import pandas as pd
import numpy as np

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from bs4 import BeautifulSoup

df = pd.DataFrame(columns=['LinkedIn Name', 'Email'])
chrome_user_profile = r"C:\Users\TAMANG\AppData\Local\Google\Chrome\User Data"

options = ChromeOptions()
options.add_argument("user-data-dir=" + chrome_user_profile)
options.add_argument("profile-directory=Profile 1")
# options.add_argument("--no-extension")
# options.add_argument("--no-sandbox");
# options.add_argument("--disable-dev-shm-usage");

service = Service(executable_path=r'C:\path\to\chromedriver.exe')

driver = Chrome(service=service, options=options)

url = "https://www.linkedin.com/posts/devanbhalla_resume-internship-college-activity-6645944070516629504-sawD?utm_source=share&utm_medium=member_android"

driver.get(url)

time.sleep(0.2) 

driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div/div/div[5]/div[3]/div[2]/div/button/span[2]').click()

# driver.find_element(By.XPATH, '//*[@id="ember88"]').click()

time.sleep(1)
# element = driver.find_element_by_class_name("")

driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div/div/div[5]/div[3]/div[2]/div/div/div[1]/ul/div[2]/li[1]/div').click()

load_time = 1

num_of_pages = np.arange(1,1000)

count = 0
count2 = 0

for page in num_of_pages:
  try:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div/div/div[5]/div[3]/div[3]/div[2]/button/span').click()
    # driver.execute_script("window.scrollTo(0,(document.body.scrollHeight))")
    time.sleep(load_time)
  except Exception as e:
    count = count + 1
    print(count)
    pass

df = pd.DataFrame(columns=['LinkedIn Name', 'Email'])

soup = BeautifulSoup(driver.page_source, 'html5lib')
# print(soup.encode('utf-8'))

result = soup.find('div', id='ember90')

# print('result:', result.encode('utf-8'))

final_result = result.find_all('article', class_='comments-comment-item')

# print('final result:', final_result)

for i in final_result:
  try:
    # print(i.encode('utf-8'))
    name = i.find('span', class_='comments-post-meta__name-text').text.strip()
    # print(name.strip())

    message_box = i.find('div', class_='update-components-text relative')
    # print(message_box.encode('utf-8'))

    email = message_box.find('a').text
    # print(email.strip())

    # df = df.append({'LinkedIn Name': name, 'Email': email}, ignore_index=True)
    df = pd.concat([df, pd.DataFrame([[name, email]], columns = ['LinkedIn Name', 'Email'])], ignore_index=True)
  except Exception as e:
    count2 = count2 + 1
    print('Exception Occured', count2)

time.sleep(5)

print('TOTAL EXCEPTIONS: ', count2)

print(df)
df.to_excel('output.xlsx', index=False)