# 定义一个类，实现加减乘除
class mymath():
    def jia(self,a,b):
        return a + b

    def jian(self,a,b):
        return a - b

    def cheng(self,a,b):
        return a * b

    def chu(self,a,b):
        return a / b

if __name__ == '__main__':
    mm = mymath()
    # 实现第一条用例，验证数字的加法
    acttualValue = mm.jia(2,3)
    exceptValue = 5
    if acttualValue == exceptValue:
        print("加法功能正确实现")

    # 第二条测试用例，验证数字和字符串的加法
    # 执行结果：该方法实现正确  can only concatenate str (not "int") to str（后面试抛出的异常）
    try:
        acttualValue = mm.jia("a", 3)
    except Exception as e:
        print("该方法实现正确",e)

    # 需求：设计的方法除了数字的运算外，还能进行字符串的比较
    # 第三条测试用例，验证字符串的加法
    try:
        acttualValue = mm.jia("a","b")
        exceptValue = "ab"
        if acttualValue == exceptValue:
            print("字符串加法实现正确")
    except Exception as e:
        print(e)