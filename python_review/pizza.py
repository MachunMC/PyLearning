# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : pizza.py
# @Author  : Machun Michael
# @Time    : 2021/4/5 15:41
# @Software: PyCharm

# 模块化
def make_pizza(*toppings):
    print("makeing pizza with followed toppings:")
    for topping in toppings:
        print('- ' + topping)

def make_salad(*toppings):
    print("makeing salad with followed toppings:")
    for topping in toppings:
        print('- ' + topping)

def make_noodles(*toppings):
    print("makeing noodles with followed toppings:")
    for topping in toppings:
        print('- ' + topping)