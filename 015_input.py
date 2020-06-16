# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 015_input.py
# @Author  : Machun Michael
# @Time    : 2020/6/16 15:15
# @Software: PyCharm

'''
0. input()
    (0) 格式：var = input("This is a notice")
    (1) 说明：input函数等待用户输入，并将输入信息保存到var变量中。其中，input中可以加提示信息，告诉用户输入什么内容，也可以不加
    (2) 当提示信息需要多行时，可以用"\n"来换行，可以将多行信息保存到一个变量中，也可以直接在input中拼接字符串
    (3) input输入获得的变量为字符串类型，如果输入的是数字，可以用int()转换为整形
'''

# input()
name = input("please input your name:")
age  = input("please input your age:")
job  = input("please input your job:")
# null = input()  # 没有提示信息，不友好
print("Hello everyone, my name's " + name + ", and I'm " + age + " years old, I am a " + job)


# 提示信息分多行
notice = "Good moring, it's nice to meet you." +  "\nWhat's your name:"
name_0 = input("Good moring, it's nice to meet you." +  "\nWhat's your name:")
print("Hello " + name_0)


# input获取数值输入
salary = input("Please input your salary:")
if int(salary) >= 30000:
    print("your are so rich.")
else:
    print("your are not so rich as me")