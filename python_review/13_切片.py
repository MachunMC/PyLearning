# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 13_切片.py
# @Author  : Machun Michael
# @Time    : 2021/3/22 19:13
# @Software: PyCharm

# 处理列表的部分元素，叫做切片
# 切片后的结果，也是一个列表
cities = ['Anhui', 'Beijing', 'Chongqing', 'guangdong', 'guangxi', 'shanghai']

# 类似于range()函数，创建切片，也需要指定一个起始索引和一个结束索引
print("原始列表:", cities)
print("cities[1:4]", cities[1:4])

# 如果只有起始索引，没有结束索引，则表示取到最后一个
# 如果只有结束索引，没有起始索引，则表示从第0个开始取
print("cities[0:]：", cities[0:])
print("cities[:3]：", cities[:3])

# 使用列表最后几个元素的切片
# 负数索引表示距离列表末尾相应距离的索引
print(cities[-3:])  # 表示从列表倒数第3个，到列表末尾的切片


# 遍历切片
pro_languages = ['C', 'C++', 'python', 'Go', 'Java']

print('Here are the top 3 of my kown program languages')
for pro_language in pro_languages[0:3]:
    print(pro_language)