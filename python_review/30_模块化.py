# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 30_模块化.py
# @Author  : Machun Michael
# @Time    : 2021/4/3 16:52
# @Software: PyCharm

# 模块是独立的文件，模块中存储的是函数
# 当程序中需要使用到模块中的函数时，使用import将模块导入到程序中即可
# 模块化可以让别人使用你写的代码

# 1.导入整个模块
# 导入方法：import 模块名称（.py文件名）
# 模块中的函数使用方法：模块名.函数名()
# import xxx类似于C中的include，python会将模块中的所有函数复制到该文件中
import pizza

pizza.make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 2.导入特定函数
# 导入方法：from 模块名 import 函数名0,函数名1
# 模块中的函数使用方法：函数名()，因为这里已经显示的指定了导入哪些函数，所以这里直接使用函数名即可
from pizza import make_pizza, make_salad, make_noodles

make_pizza('mushrooms', 'green peppers', 'extra cheese')
make_salad('mushrooms', 'green peppers', 'extra cheese')
make_noodles('mushrooms', 'green peppers', 'extra cheese')


# 3.给导入的函数起别名
# 目的：为了防止导入的函数和本文件中的函数重名，或者导入的函数名太长，可以给函数起别名
# 方法：from 模块名 import 函数名 as 别名
from pizza import make_pizza as mp
from pizza import make_salad as ms

mp('mushrooms', 'green peppers', 'extra cheese')
ms('mushrooms', 'green peppers', 'extra cheese')


# 4.给导入的模块起别名
# 目的：简化模块名称
# 方法：import 模块名 as 别名
import pizza as pi

pi.make_pizza('mushrooms', 'green peppers', 'extra cheese')
pi.make_salad('mushrooms', 'green peppers', 'extra cheese')


# 5.导入模块中的所有函数（不推荐使用）
# 方法：from 模块名 import *
# 备注：使用这种方法可以导入该模块中的所有函数，但可能会因为导入的模块中，有函数名与本文件中的函数同名，
#       进而出现异常，所以不推荐这种方法。要么导入具体函数，要么导入整个模块。导入整个模块时，调用函数
#       需要指定模块名，所以不会有函数同名的问题