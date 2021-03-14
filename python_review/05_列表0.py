# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 05_列表0.py
# @Author  : Machun Michael
# @Time    : 2021/3/14 14:23
# @Software: PyCharm

# 列表类似数组
# 是由一系列按特定顺序排列的元素组成
# 列表由 "[]"括起来，并用逗号分隔

students = ["Tom", "Lucy", "Lily", "Jack"]
print(students)

# 可以使用列表索引来访问列表元素，列表索引从0开始
print("The first student is " + students[0])
print("The second student is " + students[1])

# 可以使用-1来访问列表最后一个元素，-2表示倒数第二个元素，-3表示倒数第三个元素等
print("The last student is " + students[-1])