'''
    先安装xlrd模块
    从excel文件中读入数据
        1、导包：import xlrd
        2、使用xlrd的方法打开excel文件（创建一个文件对象）
        3、获取excel文件的sheet页
        4、获取sheet页的行数、列数以及行数据、列数据、单元格数据
        5、通过sheet页的行数和列数遍历当前页数据
        6、使用for循环
'''

import xlrd
import os

# 使用xlrd的方法打开excel文件（创建一个文件对象）
filename = os.path.dirname(__file__) + r"/data_excel.xlsx"
data = xlrd.open_workbook(filename)

# 获取excel文件的sheet页
# 方式一：先获取所有的sheet，然后按照索引拿其中第几个sheet页，索引号是从0开始的
table1 = data.sheets()[0]
table2 = data.sheets()[1]
print(table1)
print(table2)

# 方式二：按照sheet的名字来获取
table = data.sheet_by_name("test")
print(table)

# 读取行数和列数
rows = table.nrows
cols = table.ncols
print(rows)
print(cols)

# 获取行数据、列数据、单元格数据
rowValue = table.row_values(0)
colValue = table.col_values(0)
print(rowValue)
print(colValue)

cellValue = table.cell_value(0,1)
print(cellValue)

# 遍历当前页数据
# 方式一：先获取列数据，然后拿其中一个值
for i in range(rows):
    print(table.row_values(i))  # 所有行数据
    print(table.col_values(i))  # 所有列数据
# 方式二：遍历单元格
for i in range(rows):
    for j in range(cols):
        print(table.cell_value(i,j))



