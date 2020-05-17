# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 003_字符串test.py
# @Author  : Machun Michael
# @Time    : 2020/5/17 17:40
# @Software: PyCharm

# 个性化消息
user_name = "machun"
message = "hello " + user_name + ", " + "would you like to learn some python today?"
print(message.title())

# 调整名字的大小写
init_name = "michael machun"
title_name = init_name.title()
lower_name = init_name.lower()
upper_name = init_name.upper()
print("init name: ", init_name)
print("title name: ", title_name)
print("lower name: ", lower_name)
print("upper name: ", upper_name)

# 名言
famous_words = "Albert Einstein once said, 'A person who never made a mistake never tried anything new.'"
print(famous_words)

# 剔除人名中的空白
name = "\tmachun michael\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())