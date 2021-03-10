# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 02_string1.py.py
# @Author  : Machun Michael
# @Time    : 2021/3/10 19:51
# @Software: PyCharm

# 字符串拼接：使用+来拼接字符串
# first_name = "li"
# last_name = "ming"
# full_name = first_name + " " + last_name
# print(full_name)
# print(full_name.title())
#
# greet_message = "Hello" + " " + full_name.title() + ", nice to meet you!"
# print(greet_message)


# 制表符table '\t'
# 换行符 '\n'
# print('\thello\n')


# 删除多余空格
# 删除字符串开头的所有空格：lstrip
# 删除字符串末尾的所有空格：rstrip
# 删除字符串两端的所有空格：strip
# question：如何删除字符串中间部分的空格？

space_str = "  hello space   "
print(space_str)
print(space_str.lstrip())
print(space_str.rstrip())
print(space_str.strip())
