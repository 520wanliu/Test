'''
    csv文件的创建：
        1、创建一个excel文件，录入数据
        2、将excel文件另存为utf格式的带逗号分隔符的csv文件
        3、使用notepad++超级记事本文件将csv文件转码为utf-8格式

    如何读取csv文件中的数据：
        with open(r"./自动化测试用例/data_csv.csv","r",encoding = "utf-8") as f:
            data = csv.reader(f)
'''

import csv
with open(r"./自动化测试用例设计/data_csv.csv","r",encoding="utf-8") as f:
    data = csv.reader(f)
    # <_csv.reader object at 0x000001B5A068A6D8> 可以遍历读取
    print(data)

    # 从data中获取每行数据，其实是一个列表
    for d in data:
        print(d[2])




