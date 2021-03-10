# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 006_列表.py
# @Author  : Machun Michael
# @Time    : 2020/5/18 19:41
# @Software: PyCharm


'''
0. 列表是啥？
    (0) 列表是一个有序集合，由一系列按照特定顺序排列的元素组成
    (1) 列表的元素可以是数字、字符、字符串等等
    (2) 用"[]"来表示列表，用","来分隔列表元素
    (3) 同一个列表，元素可以为不同类型

1. 如何访问列表元素？
    (0) 类似于访问数组元素，可以使用 “列表名+索引” 的方式访问列表元素。
    (1) 索引从0开始，python中的索引可以为负数。例如-1表示列表的最后一个元素，-2表示列表的倒数第2个元素
    (2) 注意，索引不能超过列表长度

2. 如何修改列表元素的值？
    给列表元素赋一个新的值，就可以修改元素的值

3. 如何在列表中新增元素？
    (0) append()，在列表末尾追加元素
    (1) insert()，在列表的指定位置前插入一个元素。索引值可以大于等于列表长度

4. 如何删除列表元素？
    (0) del语句，删除列表指定位置的元素
    (1) pop()，删除列表指定位置的元素。如果不指定位置，默认为列表末尾的元素。pop删除的元素，可以用一个变量来保存
    (2) remove()，根据元素的值来删除元素。如果要删除的元素有多个，只会删除第一个；如果需要删除多个，需要多次删除

5. 列表和数组、链表的异同点？
    (0) 列表和数组：可以通过索引来访问指定位置的元素；但列表的索引可以为负数，数组的索引必须非负
    (1) 列表和链表：可以动态的增加和删除
'''


names  = ["michae", "Tom", "Lucy", "Lily", "Sheldon"]
ages   = [25, 24, 23, 25, 22]
scores = ['A', 'B', 'A', 'A', 'C']
print(names)
print(ages)
print(scores)


# 如何访问列表元素？
message = names[0] + "is " + str(ages[0]) + " years old, and he got an " + scores[0]
print(message)
print(names[-1])
print(names[-2])
# print(names[-8])  # 索引值不能超过列表长度


# 如何修改列表元素的值？
print(names)
names[1] = "Tony"
print(names)


# 如何在列表中新增元素？
names.append("Jack")
ages.append(26)
scores.append('A')
message = names[-1] + "is " + str(ages[-1]) + " years old, and he got an " + scores[-1]
print(message)

# 同一个列表，元素可以为不同类型
list_empty = []       # 创建一个空列表
print(list_empty)
list_empty.append("hello")
print(list_empty)
list_empty.append("world")
print(list_empty)
list_empty.append(25)
print(list_empty)
list_empty.append('A')
print(list_empty)


# 插入元素，索引index表示在链表第index个位置前插入元素
print(names)
names.insert(0, "Jerry")
print(names)
names.insert(1, "Tom")
names.insert(-1, "Linda")
print(names)
names.insert(9, "linux")  # 如果想插入到链表末尾，索引值大于等于列表长度即可
print(names)


# 如何删除列表元素？
prog_language = ["C", "C++", "python", "go", "Java"]
print(prog_language)
del prog_language[0]
print(prog_language)
# del prog_language[4]  # 索引值不能超过列表长度
# print(prog_language)

prog_language.pop()
print(prog_language)
prog_language.pop(1)
print(prog_language)
prog_language.insert(1, "C#")
print(prog_language)
save_language = prog_language.pop()  # pop的元素，可以用一个变量来保存
print(prog_language)
print(save_language)


letter = ['A', 'B', 'C', 'A', 'D']
print(letter)
letter.remove('B')
print(letter)
letter.remove('A')  # 元素'A'出现了多次，但是只会删除第一个；如果需要删除多个，需要多次删除
print(letter)