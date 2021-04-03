# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 27_函数返回值.py
# @Author  : Machun Michael
# @Time    : 2021/4/3 14:25
# @Software: PyCharm


# 使用return将值返回到函数调用行
def sum(a, b):
    return (a+b)

# print("sum(1, 3):", sum(1, 3))
# print("sum(299, 10983):", sum(299, 10983))


def get_full_name(first_name, last_name):
    return ('My name is ' + first_name.title() + " " + last_name.title())

name0 = get_full_name('zhang', 'san')
print(name0)

name1 = get_full_name('li', 'si')
print(name1)