'''
    使用unitttest框架设计mymath的单元测试用例（通过这个案例讲解unittest的特性）
    步骤：
        1、导包：unittest是python的自带框架，不需要安装
        2、创建一个单元测试类（一个python类，只是继承了单元测试框架单元测试用例的类）
        3、先讲单元测试类中五个特殊方法的使用，包括使用场景和执行顺序
            setUp() 、 test_xxx() 、 tearDown()三个方法的执行顺序与书写位置无关

            setUp()：主要是进行测试用例的资源初始化，测试用例的前提条件写在该方法中
            test_xxx()：测试用例，要把测试用例的步骤写在该方法中
            tearDown()：主要是进行测试用例资源释放的
            @classmethod()注解的方法是类方法，不用创建对象也能用的方法，在对象进内存之前就已经存在的方法
                        随着类一起进内存
            setUpClass()：给当前单元测试类的所有测试用例进行初始化
            tearDownClass()：给当前单元测试类的所有测试用例进行资源释放

            setUpClass()方法 与 setUp()方法的区别：
                1) setUp()方法不需要@classmethod注解；setUpClass()方法需要@classmethod注解
                2) setUp()方法是实例方法，需要创建对象在调用；setUpClass()方法是类方法，不需要对象也可以调用
                3) setUp()方法在每一个测试用例执行之前运行一次，多个测试用例时执行多次；setUpClass()方法在所有的测试执行之前只执行一次
                4) setUp()方法只对一条测试用例初始化；setUpClass()方法给当前单元测试类的所有用例进行初始化

        4、创建测试用例：test开头的方法
        5、测试用例执行：
            main()方法：
                将所有的测试用例都执行一遍
                执行测试用例的顺序控制不了（按照测试用例名（方法名）的字母顺序执行）
            如何解决上面这个不太好的特点：使用测试集合的概念（testsuite）
            分类：将加法的测试用例加到一个测试集合testsuite中，只运行该测试集合即可
            testsuite：
                1、创建testsuite的对象
                2、调用testsuite中的方法addTest、addTests方法将测试用例加入测试集合
                3、testsuite方法的run方法运行测试集合

                注意：run方法的参数是testresult的对象：re = unittest.TestResult()
                     TestResult中存储的是测试执行的结果
                print(re.__dict__)
            TestLoader:
                1、创建Testloader对象：loader = unittest.TestLoader()
                2、使用loader的方法loadtestsfromName()将指定的测试用例加载到测试集合，并返回一个测试集合对象
                    loadtestsfromName()的参数比较灵活：
                        1、可以是模块名：unitMymath
                        2、可以是模块中的类名：unitMymath.unitMymath
                        3、可以是模块中类中的某一个用例：unitMymath.unitMymath.test_add_2
                3、使用TestLoader的discover方法（必须掌握），将指定的文件（模块）中的测试用例一次性加载
                    discover()方法：suitt = unittest.defaultTestLoader.discover(r"./cellTest/",pattern="unit*.py")
                    path：指定存放测试用例的目录即可（单元测试用例，使用unittest框架写的测试用例）
                    pattern：指定匹配规则，very_reg_*.py
                                        very_login_*.py
                4、TestRunner()：
                    在前面测试用例、测试集合执行的时候都是用testsuite()的run()方法：suitt.run(result)
                    textTestRunner()--->将结果能够以text文本形式展示的运行器


'''

import os
import unittest
from cellTest.myMath import mymath

# 创建一个单元测试类
class unitMymath(unittest.TestCase):

    # 一种注解，在python、Java中使用这种方式给方法指定特定含义
    @classmethod
    def setUpClass(self) :
        print("我是setUpClass方法")
        # 3个用例，其中第一个需要A条件，第二个需要B条件，第三个需要C条件，三个都需要D条件
        # 其中第一个需要A条件，第二个需要B条件，第三个需要C条件：可以直接放在test开头的方法中
        # D条件因为是都需要的参数，可以放在setUp()中，也可以放在setUpClass()方法中

    @classmethod
    def tearDownClass(cls) :
        print("我是tearDownClass方法")

    # 方法名不能改，self参数不能少
    def setUp(self):
        print("我是setUp()方法")
        self.mm = mymath()

    # 必须以test开头的方法，表示一个测试用例
    def test_add_1(self):
        print("我是test_add_1()方法")
        # mm = mymath()
        # actualValue = mm.jia(10,12)
        # actualValue = cls.mm.jia(10,12)
        actualValue = self.mm.jia(10,12)
        expectualValue = 22
        # 该方法的作用是判断给定两个参数是否相等
        # Assertion failed  22 != 23 : 预期结果与实际结果不相等
        self.assertEqual(expectualValue,actualValue,"预期结果与实际结果不相等")


    def test_add_2(self):
        print("我是test_add_2()方法")
        # mm = mymath()
        actualValue = self.mm.jia("abc","123")
        expectualValue = "abc123"
        self.assertEqual(expectualValue,actualValue,"预期结果与实际结果不相等")

    def test_muilt_3(self):
        print("我是test_muilt_3()方法")
        # mm = mymath()
        actualValue = self.mm.cheng(22,2)
        expectualValue = 44
        self.assertEqual(expectualValue,actualValue,"预期结果与实际结果不相等")

    # 方法名不能改，self参数不能少
    def tearDown(self) :
        print("我是tearDown()方法")
        # 用这句话注销对象，释放资源
        # self.mm = None

if __name__ == '__main__':
    # 创建测试集合
    suitt = unittest.TestSuite()
    # 使用TestLoader中的discover()方法返回测试集合
    suitt = unittest.defaultTestLoader.discover(r"./cellTest/",pattern="unit*.py")

    # 调用测试集合的run()方法运行测试用例
    # suitt.run(unittest.TestResult())  # 该方法没法查看运行了哪些用例
    # 创建一个TestResult()的对象
    # result = unittest.TestResult()
    # suitt.run(result)
    # 查看运行结果
    # print(result.__dict__)

    # 使用TextTestRunner()运行器提供的run()方法运行测试集合
    # 如何产生一个文件流对象，如果打开一个文本文件，想着往里面写入数据
    with open(r"./cellTest/re.txt","w",encoding="utf-8") as f:
        runner = unittest.TextTestRunner(f)
        runner.run(suitt)
