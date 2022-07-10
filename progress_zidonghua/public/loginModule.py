from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
class very_login():
    def login(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.get("http://kkk.xmyxwl.com/")

        # 点击页面登录按钮
        self.driver.find_element(By.LINK_TEXT, "登陆").click()
        # 输入用户名
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("zhangsan")
        # 输入密码
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("1234567")
        # 点击登录按钮
        self.driver.find_element(By.XPATH, '//*[@id="login-form"]/div/a').click()

        time.sleep(5)

    # 退出浏览器
    def quitB(self, driver):
        self.driver = driver
        self.driver.quit()

        # 退出登录

    def logout(self, driver):
        self.driver = driver
        ele = self.driver.find_element(By.XPATH, '//*[@id="top-userbar"]/a')
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element(By.LINK_TEXT, "退出").click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    aa = very_login()
    aa.login(driver)
    aa.logout(driver)
    aa.quitB(driver)
