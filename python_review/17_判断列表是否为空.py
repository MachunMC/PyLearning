# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 17_判断列表是否为空.py
# @Author  : Machun Michael
# @Time    : 2021/3/24 21:30
# @Software: PyCharm

scores = [100, 99, 88, 76, 44]
if scores:     # 当列表不为空时返回True，否则返回False
    print("score list is not empty")
    for score in scores:
        print(score)
    # else:
    #     print("score list is empty")
else:
    print("score list is empty")

# 注意：上面两种不同的缩进写法，执行不会报错，但执行的结果不同




