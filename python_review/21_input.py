# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 21_input.py
# @Author  : Machun Michael
# @Time    : 2021/3/26 21:40
# @Software: PyCharm

# input()等待用户输入数据，之后将用户输入的数据保存到变量中
# input()可以传入一个参数，作为提示和说明
message = input("please tell me something, and I'll repeat it to you: ")
print('You said:', message)

# 获取数值输入：int()
# python将用户的输入数据当作字符串，所以需要将字符串转为int
age = input("please tell me how old are you? ")
print("you're %d years old." %(int(age)))