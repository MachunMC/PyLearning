# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 11_创建数值列表.py
# @Author  : Machun Michael
# @Time    : 2021/3/22 8:03
# @Software: PyCharm


# 1.生成一系列整数：range()函数
print(range(1,8))  # 这里只会原样输出range(1, 8)

# 需要使用for循环来打印range返回的结果
# 会生成从1到8之间的整数，包括1，不包括8
for value in range(1, 8):
    print(value)

# 生成-11到11之间的整数
# 注意，传入的两个参数，只能是整数
for value in range(-11, 11):
    print(value)


# 2.使用list()函数，将range生成的一系列数字，转换为列表
number = list(range(1, 20))
print(number)
print(len(number))


# 3.使用range()时，可以指定步长（两个数之间的间隔）
even_num = list(range(2, 11, 2))
uneven_num = list(range(1, 11, 2))
print("1到11（不包括11）之间的偶数有：", even_num)
print("1到11（不包括11）之间的奇数有：", uneven_num)


# 4.创建一个只包含1到10的平方的值的列表
num_list = []
for tmp in range(1,11):
    num_list.append(tmp * tmp)
print(num_list)


# 5. 数值列表中常用的几个函数
# max()：取出列表中的最大值
# min()：取出列表中的最小值
# sum()：列表求和
num_list = [1, 3, 5, 2, 6, 9, 88, 2, -9]

print("max(num_list):", max(num_list))
print("min(num_list):", min(num_list))
print("sum(num_list):", sum(num_list))