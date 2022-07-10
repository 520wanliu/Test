'''
    csv文件数据读取：
        1、新建一个excel文件，写入测试数据（是根据测试用例中分离处理的数据部分，有几个，都是什么）
        2、将文件另存为utf带逗号分隔符的csv文件
        3、将csv文件转码为utf-8格式
        4、在python代码中导入数据
            导包
            使用with + open 打开文件
            使用data = csv.reader(f)
            使用for循环遍历数据
        5、文件路径问题(以下为相对路径，不建议使用绝对路径)
            获取当前编辑文件的目录 ：os.path.dirname(__file__)
                                os.path.dirname(os.path.dirname(__file__)) ：表示当前文件的上级目录
'''
import csv
import os

# path1 = os.path.dirname(__file__)
# print(path1)

filename = os.path.dirname(__file__) + r"/data_csv.csv"
print(filename)

filename = os.path.dirname(os.path.dirname(__file__)) + r"/自动化测试用例设计/data_csv.csv"

# with open(r"E:/work/Test/jiaobenkaifa/data_csv.csv", "r", encoding="utf-8") as f:
with open(filename, "r", encoding="utf-8") as f:
    data = csv.reader(f)
    print(data)
