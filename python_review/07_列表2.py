# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 07_列表2.py
# @Author  : Machun Michael
# @Time    : 2021/3/14 16:20
# @Software: PyCharm


# # 从列表中删除元素
# # 1.根据索引，使用del语句删除元素（del不是方法）
# jobs = ['teacher', 'actor', 'doctor', 'engineer']
# print(jobs)
#
# del jobs[0]
# print(jobs)
#
# del jobs[2]
# print(jobs)
#
#
# # 2.根据索引，使用pop()方法删除元素
# # pop可以理解为，从列表中取出某个元素，取出的元素可以保存到另一个变量中
# colors = ['red', 'green', 'yellow', 'blue', 'pink']
# print("the original color list: ", colors)
#
# first_color = colors.pop(0)
# print("the first color in the list: ", first_color)
# print("the left color list: ", colors)
#
# last_color = colors.pop()  # 不加索引值，表示取出最后列表中的最后一个元素
# print("the last color in the list: ", last_color)
# print("the left color list: ", colors)

# 3.根据值删除元素，remove()
# 如果列表中有多个元素的值相同，remove只会删除第一个元素
values = [1, 3, 5, 7, 9, 7, 5, 3, 1]
print("the value list: ", values)

values.remove(3)
print("the left value list: ", values)

del_value = 5
values.remove(del_value)
print("the left value list: ", values)