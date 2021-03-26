# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 19_遍历字典.py
# @Author  : Machun Michael
# @Time    : 2021/3/26 21:03
# @Software: PyCharm

favorite_language = {
    'michael' : 'C',
    'Jack' : 'C++',
    'Tom' : 'python',
    'Lucy' : 'java',
    'jerry' : 'go',
}

# 1. 遍历字典所有的键值对
# items()方法，返回一对键值对
# 定义两个变量name和language，分别存储返回的键和值
# 注意：遍历字典时，返回的键值对顺序，可能和存储顺序不同！！！python不关心存储的键值对的顺序
for name, language in favorite_language.items():
    print(name + "'s favorite language is " + language)

# 2. 遍历字典所有的键
# keys()方法，返回字典中所有键的一个列表
print(favorite_language.keys())
for name in favorite_language.keys():
    print(name)

# 3. 按顺序遍历字典所有的键
# python获取键值对的顺序是不可预测的， 可使用sorted()函数来进行排序
for name in sorted(favorite_language.keys()):
    print(name)

# 4.遍历字典中所有的值
# values()方法，返回字典中所有值的一个列表
print(favorite_language.values())
for language in favorite_language.values():
    print(language)