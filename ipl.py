from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
import time

print('Watch unlimited free 10 min matches on hotstar')
print('******some extra features*******')
print('1. Browser will automatically close and restart with new timer')
print('2. Close browser anytime. It will start a new browser with new timer \n\n\n')
print('Enter the hotstar live match link')
# txt = 'https://www.hotstar.com/sports/cricket/vivo-ipl-2019/chennai-super-kings-vs-royal-challengers-bangalore-m189952/live-streaming/2001710503?utm_source=onebox&utm_campaign=IPL19&utm_content=live'
txt = input('waiting for the link ........\n')
txt = txt.replace('www.','http://')
print('Opening browser with given link')

def get_chrome():
    driver = webdriver.Chrome()
    driver.get(txt)
    for i in range(540):
        time.sleep(1)
        driver.execute_script('window;')
    driver.execute_script('window.localStorage.clear();')
    driver.execute_script('window.sessionStorage.clear();')
    driver.delete_all_cookies()
    driver.close()

while 1:
    try:
        get_chrome()
    except Exception:
        continue




