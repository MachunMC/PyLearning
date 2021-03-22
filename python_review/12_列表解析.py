# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 12_列表解析.py
# @Author  : Machun Michael
# @Time    : 2021/3/22 19:07
# @Software: PyCharm

# 创建一个只包含1到10的平方的列表
num_list = [value * value for value in range(1,11)]
print(num_list)