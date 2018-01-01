# -*- coding=utf-8 -*-
def count():
    """
    返回闭包不能引用循环变量，请改写count()函数，让它正确返回能计算1x1、2x2、3x3的函数。
    :return:
    """
    fs = []
    for i in range(1, 4):
        def f(j):
            """
            把i传给内部函数f,而不是直接塞给他, 内部函数f一定要接受enclosing参数
            :param j:
            :return:
            """

            def g():
                return j * j

            return g

        # 把i传给内部函数f,而不是直接塞给他, 内部函数一定要接受参数,
        r = f(i)  # i给啦line 9的j
        fs.append(r)
    return fs


def count2():
    """
    问题的产生是因为函数只在执行时才去获取外层参数i，若函数定义时可以获取到i，问题便可解决。
    而默认参数正好可以完成定义时获取i值且运行函数时无需参数输入的功能，所以在函数f()定义中改为f(m = i),函数f返回值改为m*m即可.
    :return:
    """
    fs = []
    for i in range(1, 4):
        def f(m=i):
            return m * m

        fs.append(f)
    return fs


def count3():
    """
    只要将这里改为fs.append(f())即可，这样就在这一步的时候已经进行了i*i的运算，将结果保存了
    :return:
    """
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f())
    return fs


f1, f2, f3 = count()
f4, f5, f6 = count2()
print f1(), f2(), f3()
print f4(), f5(), f6()

for i in count3():
    print i
