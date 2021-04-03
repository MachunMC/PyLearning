# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 26_参数默认值.py
# @Author  : Machun Michael
# @Time    : 2021/4/3 14:01
# @Software: PyCharm

# 定义函数时，可以给形参指定默认值
# 这样，当函数调用时传递了实参，就使用实参的值；如果没有传递实参，就使用默认值
# 注意：使用默认值的形参，一定要放到最右边
def describe_pets(name, animal_type='dog'):
    print("I have a " + animal_type + ", and his name is " + name.title())

describe_pets('jack')
describe_pets('tom', 'cat')
describe_pets(animal_type='mouse', name='Jack')