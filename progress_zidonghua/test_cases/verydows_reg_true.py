import csv
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

filename = os.path.dirname(os.path.dirname(__file__)) + r"/test_datas/data_csv.csv"
print(filename)
class verydows_reg_true(unittest.TestCase):
    def setUp(self):
        pass

    def test_reg_01(self):
        with open(filename, "r", encoding="utf-8") as f:
            data = csv.reader(f)
            for d in data:
                driver = webdriver.Chrome()
                driver.get("http://kkk.xmyxwl.com/")
                driver.find_element(By.LINK_TEXT,"免费注册").click()
                driver.find_element(By.ID,"username").send_keys(d[0])
                driver.find_element(By.ID,"email").send_keys(d[1])
                driver.find_element(By.ID,"password").send_keys(d[2])
                driver.find_element(By.ID,"repassword").send_keys(d[3])
                driver.find_element(By.LINK_TEXT,"立即注册").click()

                # 等待
                time.sleep(10)

                # 断言
                # expectValue = d[4]
                # actualValue = driver.find_element(By.XPATH,'//*[@id="register-form"]/div/d1[1]/dd/span/font').text

                # self.assertEqual(actualValue, expectValue)

                # 关闭浏览器
                driver.quit()
    def tearDown(self) :
        pass

if __name__ == '__main__':
    unittest.main()







