# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 011_元组.py
# @Author  : Machun Michael
# @Time    : 2020/6/6 13:57
# @Software: PyCharm

'''
0. 元组（tuple）是啥？
    (0) 元组是不可变的列表
    (1) 用圆括号表示，可以用索引来访问元组的元素

1. 修改元组的值
    虽然元组元素的值不能修改，但是可以修改元素变量的值，相当于修改元组所有元素的值。通过这种方式，达到了修改元组元素的目的
'''

# 定义元组
rectangle = (20, 10)
print("the lenth of rectangle is " + str(rectangle[0]) + ", and the width of rectangle is " + str(rectangle[1]))

# 尝试修改元组元素的值
#rectangle[0] = 120     # 修改元组元素的值，会提示报错
#print("the lenth of rectangle change to " + str(rectangle[0]))

# 遍历元组
print("traverse of the rectangle tuple start")
for x in rectangle:
    print(x)
print("traverse of the rectangle tuple end")

# 修改元组的值
rectangle = (5, 8)
print("the new lenth of the rectangle is " + str(rectangle[0]) + ", and the new width of rectangle is " + str(rectangle[1]))