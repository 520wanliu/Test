'''
    将上文的线性脚本转化为模块化的脚本：
        脚本中重复的代码抽离出来形成一个模块（模块中的方法）
        1、如果单独验证的是登录、退出、xxx功能，则需要加上断言
        2、如果对其进行模块化（写成了方法或者类），就不需要再加上断言

    1.登录电商系统
    2.退出电商系统
'''

# 需要设计一个方法：实现可以提供注册的基本步骤，并通过参数传入数据
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class very_login:
    def __init__(self):
        # 实现浏览器对象的创建
        self.driver = webdriver.Chrome()
        # 隐形等待
        self.driver.get("http://kkk.xmyxwl.com/")
    def login(self):  # 实现登录功能
        # 点击页面登录按钮
        self.driver.find_element(By.LINK_TEXT,"登陆").click()
        # 输入用户名
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("zhangsan")
        # 输入密码
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("1234567")
        # 点击登录按钮
        self.driver.find_element(By.XPATH,'//*[@id="login-form"]/div/a').click()

        time.sleep(5)

    # 退出浏览器
    def quitB(self):
        self.driver.quit()

    # 退出登录
    def logout(self):
        ele = self.driver.find_element(By.XPATH,'//*[@id="top-userbar"]/a')
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element(By.LINK_TEXT,"退出").click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    aa = very_login()
    aa.login()
    aa.logout()
    aa.quitB()








