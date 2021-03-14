# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 04_number.py
# @Author  : Machun Michael
# @Time    : 2021/3/14 13:49
# @Software: PyCharm

# 整数
# 加（+）、减（-）、乘（*）、除（/）、乘方（**）

tmp = 1 + 2
print("1 + 2 = " + str(tmp))  # str()将数字转换成字符串

tmp = 2 + 100093200998
print("2 + 100093200998 = " + str(tmp))

tmp = 1 - 999
print("1 - 999 = " + str(tmp))

tmp = 999 * 8888888888888888888888
print("999 * 8888888888888888888888 = " + str(tmp))

tmp = 8899 / 2233
print("8899 / 2233 = " + str(tmp))

# 乘方
tmp = 2 ** 3
print("2 ** 3 = " + str(tmp))


# 浮点数（小数）
# 有一点需要注意的是：浮点数计算的结果，后面的小数位数是不确定的，有可能和预期的结果位数不同
# 这是由于计算机内部表示数字的方式导致的，后续学习处理多余位数的方法
tmp = 0.1 + 0.1
print("0.1 + 0.1 = " + str(tmp))

print("0.1 + 0.2 = " + str(0.1 + 0.2))