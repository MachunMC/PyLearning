# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 007_列表排序.py
# @Author  : Machun Michael
# @Time    : 2020/5/20 20:20
# @Software: PyCharm

'''
说明：下面所有示例，列表元素首字母均为大写或小写。元素首字母大小写都有的情况会比较复杂，会在后面进行说明

1. sort()：将列表元素按首字母顺序排列，这会修改原列表元素的位置

2. sort(reverse=TRUE)：将列表元素按首字母相反的顺序进行排列

3. sorted()函数：和sort()方法效果类似，都是将列表元素按首字母顺序排列，但是sorted不会修改原列表元素的位置，只是用于显示

4. sorted(reverse=TRUE)：按照列表元素首字母相反的顺序排列，同样不会修改原列表元素的位置
'''


names = ["Ada", "Cindy", "Brace", "franke", "Dale", "Elen", "Grace", "Hellen", "Jerry"]
print(names)

# 按首字母顺序排列
names.sort()
print(names)

# 按首字母相反的顺序排列
names.sort(reverse=True)
print(names)

# sorted()函数
fruits = ["banana", "grape", "apple", "orange", "lemon", "mango", "olive", "peach"]
print(fruits)
print(sorted(fruits))
print(fruits)
print(sorted(fruits, reverse=True))