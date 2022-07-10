'''
    需求：使用先行脚本的模型，编写电商系统反向用例的脚本
            打开verydows系统首页
            点击”免费注册“按钮
            输入有效用户名
            输入有效邮箱
            输入有效密码
            输入有效确认密码
            已阅读按钮
            点击”同意协议，立即注册“
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 定义字典数据，用来存储注册数据（用户名、密码、确认密码、email）
# 字典中存数据，字典放列表
# 若数据不合理，用例的执行结果是错的
dictData = [{"username":"","email":"zhangsan@163.com","password":"1234567","repassword":"1234567","expect":"请设置用户名"},
            {"username":"lisi","email":"lisi@163.com","password":"1234567","repassword":"1234567","expect":"用户名不符合格式要求"},
            {"username":"lisi_0237539463472","email":"lisi@163.com","password":"1234567","repassword":"1234567","expect":"用户名不符合格式要求"}]

for i in dictData:
    # print(i["userame"])

    driver = webdriver.Chrome()
    driver.get("http://kkk.xmyxwl.com/")

    driver.find_element(By.LINK_TEXT,"免费注册").click()
    driver.find_element(By.ID,"username").send_keys(i["username"])
    driver.find_element(By.ID,"email").send_keys(i["email"])
    driver.find_element(By.ID,"password").send_keys(i["password"])
    driver.find_element(By.ID,"repassword").send_keys(i["repassword"])
    driver.find_element(By.LINK_TEXT,"立即注册").click()

    # 因为由中间页面的跳转，需强制等待
    # 若脚本执行逻辑不合理，用例执行结果报错
    time.sleep(3)

    # 断言 通过获取当前页面的url地址，与预期的url地址进行对比，判断是否成功注册
    # exceptUrl = "http://kkk.xmyxwl.com/index.php?c=user&a=index"
    # actualUrl = driver.current_url
    expectValue = i["expect"]
    actualValue = driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font').text

    if expectValue == actualValue:
        print("注册username反向用例通过，注册成功")
    else:
        print("注册username反向用例不通过，注册失败")

    # 关闭浏览器对象
    driver.quit()







