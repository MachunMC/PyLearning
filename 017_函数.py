# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 017_函数.py
# @Author  : Machun Michael
# @Time    : 2020/6/16 19:31
# @Software: PyCharm

'''
0. 函数定义
    (0) 格式：def func_name(param0, param1...):
                function body
1. 参数默认值
    (0) 在定义函数时，可以指定参数默认值。在调用函数时，如果传递了实参，则使用实参值；如果没有传递实参，则使用默认值。
    (1) 这样可以简化函数调用
    (2) 指定默认值的形参，一定要放在靠右边的位置。如果给中间位置的参数指定默认值，在传递实参时，容易产生歧义

2. 调用函数时，如果指定了形参名，可以不用考虑参数传递的顺序。但是不推荐这种方法，最好按顺序传递参数，这样比较清晰易懂，而且更加简洁
'''

def display_message(name, book):
    print(name + "'s favorite book is " + book)

display_message("Michael", "平凡的世界")
display_message("Ton", "人生海海")
display_message(name="Jarry", book="围城")       # 传递参数时，可以指定对应的形参名
display_message(book="张居正", name="Jack")      # 如果传递参数时指定了对应的形参名，可以无需考虑参数顺序

# def introduction(name, age, addr="Shanghai, China", sport):
def introduction(name, age, addr="Shanghai, China"):
    print("Hello everyone, my name's " + name + ", I'm " + str(age) + " years old, and I lives in " + addr)

# introduction("Tom", 21, "basketbal")          # 如果指定中间位置的参数使用默认值，这样不知道"basketbal"传递给addr，还是sport
introduction("Tom", 21)
introduction("Michael", "24", "Anhui, China")   # 如果24用引号括起来，则认为传递的是字符串类型
