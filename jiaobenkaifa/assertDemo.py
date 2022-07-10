'''
    断言：
        就是判断预期和实际结果是否一致
        现在可以使用if语句判断
        在后面学assert Equal()。。。。。。等方法实现断言

        在使用断言的时候，注意异常的处理，如果不处理，可能会导致pvm退出，后续的脚本或者代码不能执行
        只有只用try——except——finally这种语法处理，保证后续代码或脚本的正常运行

'''

import selenium
from selenium import webdriver
import time
import csv
import os
from selenium.webdriver.common.by import By

filename = os.path.dirname(__file__) + r"/data_csv.csv"

with open(filename, "r", encoding="utf-8") as f:
    data = csv.reader(f)
    for d in data:
        driver = webdriver.Chrome()
        driver.get("http://kkk.xmyxwl.com/")

        driver.find_element(By.LINK_TEXT,"免费注册").click()
        driver.find_element(By.ID,"username").send_keys("test0001")
        driver.find_element(By.ID,"email").send_keys("test0001@163.com")
        driver.find_element(By.ID,"password").send_keys("1234567")
        driver.find_element(By.ID,"repassword").send_keys("1234567")
        driver.find_element(By.LINK_TEXT,"立即注册").click()

        time.sleep(5)

        '''
            使用 try...except 捕获异常
        '''
        # 断言
        expectValue = "test0001"
        try:
            actualValue = driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[1]/div[1]/h3/font[1]")

            if expectValue == actualValue:
                print("注册username正向测试用例通过")
            else:
                print("注册username正向测试用例不通过")
        except selenium.common.exceptions.NoSuchElementException as e:
            print("抛出异常，未定位到元素：",e)
        finally:
            # 关闭浏览器
            driver.quit()








