# 如何读取excel中数据，使用xlrd模块

import xlrd
data = xlrd.open_workbook(r"./very_excel.xlsx")
print(data)

table = data.sheets()[0]
print(table)

value = table.row_values(1)
value1 = table.col_values(0)
print(value1)

nrows = table.nrows
ncols = table.ncols
print(nrows)

for i in range(nrows):
    for j in range(ncols):
        cellValues = table.cell(i,j).value
        print(cellValues)


