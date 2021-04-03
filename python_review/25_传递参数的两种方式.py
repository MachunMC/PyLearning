# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 25_传递参数的两种方式.py
# @Author  : Machun Michael
# @Time    : 2021/3/30 21:44
# @Software: PyCharm

# 函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参
# 函数传参的方式有多种，包含位置实参和关键字实参


# 1.位置实参：按照形参顺序传递实参
# 需要注意传参的顺序
def describe_pet(animal_type, name):
    print("I have a " + animal_type + ", and his name is " + name.title())

# describe_pet('cat', 'tom')
# describe_pet('mouse', 'jerry')


# 2.关键字实参：函数调用时，传递的是 "参数名--参数值"
# 这样无须考虑传参的顺序，因为传递的参数中，已经指定了参数对应的值
describe_pet(animal_type='cat', name='tom')
describe_pet(name='tom', animal_type='cat')