# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 06_修改列表元素.py
# @Author  : Machun Michael
# @Time    : 2021/3/14 15:19
# @Software: PyCharm

# 1. 修改列表元素的值
language = ["C", "C++", "Python", "Go", "Java"]
print("初始列表：", language)

language[4] = "Per"
print("修改第5个元素后的列表：", language)

# 2. 在列表中添加新元素
# 2.1 在列表末尾添加新元素
language.append('Shell script')
print("在列表末尾新增一个元素：", language)

users = []  # 定义一个空列表，列表名称是users，元素个数是0
print("定义一个空列表：", users)

users.append("Tom")
users.append("Jack")
users.append("admin")
print("空列表新增3个元素：", users)

# 2.2 在列表任意位置插入元素，后面的元素往后偏移一个位置
users.insert(1, "Michael")
print("在列表第一个元素的位置，插入一个新元素：", users)