# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 18_字典.py
# @Author  : Machun Michael
# @Time    : 2021/3/24 21:39
# @Software: PyCharm

# 字典是一系列键值对，每个键都与一个值相关联，可以通过键来访问相关联的值
# 值可以是数字、字符串、列表、字典
# 键和值之间用冒号分隔，键值对之间用逗号分隔

person = {'name' : 'michael', 'sex' : 'male', 'age' : 26}
print(person)

# 通过键，可以访问字典中对应的值: 字典名[键名]
print("His name is " + person['name'] + ", and he is " + str(person['age']) + " years old.")

# 字典是一种动态结构，可随时添加键值对
person['addr'] = 'Shanghai'
person['job']  = 'engineer'
print(person)

# 创建空字典
dog = {}
print(dog)

dog['name'] = 'Jack'
dog['age']  = 2
print(dog)

# 修改字典中的值
dog['age'] = 3
print(dog)

# 删除键值对
del dog['age']
print(dog)


# 当字典内容较多时，可以分多行
favorite_language = {
    'michael' : 'C',
    'Jack' : 'C++',
    'Tom' : 'python',
    'Lucy' : 'java',
    'jerry' : 'go',
}
print(favorite_language)