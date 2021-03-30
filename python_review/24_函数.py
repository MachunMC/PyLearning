# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 24_函数.py
# @Author  : Machun Michael
# @Time    : 2021/3/30 21:32
# @Software: PyCharm

# 1.定义函数
# 格式：def func_name(param_list):
#            func_body
def print_hello():
    print("hello world")

# 2.调用函数：函数名(形参)
print_hello()

# 3.函数传参
def say_hello(name):
    print("hello", name)

say_hello("michael")
say_hello("Jack")