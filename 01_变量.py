# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 01_变量.py
# @Author  : Machun Michael
# @Time    : 2020/5/16 18:26
# @Software: PyCharm

'''
0. 变量命名规则
    (0) 变量名只能用数字、字母和下划线，并且只能以字母和下划线开头
    (1) 不能使用python关键字作为变量名
    (2) 变量名应该简洁易懂

1. 使用方法
    (0) python中，定义变量不需要指定数据类型，变量的数据类型，是根据所赋的值决定的
    (1) 变量可以用整数、浮点数、字符和字符串来赋值
    (2) 同一个变量，可以分别赋为不同类型的值
'''

message = "welcome to python world"
print(message)

null = ""
print(null)

name = "michael"
age = 25
print("hello, my name's %s, and I'm %d years old" %(name, age))

var = 10
print("var is ", var)

var = 3.141592653
print("var is ", var)

var = "int"
print("var is ", var)