'''
    常见的自动化测试模型（掌握）
        线性模型：最基本的代码组织形式，就纯粹是模拟用户步骤或场景。维护性较差

        需求：使用先行脚本的模型，编写电商系统正向用例的脚本
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
from selenium.webdriver.common.by import By
import time

# 创建浏览器对象
driver = webdriver.Chrome()

# 打开verydows系统首页
driver.get("http://kkk.xmyxwl.com/")
# 获取电商系统首页的URL地址，用于第一个步骤的断言
# urL1 = driver.current_url
# if urL1 == "http://kkk.xmyxwl.com/":
#     print("首页打开正确")
# else:
#     print("首页打开失败")

# 点击”免费注册“按钮
driver.find_element(By.LINK_TEXT,"免费注册").click()
# urL2 = driver.current_url
# if urL2 == "http://kkk.xmyxwl.com/index.php?c=user&a=register":
#     print("注册页面打开成功")
# else:
#     print("注册页面打开失败")

# 输入有效用户名
driver.find_element(By.ID,"username").send_keys("cc12_abcdABCDefg")
# 输入有效邮箱
driver.find_element(By.ID,"email").send_keys("ccc@163.com")
# 输入有效密码
driver.find_element(By.ID,"password").send_keys("123456777566534112176546764")
# 输入有效确认密码
driver.find_element(By.ID,"repassword").send_keys("123456777566534112176546764")
# 已阅读按钮
# 点击”立即注册“
driver.find_element(By.LINK_TEXT,"立即注册").click()

# 需要添加强制延时，跳过中间的提示页面
time.sleep(5)

# 断言 通过获取当前页面的url地址，与预期的url地址进行对比，判断是否成功注册
exceptUrl = "http://kkk.xmyxwl.com/index.php?c=user&a=index"
actualUrl = driver.current_url
if exceptUrl == actualUrl:
    print("注册的正向用例通过，注册成功")
else:
    print("注册的正向用例不通过，注册失败")

# 完成线性操作，关闭浏览器
driver.quit()







