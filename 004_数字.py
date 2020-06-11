# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 004_数字.py
# @Author  : Machun Michael
# @Time    : 2020/5/17 18:00
# @Software: PyCharm

'''
0. python中使用"+"、"-"、"*"、"/"来进行数字的运算，**表示几次方

1. 浮点数：python中进行浮点数运算时，运算结果中的小数点位数可能是不确定的
   如：0.2 + 0.1，运算结果为0.30000000000000004
'''


# 1. 整数
sum = 1 + 1
print(sum)
print(2 + 2)
print(1024 - 128)
print(10 * 11)
print(120/5)
print(8 ** 2)    # 表示8的平方
print(8 ** 3)    # 表示8的3次方

# 2. 浮点数
print(0.2 + 0.03)
print(0.2 + 0.1)
print(0.1 * 0.3)
print(.1 + .2)   # 省略小数点前面的0也是可以的