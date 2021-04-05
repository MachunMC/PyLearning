# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 00_squares.py
# @Author  : Machun Michael
# @Time    : 2021/4/3 17:25
# @Software: PyCharm

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# 将输入的数字生成图形, linewidth指定线条的粗细
plt.plot(squares, linewidth=1)

# 添加标题，fontsize指定字体大小
plt.title("hello world", fontsize=20)

# 给x, y坐标添加标签
plt.xlabel('time', fontsize=15)
plt.ylabel('result', fontsize=15)

# 设置刻度标记的大小
# plt.tick_params(axis='both', labelsize=10)

# 显示绘制的图形
plt.show()
