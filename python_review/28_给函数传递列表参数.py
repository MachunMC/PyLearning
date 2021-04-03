# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 28_给函数传递列表参数.py
# @Author  : Machun Michael
# @Time    : 2021/4/3 14:46
# @Software: PyCharm

# 可以给函数传递列表参数
def greet_users(names):
    for name in names:
        print("Hello, " + name.title() + '!')

# 传递列表参数
users = ['michael', 'jack', 'lily', 'tom']
greet_users(users)

# 传入一个字符串，函数的执行不会报错，只是执行结果和预期的有点不同
name = 'zhangsan'
greet_users(name)

# 传入一个整数，函数执行报错
# 由于函数的形参没有类型的限制，调用者如何确定需要传递什么类型的参数？？必须要阅读函数体吗？
# 以这个函数为例，只知道需要传入姓名，但函数内部是按照列表来处理的
# 是不是需要编写相应的函数声明，说明函数的功能、参数类型等
# name = 123
# greet_users(name)