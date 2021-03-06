# 在此文件中调度测试用例进行执行

import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import time

pathCase = os.path.dirname(__file__) + r"/test_cases/"
pathReport = os.path.dirname(__file__) + r"/test_reports/"

filename = time.strftime("%Y-%m-%d-%H-%M-%S") + r".html"
filename = pathReport + filename
discover = unittest.defaultTestLoader.discover(pathCase,pattern = "verydows*.py")

with open(filename, "wb") as f:
    runner = HTMLTestRunner(f, verbosity = 2, title = "自动化测试用例执行", description = "xx")
    runner.run(discover)