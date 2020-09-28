# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : MathModule.py
# @Author  : Machun Michael
# @Time    : 2020/6/21 17:21
# @Software: PyCharm

# 求和
def func_sum(*nums):
    sum = 0
    for num in nums:
        sum += num

    return sum

# 求积
def func_product(*nums):
    product = 1
    for num in nums:
        product *= num

    return product

# 求平方和
def func_quadratic_sum(*nums):
    sum = 0
    for num in nums:
        sum += num ** 2

    return sum

print("hello world")