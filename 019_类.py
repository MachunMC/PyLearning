# -*- coding: utf-8 -*-
# @Project : python_learning
# @File    : 019_类.py
# @Author  : Machun Michael
# @Time    : 2020/6/21 23:16
# @Software: PyCharm

'''
1. 类和实例
    (1) 类表示某些事物所共有的属性，比如Dog类
    (2) 实例是根据类所创建的对象

2. 定义类
    (1) 格式：class Class_name():
                    def __init__(self, param0, param1):
                        self.param0 = param0
                        self.param1 = param1

                    def func0(self):
                        body

    (2) 说明
        i. class关键字表示类
        ii. 类中的函数称为方法
        iii. __init__()是一个特殊的方法，每当根据类创建方法时，python都会自动运行这个方法。函数形参self必不可少，其他参数可有可无。
            另外，self开头的变量可供类中的方法使用，也可以供类的实例使用，这种变量称为属性

3. 根据类创建实例
    (1) 格式：var = class_name(param0, param1)
    (2) 说明：根据类创建实例时，python调用__init__()方法，__init__会创建一个对象，并将param0、param1分别做对应的赋值，
             随后会返回所创建的实例，用var来保存这个实例

4. 变量命名约定
    类的首字母用大写表示，实例用小写字母表示

5. 访问实例的属性和方法
    通过"."访问属性和调用方法

6. 给属性指定默认值
    每个属性都必须要有初始值，哪怕是0或者空字符串，所以可以在定义类的时候，给属性指定默认值

7. 修改属性的值

'''


# 定义类
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):
        print(self.name + " is eating.")

    def bark(self):
        print(self.name + " is barking.")

# 根据类创建实例
dog_tom = Dog("Tom", "3")       # 创建实例时，需要传入name和age参数
dog_jerry = Dog("jerry", 2)

# 访问实例的属性和调用方法
print("I have a dog, he's name is " + dog_tom.name +   ", and he's " + str(dog_tom.age)   + " years old.")
dog_tom.bark()

print("He has a dog, he's name is " + dog_jerry.name + ", and he's " + str(dog_jerry.age) + " years old.")
dog_jerry.bark()

# 给属性指定默认值
class Cat():
    def __init__(self, name):
        self.name = name
        self.age = 1        # 给age属性指定默认值

    def say_hello(self):
        print("hello little cat")

cat_lucy = Cat("lucy")
print("This cat is " + cat_lucy.name + ", and she is " + str(cat_lucy.age) + " years old")