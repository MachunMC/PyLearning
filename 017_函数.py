# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 017_函数.py
# @Author  : Machun Michael
# @Time    : 2020/6/16 19:31
# @Software: PyCharm

'''
0. 函数定义
    (0) 格式：def func_name(param0, param1...):
                function body

1. 参数默认值
    (0) 在定义函数时，可以指定参数默认值。在调用函数时，如果传递了实参，则使用实参值；如果没有传递实参，则使用默认值。
    (1) 这样可以简化函数调用
    (2) 指定默认值的形参，一定要放在靠右边的位置。如果给中间位置的参数指定默认值，在传递实参时，容易产生歧义

2. 调用函数时，如果指定了形参名，可以不用考虑参数传递的顺序。但是不推荐这种方法，最好按顺序传递参数，这样比较清晰易懂，而且更加简洁

3. 函数返回值
'''

# 定义函数
def display_message(name, book):
    print(name + "'s favorite book is " + book)

display_message("Michael", "平凡的世界")
display_message("Ton", "人生海海")
display_message(name="Jarry", book="围城")           # 传递参数时，可以指定对应的形参名
display_message(book="张居正", name="Jack")          # 如果传递参数时指定了对应的形参名，可以无需考虑参数顺序

# 函数参数默认值
# def func_introduction(name, age, addr="Shanghai, China", sport):
def func_introduction(name, age, addr="Shanghai, China"):
    print("Hello everyone, my name's " + name + ", I'm " + str(age) + " years old, and I lives in " + addr)

# func_introduction("Tom", 21, "basketbal")          # 如果指定中间位置的参数使用默认值，这样不知道"basketbal"传递给addr，还是sport
func_introduction("Tom", 21)
func_introduction("Michael", "24", "Anhui, China")   # 如果24用引号括起来，则认为传递的是字符串类型

# 函数返回值，返回整形
def func_sum(num0, num1, num2=0):
    sum = num0 + num1 + num2
    return sum

sum = func_sum(1, 2001)
print(sum)

def func_fullname(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

full_name = func_fullname("Michael", "John")
print("His  full name is " + full_name)


# 列表作为形参
names = ["Tom", "Michael", "lucy", "jack", "jerry"]
greetings = []

# 这里会修改传入的列表内容
def say_hello(names, greetings):
    for name in names:
        greetings.append("Hello " + name + "!")

def print_message(messages):
    for message in messages:
        print(message)

say_hello(names, greetings)
print(greetings)
print_message(greetings)