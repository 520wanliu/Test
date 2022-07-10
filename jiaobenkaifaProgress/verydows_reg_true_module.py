'''
    需求：正向的测试用例

    步骤：打开verydows系统首页
         点击”免费注册“按钮
         输入有效用户名
         输入有效邮箱
         输入有效密码
         输入有效确认密码
         已阅读按钮
         点击”同意协议，立马注册“
'''

import csv
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# 写成模块化的形式
def very_reg_true(filename):
    file = os.path.dirname(__file__) + r"/" + filename
    with open(file, "r", encoding="utf-8") as f:
        data = csv.reader(f)
        for d in data:
            # 打开系统首页
            driver = webdriver.Chrome()
            driver.get("http://kkk.xmyxwl.com/")

            # 点击"免费注册"按钮
            driver.find_element(By.LINK_TEXT,"免费注册").click()
            # 输入有效用户名
            # driver.find_element(By.ID,"username").send_keys("aaaaaaa")
            username = d[0] + str(random.randint(0,999))    # 用于生成一个随机位数的name
            driver.find_element(By.ID,"username").send_keys(username)

            # 输入有效邮箱
            # driver.find_element(By.ID,"email").send_keys("aaaaaaa@163.com")
            email = username + r"@163.com"
            driver.find_element(By.ID,"email").send_keys(email)

            # 输入有效密码
            driver.find_element(By.ID,"password").send_keys(d[2])
            # driver.find_element(By.ID,"password").send_keys("1234567")
            # 输入有效确认密码
            driver.find_element(By.ID,"repassword").send_keys(d[3])
            # driver.find_element(By.ID,"repassword").send_keys("1234567")
            # 点击已阅读按钮
            # 点击“立即注册
            driver.find_element(By.LINK_TEXT,"立即注册").click()

            # 等待
            time.sleep(10)

            # 断言
            exceptUrl = "http://kkk.xmyxwl.com/index.php?c=user&a=index"
            actualUrl = driver.current_url

            if exceptUrl == actualUrl:
                print("正向测试用例注册通过，登录成功")
            else:
                print("正向测试用例注册不通过，登录失败")

            # 关闭浏览器
            # driver.quit()

if __name__ == '__main__':
    very_reg_true("data_csv.csv")






