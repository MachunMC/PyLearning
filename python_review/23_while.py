# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 23_while.py
# @Author  : Machun Michael
# @Time    : 2021/3/30 21:10
# @Software: PyCharm

import time

# 3s倒计时
# sec = 3
# while sec > 0:
#     print(sec)
#     sec -= 1
#     time.sleep(1)
#
# print("time over")

# while + break
# 输出
# num0 = 100
# while True:
#     if num0 == 10:
#         break
#     else:
#         num0 -= 1
# print(num0)

num1 = 100
while True:
    if num1 != 10:
        num1 -= 1
        #time.sleep(1)
        continue
    else:
        num1 -= 1
        break