from selenium import webdriver

webdriver = webdriver.Chrome()

webdriver.get('https://www.baidu.com')

webdriver.find_element(By.ID,'kw').send_keys('jmeter')

webdriver.find_element_by_id('su').click()

pass

