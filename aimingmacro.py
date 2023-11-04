from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import re
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename, askopenfilenames
from tkinter import messagebox

# window=tk.Tk()

# window.title("MingTicketer")
# window.geometry("640x400+100+100")
# window.resizable(False, False)

# window.mainloop()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver_time = webdriver.Chrome()
driver_time.get('https://time.navyism.com/?host=aimingmarket.com')
driver_time.find_element_by_id('msec_check').click()

driver.set_window_size(1400, 1000)  # (가로, 세로)
driver.get('https://www.aimingmarket.com/PRODUCT/?idx=500') # 페이지 이동(URL)

driver.find_element_by_name('uid').send_keys('') # ID
driver.find_element_by_name('passwd').send_keys('') # Password

def aimingmacro(): # 로그인 및 이후 동작
    driver.find_element_by_class_name('btn.btn-primary.btn-block').click() # 로그인

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="prod_options"]/div/div/div[2]/a'))
        )
    finally:
        pass
    
    try:
        driver.find_element_by_xpath('//*[@id="prod_options"]/div/div/div[2]/a').click() # 드롭다운메뉴 클릭
        driver.find_element_by_xpath('//*[@id="prod_options"]/div/div/div[2]/div/div[3]/a').click() # 원하는메뉴 클릭 / 마지막 숫자는 메뉴번호 index: 1, 2, 3,...
        #driver.find_element_by_xpath('//*[@id="prdOption0"]/div/div[2]/div[1]/div/input').send_keys(Keys.BACK_SPACE) # 박스주문시 주석처리
        #driver.find_element_by_xpath('//*[@id="prdOption0"]/div/div[2]/div[1]/div/input').send_keys(3) # 수량, 박스주문시 주석처리, default=1

        #driver.find_element_by_xpath('//*[@id="prod_options"]/div/div/div[2]/div/div[2]/a').click() # 원하는메뉴 클릭 / 마지막 숫자는 메뉴번호
        #driver.find_element_by_xpath('//*[@id="prdOption0"]/div/div[2]/div[1]/div/input').send_keys(Keys.BACK_SPACE) # 박스주문시 주석처리
        #driver.find_element_by_xpath('//*[@id="prdOption0"]/div/div[2]/div[1]/div/input').send_keys(1) # 수량, 박스주문시 주석처리, default=1

        driver.find_element_by_xpath('//*[@id="prod_goods_form"]/div[8]/a[1]').click() # 구매하기
        time.sleep(1000)
    finally:
        time.sleep(1000)

while True:
    a = driver_time.find_element_by_id('time_area').text
    b = driver_time.find_element_by_id('msec_area').text

    time_chk = re.findall("[0-9]+", a)
    if (time_chk[4]=='30' and time_chk[5]=='00'): # time[4] : 분, time[5] : 초
        msec = re.findall("[0-9]+", b)
        if (int(msec[0]) >= 0):
            aimingmacro()
            time.sleep(1000)