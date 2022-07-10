# 导包
from selenium import webdriver
# 创建浏览器对象
driver = webdriver.Chrome()
# 打开百度首页
driver.get("https://www.baidu.com")
# 在百度首页的文本框中输入selenium
driver.find_element_by_id("kw").send_keys("selenium")
# 点击百度按钮
driver.find_element_by_id("su").click()
# 关闭浏览器
driver.quit()