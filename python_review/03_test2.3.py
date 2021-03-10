# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 03_test2.3.py
# @Author  : Machun Michael
# @Time    : 2021/3/10 20:37
# @Software: PyCharm

# 2.3节课后试一试

# 2-3 个性化消息
name = "Li ming"
greeting_msg = "Hello " + name.title() + ", would you like to learn some Python today?"
print(greeting_msg)

# 2-4 调整名字的大小写
name_0 = "zhang san"
print("所有字母大写：" + name.upper())
print("所有字母小写：" + name.lower())
print("首字母大写：" + name.upper())

# 2-5 名言
person = "Albert Einstein"
famous_saying = '"A person who never made a mistake never tried anything new."'
print(person + " once said, " + famous_saying)

# 2-6 名言2（同上）

# 2-7 剔除人名中的空白
name_1 = " li si\t \n"
print("原始姓名：" + name_1)
print("剔除开头的空白：" + name_1.lstrip())
print("剔除末尾的空白：" + name_1.rstrip())
print("剔除两端的空白：" + name_1.strip())