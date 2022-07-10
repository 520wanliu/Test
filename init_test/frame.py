from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')

# 此时已经切换到iframe内部，若要选择外部元素，需要切换至iframe外部
# 切换操作范围 到 被嵌入的文档中，在内层的frame中选择元素
# wd.switch_to.frame('frame1')

# 若当前frame没有id或者name 可自行选择区别对象
wd.switch_to.frame(wd.find_element_by_css_selector('[src="sample1.html"]'))

elements = wd.find_elements_by_css_selector('.plant')

for element in elements:
    print('--------------------')
    print(element.get_attribute('outerHTML'))

# 由于之前是在iframe内部进行操作，此时需要切换到外部去选择外部元素
wd.switch_to.default_content()
wd.find_element_by_id('outerbutton').click()

# wd.quit()