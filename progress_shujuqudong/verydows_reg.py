'''
    数据驱动测试（DDT）：
        1、所谓数据驱动测试，简单的理解为数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变
        2、通过使用数据驱动测试的方法，可以在需要验证多组数据测试场景中，使用外部数据源实现对输入、输出
          与期望值的参数化，避免在测试中使用硬编码的数据
        3、这种方法对于测试步骤相同而使用不同的输入值和期望值的测试场景尤为重要
        4、数据驱动的模式不仅可以帮助增加类似复杂条件场景下的测试覆盖，还可以极大的减少对测试代码的编写和维护工作
'''

import time
import unittest
from ddt import ddt,data
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1、创建字典数据
# 2、导入ddt模块，帮助实现数据驱动   from ddt import ddt,data
# 3、用ddt修饰，注解unittest类
# 4、使用data修饰测试用例  @data(*dataValue)
# 5、重写生命测试用例名称   test_reg_01(self,para)
# 6、使用para["username"]

@ddt
class verydows_reg(unittest.TestCase):
    # 案例1：使用字典数据结构存储数据，实现数据驱动
    dataValue = [{"username":"test11111","email":"test11111@163.com","password":"1234567","repassword":"1234567","expect":"用户名不符合格式要求"},
            {"username":"","email":"test11111@163.com","password":"1234567","repassword":"1234567","expect":"请设置用户名"}]
    def setUp(self):
        pass

    @data(*dataValue)
    def test_reg_01(self,para):
        driver = webdriver.Chrome()
        # 1、打开verydows电商网站首页
        driver.get("http://kkk.xmyxwl.com/")
        # 2、点击首页的免费注册按钮，跳转到注册页面
        driver.find_element(By.LINK_TEXT,"免费注册").click()
        # 3、输入合法用户名
        driver.find_element(By.ID,"username").send_keys(para["username"])
        # 4、输入有效邮箱
        driver.find_element(By.ID,"email").send_keys(para["email"])
        # 5、输入有效密码
        driver.find_element(By.ID,"password").send_keys(para["password"])
        # 6、输入有效的确认密码
        driver.find_element(By.ID,"repassword").send_keys(para["repassword"])
        # 7、点击我已同意按钮（默认已勾选）
        # 8、点击注册按钮，注册成功
        driver.find_element(By.LINK_TEXT,"立即注册").click()

        # 等待时间
        time.sleep(5)

        # 断言
        # actualValue = driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font').text
        # expectValue = para["expect"]
        # self.assertEqual(actualValue,expectValue)

        driver.quit()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()







