# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 009_创建数值列表.py
# @Author  : Machun Michael
# @Time    : 2020/6/1 19:07
# @Software: PyCharm

'''
1. range()函数：range可以生成一系列数字
    示例：range(1,9)会生成1~8这个8个数字，1表示开始的数字，9表示结束的数字，但不包括9

2. list()函数：可以将range生成的系列数字转换为列表

3. 可以使用min() & max() & sum()，找出列表中的最大最小值，以及求和

4. 列表解析：将for循环和创建新元素的代码合并成一行，可以减少代码量
'''


# 使用range()生成一系列数字
for num in range(1, 9):
    print(num)


# 使用list()将range()的结果转换为列表
odd_numbers  = list(range(1, 10, 2))   # 生成1~9之间的奇数列表，2为步长，表示间隔
even_numbers = list(range(0, 10, 2))   # 生成0~9之间的偶数列表，2为步长，表示间隔
print(odd_numbers)
print(even_numbers)

print("odd numbers for 1 to 9")
for x in odd_numbers:
    print(x)

print("even numbers for 1 to 9")
for x in even_numbers:
    print(x)


# 创建一个包含1~20平方的数值的列表
square = []                 # 创建一个空列表
print(square)

for x in range(1,20):
    square.append(x**2)     # 往列表中添加元素
print("square list is " + str(square))

# 列表解析
square_ex = [num**2 for num in range(1,20)]
print("square_ex list is " + str(square_ex))

# min() & max() & sum()
test_list = [1, 2, 8, 3, 0, 19, -1, -4]
print("the min number of test_list is " + str(min(test_list)))
print("the max number of test_list is " + str(max(test_list)))
print("the sum of test_list is " + str(sum(test_list)))

print(max(1, 5))
print(sum(range(1,10)))