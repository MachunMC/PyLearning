# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 10_遍历列表.py
# @Author  : Machun Michael
# @Time    : 2021/3/22 7:54
# @Software: PyCharm

# 使用for循环遍历列表
prog_languages = ['C', 'C++', 'Python', 'Java', 'Go', 'Shell Script']
print("打印整个列表：", prog_languages)

print("使用for循环遍历列表")
for language in prog_languages:
    print(language)

# 解读：依次从列表prog_languages中取出一个值，保存到变量language中，然后再打印language的值