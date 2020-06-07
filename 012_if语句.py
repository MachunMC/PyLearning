# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 012_条件语句.py
# @Author  : Machun Michael
# @Time    : 2020/6/6 14:33
# @Software: PyCharm

'''
1. 判断是否相等
    (1) 用"=="判断两边的值是否相等
    (2) 在判断是否相等时，区分大小写

2. 判断是否不相等：用"!="判断两边的值是否不相等

3. 判断数字大小：大于、大于等于、小于、小于等于

4. 逻辑与（and）和逻辑或（or）

5. 判断特定值是否在列表中：关键字 in

6. 判断特定值是否不在列表中：关键字 not in

7. if语句
    (1) if
    (2) if...else...
    (3) if...elif...else
'''

cars = ["Audi", "BMW", "Bentley", "Benz", "Bugatti", "Ferrari"]

# 判断是否相等
for car in cars:
    if car == "Bugatti":
        print("This " + car + " is very expensive.")
    elif car == "Ferrari":
        print("This " + car + " is expensive too.")
    else:
        print("I don't know if this " + car + " is expensive.")

# 判断是否不相等
score_tom = 1119
score_linda = 91
if score_tom != score_linda:
    print("Tom and linda has different score")
else:
    print("Tom and linda has the save score")

# 判断数字大小
if score_tom > 100 or score_tom < 0:
    print("The score is error, and score  is" + str(score_tom))
elif score_tom >= 90:
    print("Tom got an 'A'")
elif score_tom >= 80:
    print("Tom got a 'B'")
elif score_tom >= 60:
    print("Tom got a 'C'")
elif score_tom >= 0:
    print("Tom got a 'D'")

# 判断特定值是否（不）在列表中
fruits = ["apple", "banana", "peach", "orange", "lemon", "watermelon"]
fruit_0 = "pear"
fruit_1 = "watermelon"

if fruit_0 in fruits:
    print("I already have a(an) " + fruit_0)
else:
    print("I don't have a(an) " + fruit_0)

if fruit_1 not in fruits:
    print("I don't have a(an) " + fruit_1)
else:
    print("I already have a(an) " + fruit_1)



