# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 16_if.py
# @Author  : Machun Michael
# @Time    : 2021/3/24 21:01
# @Software: PyCharm

# cars = ['bmw', 'audi', 'benz', 'tesla']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())


# 同时判断多个条件，使用and和or
# 同时满足两个条件，使用and；只要其中一个条件，使用or
# age = 270
# if age < 0 or age > 100:
#     print("your age %d is abnormal" %(age))
# else:
#     print("your age is:", age)

# sex = 'male'
# if age >= 18 and sex == 'male':
#     print("you are allowed in")
# else:
#     print("you are not allowed in")

# if ... else ...
# if ... elif ... else
# 记住不要使用else if
scores = [0, 22, 55, 60, 88, 99, 100, -1, 199]
for score in scores:
    if score >= 0 and score < 60:
        print("你的成绩是：%d，不及格" %(score))
    elif score >= 60 and score < 80:
        print("你的成绩是：%d，及格" %(score))
    elif score >= 80 and score <= 99:
        print("你的成绩是：%d，良好" %(score))
    elif score == 100:
        print("你的成绩是：%d，完美" %(score))
    else:
        print("你的成绩是：%d，成绩出错了" %(score))