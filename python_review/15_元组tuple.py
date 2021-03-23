# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 15_元组tuple.py
# @Author  : Machun Michael
# @Time    : 2021/3/23 7:56
# @Software: PyCharm

# 列表在创建后，可以动态的修改；元组在创建后，不可以修改
# 可以把元组看作是不可修改的列表

# 1.定义元组（tuple），使用圆括号，可以通过索引访问元组的元素
rectangle = (100, 50)
print("长方形的长宽分别是:", rectangle[0], rectangle[1])

# 修改元组元素
# rectangle[1] = 80，直接报错


# 2.使用for循环，遍历元组
salaries = ('6.5k', '7k', '10k', '11.8k', '12.6k')
for salary in salaries:
    print(salary)

# 3.虽然不允许修改单个元组元素，但是可以修改整个元组变量，相当于重新给该变量赋值
# salaries[0] = '20k'
salaries = ('25k', '28k', '32k')
print(salaries)