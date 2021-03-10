# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 016_while循环.py
# @Author  : Machun Michael
# @Time    : 2020/6/16 15:42
# @Software: PyCharm


# 如何检查用户输入是否合法？
print("Please input a number, and then I will guess the number, enter 999 to end the game.")
num = int(input("Now let's begin, please enter a number:"))
ply_count = 1

while num != 999:
    print("I guess the number you enter is:" + str(num) + ". Is it right? Haha.")
    num = int(input("Would you wanna try again? If yes, please enter a number, if no, please enter 999:"))

    if num == 999:
        print("Oh, it's so pity that you don't want to play it again. Looking forward to play with you next time.")

    ply_count = ply_count + 1  # ply_count += 1
    if ply_count >= 10:
        print("Oh, I'm tired, and I want to take a break.Looking forward to play with you next time.")
        break