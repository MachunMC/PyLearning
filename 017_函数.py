# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 017_函数.py
# @Author  : Machun Michael
# @Time    : 2020/6/16 19:31
# @Software: PyCharm

'''
1. 定义一个函数
    (1) 格式：def func_name(param0, param1...):
                function body

'''

def display_message(name, book):
    print(name + "'s favorite book is " + book)

display_message("Michael", "平凡的世界")
display_message("Ton", "人生海海")