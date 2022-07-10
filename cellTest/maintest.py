
import unittest
from HTMLTestRunner import HTMLTestRunner

discover = unittest.defaultTestLoader.discover(r"./cellTest/",pattern = "unitMymath.py")

# 使用runner运行器运行测试集
with open(r"./cellTest/res.html","wb") as f:
    # runner = unittest.TextTestRunner(f,verbosity=2)
    # runner.run(discover)

    runner = HTMLTestRunner(f, verbosity = 2,title = "单元测试报告",description = "第一次运行结果")
    runner.run(discover)
