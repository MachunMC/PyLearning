# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 29_传递任意数量的实参.py
# @Author  : Machun Michael
# @Time    : 2021/4/3 15:04
# @Software: PyCharm

# 有时提前无法预知函数需要接受多少个参数，所以python支持传递任意数量的实参
# 该函数只有一个形参 *toppings，表示可以接受任意多个实参，接受的实参，将统一保存到一个元组中
# 实际上，形参*toppings，表示定义一个名为toppings的空元组，函数调用传递的实参都保存到这个元组中
def make_pizza(*toppings):
    print(toppings)

    for topping in toppings:
        print('- ' + topping)

# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参，必须将任意数量实参放到最后（这是书上说的，但如果最后一个参数使用关键字实参，也可以执行成功）
# python先匹配位置实参和关键字实参，最后将其他的实参放到任意数量实参中
def make_pizza_pro(size, *toppings, name):
    print(name.title() + " is makeing a " + str(size) + ' inch pizza with followed toppings:')
    for topping in toppings:
        print('- ' + topping)

# make_pizza_pro(9, 'mushrooms', 'green peppers', 'extra cheese', name='michael')


# 使用任意数量的关键字实参
# 有时候需要接受任意数量的实参，但预先不知道传递给函数的是什么信息，这种情况下可以让函数接受任意数量的键-值对
# 在传入实参的同时，需要指定传入的是什么参数
# 参数**info表示让python创建一个名为info的空的字典，函数调用时传入的键值对都保存到整个字典中
def get_user_info(name, **info):
    user_info = {}  # 创建一个空字典
    user_info['name'] = name
    for key,value in info.items(): # 将info字典中的键值对插入到user_info字典中
        user_info[key] = value

    return user_info  # 将新字典返回

user_info = get_user_info('michael', age='21', addr='Shanghai', job='engineer')
print(user_info)
