# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 013_字典.py
# @Author  : Machun Michael
# @Time    : 2020/6/6 23:05
# @Software: PyCharm

'''
1. 啥是字典？
    (1) 字典是用来存储信息的数据结构，包含了一系列键值对，每个键都和一个值相关联，该值可以为数字、字符、字符串、列表、字典等等
    (2) 例如可以用字典来存储个人信息，包含姓名、年龄、身份证号、家庭住址等等信息（这点类似于C的结构体）
    (3) 字典用"{}"表示，键和值之间用":"分隔，多个键值对之间用","分隔

2. 如何使用？
    dic_name[key_name]

3. 如何添加键值对？
    dic_name[key_name] = value

4. 如何修改键所对应的值？
    dic_name[key_name] = new_value
    备注：添加和修改键值对的格式是相同的，如果key在字典中不存在，则会新增对应的键值对；如果存在，则会修改键所对应的值

5. 如何删除键值对：del语句
    del dic_name[key_name]

6. 如何复制字典？
    不能用等号直接赋值，这相当于两个变量同时关联了一个字典

7. 如何遍历字典？
    for
'''


dic_tom = {
    'name':'Tom',
    'gender':'Male',
    'age':25,
    'addr':'China Shanghai',
    }

print(dic_tom['name'] + ", " + dic_tom["gender"] + ", " + str(dic_tom["age"]) + " years old, and lives in" + dic_tom["addr"])

# 添加键值对
dic_tom["job"] = "engineer"
print("dictionary of tom: " + str(dic_tom))

# 修改键所对应的值
dic_tom["job"] = 'teacher'
print("new dictionary of tom: " + str(dic_tom))

# 删除键值对
del dic_tom["job"]
print("dictionary of tom: " + str(dic_tom))

# 如何复制字典？不能直接用等号赋值
dic_lucy = dic_tom              # 不是赋值，而是dic_lucy和dic_tom关联到同一个字典
print("dictionary of tom:  " + str(dic_tom))
print("dictionary of lucy: " + str(dic_lucy))

dic_lucy["name"] = "lucy"       # 修改dic_lucy，dic_tom同样也会被修改
print("dictionary of tom:  " + str(dic_tom))
print("dictionary of lucy: " + str(dic_lucy))

# 遍历字典