# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 010_切片.py
# @Author  : Machun Michael
# @Time    : 2020/6/1 19:41
# @Software: PyCharm

'''
0. 啥叫切片？
    切片就是列表的部分元素

1. 如何创建切片？
    通过指定列表的起始元素和结束元素，中间用冒号分隔，来创建一个切片，创建后的切片依然是一个列表

2. 复制列表
    (0) 可以通过切片的方式复制列表
    (1) 不能用赋值的方式来复制列表，用赋值的方式，其实关联的是同一个列表

'''


# 创建切片
animals = ["dog", "cat", "rabbit", "snake", "monkey", "elephant"]
print("animals list is: " + str(animals))

section_animals = animals[1:4]
print("section of animals list is: " + str(section_animals))

print(animals[2:4])
print(animals[:4])      # 省略起始元素索引，默认从第0个开始
print(animals[1:])      # 省略结束元素索引，默认到最后一个结束
print(animals[:])       # 省略起始和结束元素索引，默认为整个列表


# 遍历切片
for animal in animals[0:3]:
    print(animal)


# 赋值“复制”列表（关联列表）
animals_ex0 = animals    # 用直接赋值的方式，animals和animals_ex其实表示的是同一个列表
print("animal     list is: " + str(animals))
print("animal_ex0 list is: " + str(animals_ex0))

animals.append("fish")
animals_ex0.append("horse")
print("animal     list is: " + str(animals))
print("animal_ex0 list is: " + str(animals_ex0))


# 切片复制列表
animals_ex1 = animals[:]  # 用切片方式，可以复制一个列表
print("animal     list is: " + str(animals))
print("animal_ex1 list is: " + str(animals_ex1))

animals.append("fox")
animals_ex1.append("lion")
print("animal     list is: " + str(animals))
print("animal_ex1 list is: " + str(animals_ex1))