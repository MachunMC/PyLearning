# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 20_嵌套.py
# @Author  : Machun Michael
# @Time    : 2021/3/26 21:25
# @Software: PyCharm

# 有时候，需要将一系列字典存储到列表中，或者将列表中的值存储到字典中，这种称为嵌套

# 1.字典列表（字典类似于结构体，列表类似于数组，字典列表就类似于结构体数组）
dog_tom   = {'name' : 'tom', 'age' : '2'}
dog_jack  = {'name' : 'jack', 'age' : 1}
dog_jerry = {'name' : 'jerry', 'age' : 3}
dogs = [dog_tom, dog_jack, dog_jerry]  # 列表元素是字典
print(dogs)


# 2.在字典中存储列表
# 字典中某个键所对应的值，可以是列表
person = {
    'name' : 'michael',
    'age' : 26,
    'addr' : 'shanghai',
    'language' : ['C', 'C++', 'python', 'go']
}
print(person)


# 3.在字典中存储字典
# 字典中某个键所对应的值，可以是字典
users = {
    'tom' : {'age':22, 'addr':'beijing'},
    'jack' : {'age':23, 'addr':'shanghai'},
}
print(users)