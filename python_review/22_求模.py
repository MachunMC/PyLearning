# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 22_求模.py
# @Author  : Machun Michael
# @Time    : 2021/3/30 20:52
# @Software: PyCharm

# %表示取模，也是取两个数相除的余数
# 在其他语言中，如C、C++、Java中，%表示取模
# 取余和取模，在除数和被除数同号时，结果一致；异号时有区别
#示例：求1~9之间的偶数
for num in range(1,10):
    if num % 2 == 0:
        print(num)

print(2%1)
print(20%3)
print(20%-3)  # c++中运行结果为2，python运行结果为-1