# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 018_模块导入.py
# @Author  : Machun Michael
# @Time    : 2020/6/21 17:14
# @Software: PyCharm

'''
0. 什么是模块？
    模块是包含源代码的文件

1. 什么是导入模块？
    (0) 导入模块，就是在文件A中，通过导入文件B，从而在A中可以使用B的代码，可以直接使用B中定义的函数
    (1) 导入模块，会将模块中的代码完全复制到本文件中，类似于C语言中的#include

2. 导入模块有什么好处？
    (0) 通过导入模块，可以直接使用模块中的函数，减少重复工作
    (1) 使得结构更加清晰

3. 导入模块的方法
    (0) 导入整个模块
        i. 格式：import module_name
        ii. 使用方法：module_name.func_name()
        iii. 说明：这种导入方法，在调用函数时，需要指定模块名；这里会将模块中的所有代码都复制到本文件中，不仅仅是函数
        iiii. 可以使用as给导入的模块指定别名：import module_name as module_alias
    (1) 导入特定函数
        i. 格式：from module_name import func_name
        ii. 使用方法：func_name()
        iii. 说明：这种导入方法，已经指定了要导入的函数，所以不需要指定模块名；这里只会将指定的函数复制到本文件中
        iiii. 可以使用as给导入的函数指定别名，这样可以防止导入的函数和本文件中的函数重名，也可以使得导入的函数名更加简短
              格式：from module_name import func_name as func_alias
    (2) 导入模块中的所有函数（不推荐）
        i. 格式：from module_name import *
        ii. 使用方法：func_name()
        iii. 说明：这种方法会将模块中的所有函数都导入到本文件中，但是可能会出现，导入的函数和本文件中的函数重名的情况。
                  而此时调用函数无需指定模块名，所以可能会发生意想不到的情况。所以不推荐这种方法

4. import语句需要放到文件开头位置
'''

# 导入整个模块
import MathModule

# 求和
sum = MathModule.func_sum(1, 2, 3)
print(sum)

# 求积
product = MathModule.func_product(1, 4, 6, 9)
print(product)

# 求平方和
sum = MathModule.func_quadratic_sum(11, 24, 55, 99)
print(sum)

# 使用as给导入的模块指定别名
import MathModule as math_mod               # import语句需要放到文件开头位置，这里只是为了说明各种使用情况
sum = math_mod.func_sum(1, 2, 3, 4)
print(sum)

# 从模块中导入特定函数
from MathModule import func_sum             # import语句需要放到文件开头位置，这里只是为了说明各种使用情况
sum = func_sum(2, 4, 6, 8, 10, 12, 14, 16)
print(sum)

# 使用as给导入的函数指定别名
from MathModule import func_sum as my_sum   # import语句需要放到文件开头位置，这里只是为了说明各种使用情况
sum = my_sum(2, 4, 6, 8, 10, 12, 14, 16)
print(sum)