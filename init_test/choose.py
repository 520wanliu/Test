from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
'''
# radio选择框
# 读取当前选中的元素
element = wd.find_element_by_css_selector('#s_radio input[checked = checked]')
print('当前选中的是：' + element.get_attribute('value'))

# 点选“小雷老师”
element = wd.find_element_by_css_selector('#s_radio input[value = "小雷老师"]').click()'''

'''
# checked复选框
# 先将已经选中的选项点击一下，确保都是未选中状态，再点击小雷老师
elements = wd.find_elements_by_css_selector('#s_checkbox input[checked=checked]')

for element in elements:
    element.click()

wd.find_element_by_css_selector('#s_checkbox input[value = "小雷老师"]').click()'''


# select框
'''
# select单选框
# 1)导入select类的包
from selenium.webdriver.support.ui import Select
# 2)创建select对象（根据select框的id属性）
select = Select(wd.find_element_by_id("ss_single"))
# 3)通过select对象选中小雷老师
select.select_by_visible_text("小雷老师")'''

# select多选框
# 1) 导入select类
from selenium.webdriver.support.ui import Select
# 2）创建select对象
select = Select(wd.find_element_by_id("ss_multi"))
# 3) 清除所有已经选中的选项
select.deselect_all()
# 4) 选择待选项
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小凯老师")
