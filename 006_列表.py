# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 006_列表.py
# @Author  : Machun Michael
# @Time    : 2020/5/18 19:41
# @Software: PyCharm


'''
1. 列表：列表是一个有序集合，由一系列按照特定顺序排列的元素组成，类似于C语言中的数组
   列表的元素可以是数字、字符、字符串等等
   用"[]"来表示列表，用","来分隔列表元素

2. 访问列表元素
   类似于访问数组元素，可以使用 “列表名+索引” 的方式访问列表元素。
   同样，索引是从0开始；特别之处是，python中的索引可以用复数，例如-1表示列表的最后一个元素，-2表示列表的倒数第2个元素
   注意，索引不能超过列表长度

3. 修改列表中元素的值
   给列表元素赋一个新的值，就可以修改元素的值

4. 在列表中增加元素
'''

names  = ["michae", "Tom", "Lucy", "Lily", "Sheldon"]
ages   = [25, 24, 23, 25, 22]
scores = ['A', 'B', 'A', 'A', 'C']
print(names)
print(ages)
print(scores)

# 访问列表元素
message = names[0] + "is " + str(ages[0]) + " years old, and he got an " + scores[0]
print(message)
print(names[-1])
# print(names[-8])  # 索引值超过列表长度

# 修改列表中元素的值
names[1] = "Tony"
print(names)

# 在列表中增加元素