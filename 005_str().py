# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 005_str().py
# @Author  : Machun Michael
# @Time    : 2020/5/18 19:22
# @Software: PyCharm

# str()，可以将非字符串类型转换为字符串

name = "michael"
age = 25
addr = "shanghai, China"
# age是int类型，不能直接使用，需要转换为字符串
# introduce = "hello, my name's " + name + ". I am " + age + "years old, and I live in " + addr
introduce = "hello, my name's " + name + ". I am " + str(age) + "years old, and I live in " + addr
print(introduce)