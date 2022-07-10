import os
import sys
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from progress_zidonghua.public.loginModule import very_login

# path = os.path.dirname(os.path.dirname(__file__)) + r"/public"
# path1 = sys.path
# path1.append(path)


class verydows_user_update(unittest.TestCase):
    def setUp(self):
        self.ll = very_login()
        self.driver = webdriver.Chrome()
        self.ll.login(self.driver)

    def test(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="usermenu"]/li[2]/a').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="nickname"]').clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="nickname"]').send_keys("petter")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="profile-form"]/div/button').click()
        time.sleep(3)
        actualValue = self.driver.find_element(By.XPATH,'//*[@id="nickname"]').get_attribute("value")
        expectValue = "petter"
        self.assertEqual(actualValue,expectValue)


    def tearDown(self):
        self.ll.logout(self.driver)
        self.ll.quitB(self.driver)

if __name__ == '__main__':
    unittest.main()
