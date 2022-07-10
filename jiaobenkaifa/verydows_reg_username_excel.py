'''
    如果想在python文件中处理excel文件，是需要专门模块（额外安装）
    xlrd模块的使用：
        1、安装xlrd模块：pip install xlrd
        2、导包  import xlrd
        3、使用xlrd模块的方法打开excel文件
        4、读取其中一个sheet页数据
        5、读取当前sheet页某一行/列数据，索引从0开始 : row_values(0) / col_values(0)
        6、获取行数或列数，辅助做遍历循环用： nrows / ncols
        7、使用for循环遍历每一个单元格数据
            for i in range(总行数):
                print(table.row_values(i)[0])  # 取出表格中第 i 行的第一列数据
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xlrd

# 使用xlrd模块的方法打开excel文件
data = xlrd.open_workbook(r"./自动化测试用例设计/data_excel.xlsx")
# <xlrd.book.Book object at 0x000001E179C18888>
# print(data)

# 读取其中一个sheet页数据
datatable = data.sheets()[0]
# <xlrd.sheet.Sheet object at 0x000002DAD5864308>
# print(datatable)

# 读取某一行数据
rowvalue = datatable.row_values(0)
# ['', 'nz123_0000@163.com', 123456.0, 123456.0, '请设置用户名']
# print(rowvalue)

# 获取文件的行数和列数
rowN = datatable.nrows
# print(rowN)
colN = datatable.ncols
# print(colN)

# 获取所有数据
for i in range(rowN):
    print(datatable.row_values(i)[0])

    driver = webdriver.Chrome()
    driver.get("http://kkk.xmyxwl.com/")

    driver.find_element(By.LINK_TEXT,"免费注册").click()
    driver.find_element(By.ID,"username").send_keys(datatable.row_values(i)[0])
    driver.find_element(By.ID,"email").send_keys(datatable.row_values(i)[1])
    driver.find_element(By.ID,"password").send_keys(datatable.row_values(i)[2])
    driver.find_element(By.ID,"repassword").send_keys(datatable.row_values(i)[3])
    driver.find_element(By.LINK_TEXT,"立即注册").click()

    # 因为有一个中间页面的跳转，此处要强制等待一下，方便其页面跳转
    # 脚本逻辑不合理时，测试执行的结果是错的
    time.sleep(2)

    # 断言
    # expectUrl = "http://kkk.xmyxwl.com/index.php?c=user&a=index"
    # actualUrl = driver.current_url

    expectValue = datatable.row_values(i)[4]
    actualValue = driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font')

    # 判断的条件是：提示信息是否符合要求
    if expectValue == actualValue:
        print("注册username反向测试用例通过")
    else:
        print("注册username反向测试用例不通过")

    # 关闭浏览器对象
    driver.quit()

