# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 08_列表排序.py
# @Author  : Machun Michael
# @Time    : 2021/3/14 16:29
# @Software: PyCharm

# 列表的排序
# 注意：下面假定所有字母都是小写形式。
# 当大小写混合时，列表排列顺序稍微复杂一些。在决定排列顺序时，有多种方式解读大写字母
companys = ['byte dance', 'tencent', 'alibaba', 'jing dong', 'meituan', 'ping duo duo']
print("原始列表：", companys)

# 1.使用sort()方法，进行永久性排序：按照字母顺序进行排序
# 如果想按照字母顺序进行反向排序，可以加上reverse=True
companys.sort()
print("sort排序后的列表：", companys)

companys.sort(reverse=False)
print("sort(reverse=False) 排序后的列表：", companys)

companys.sort(reverse=True)
print("sort(reverse=True) 排序后的列表：", companys)


# 2.使用sorted函数，对列表进行临时性排序，不改变列表元素的顺序
# 也可以加上reverse=True进行反向排序
weekdays = ['monday', 'tuesday', 'wednesday', 'thusday', 'friday']
print("原始列表：", weekdays)
print("sort()函数临时排序后的列表：", sorted(weekdays))
print("原始列表：", weekdays)
print("sort(reverse=True)排序后的列表：", sorted(weekdays, reverse=True))


# 3.使用reverse()方法，反转列表元素的排列顺序
# 反转两次，就得到原来顺序的列表
fruits = ['Apple', 'orange', 'pear', 'lemon']
print("原始列表：", fruits)

fruits.reverse()
print("reverse()反转后的列表：", fruits)

fruits.reverse()
print("reverse()再次反转后的列表：", fruits)