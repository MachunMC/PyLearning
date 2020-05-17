# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 002_字符串.py
# @Author  : Machun Michael
# @Time    : 2020/5/16 18:51
# @Software: PyCharm

'''
1. python中，用引号括起来的内容称为字符串，既可以用单引号，又可以用双引号。
  灵活的使用单双引号，可以在一个字符串中，既包含单引号，又包含双引号

2. 方法：方法是对数据执行相应的操作，方法后面会跟一对小括号，表示传参，参数可以为空
    (1) 修改大小写
        i. title()：将每个单词的首字母改成大写
        ii. upper()：将所有字符改成大写
        iii. lower()：将所有字符改成小写
    (2) 拼接字符串:python使用“+”来拼接字符串
    (3) 删除多余的空格（可用于删除用户输入数据中多余的空格）
        i. lstrip()：删除开头多余的空格
        ii. rstrip()：删除末尾多余的空格
        iii. strip()：删除开头和末尾多余的空格
        备注：strip可以通过传入字符，来删除字符串中指定的字符
'''

print("This is a string!")
print('This is also a string!')
print("My name's michael.")
#print('My name's michael.')        # 错误写法

# 修改大小写
name = "machun michael"
str = "ABCDEFG"
print(name.title())
print(name.upper())
print(name.lower())
print(str.title())
print(str.upper())
print(str.lower())

# 拼接字符串
first_name = "ma"
last_name  = "chun"
full_name = first_name + " " + last_name
message = "hello " + full_name
print(full_name)
print(full_name.title())
print(message.title())

# 删除额外的空白
init_info    = "  This is a string with some space   "
rstrip_info = init_info.rstrip()
lstrip_info = init_info.lstrip()
strip_info  = init_info.strip()
print("init info:", init_info)
print("after rstrip:", rstrip_info)
print("after lstrip:", lstrip_info)
print("after strip:", strip_info)

# 删除指定的字符
before_str = "AABBCCDDEEFF"
after_str = before_str.strip('A')
print(before_str)
print(after_str)
