# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 14_复制列表.py
# @Author  : Machun Michael
# @Time    : 2021/3/23 7:41
# @Software: PyCharm

my_foods = ['pizza', 'cake', 'cola', 'ice creen']

# 要想复制列表，最简单的方法是使用切片
friend_foods = my_foods[:]
print('my      foods:', my_foods)
print('friend  foods:', friend_foods)

# 验证my_foods和friend_foods是两个不同的列表
my_foods.append('hot pot')
friend_foods.append('BBQ')
print('my     new foods:', my_foods)
print('friend new foods:', friend_foods)


# 直接用等号，不是复制列表。
# 用等号，类似于C++的引用，两个变量关联的是同一个列表
my_languages = ['C', 'C++', 'Python']
friend_languages = my_languages
print('my     languages:', my_languages)
print('friend languages:', friend_languages)

my_languages.append('Go')
print('my     new languages:', my_languages)
print('friend new languages:', friend_languages)

friend_languages.append('Java')
print('my     new languages:', my_languages)
print('friend new languages:', friend_languages)