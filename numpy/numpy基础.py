"""
    numpy的基本使用:
        1.创建
        2.获取数组中数据的类型
        3.numpy的数据类型
        4.改变数据类型
        5.numpy中的小数及取位数
        6.numpy数组的形状
        7.numpy改变数组的形状
"""
# 导入
import numpy as np
import random

# 三种用numpy创建数组的方法
t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(2, 12, 2)
print(t3)
print(type(t3))

print("*" * 100)
# dtype用于获取数组中数据的类型
print(t3.dtype)

# numpy中的数据类型
t4 = np.array(range(1, 4), dtype=float)
print(t4)
print(t4.dtype)

t5 = np.array([1, 1, 1, 0, 0, 1], dtype=bool)
print(t5)
print(t5.dtype)

# astype用于改变数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

print("*" * 100)
# numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

# round用于取小数后的位数
t8 = np.round(t7, 2)
print(t8)
print(t8.dtype)

print("*" * 100)
# numpy数组的形状
t11 = np.arange(12)
print(t11)
print(t11.shape)

t12 = np.array([[1, 2, 3], [2, 3, 5]])
print(t12)
print(t12.shape)

t13 = np.array([[[2, 3, 4], [3, 4, 5]], [[5, 6, 7], [7, 8, 9]]])
print(t13)
print(t13.shape)

# numpy中改变数组的形状
t14 = np.arange(12)
print(t14)
# reshape是重新创造一个数组
t15 = t14.reshape((3, 4))
print(t15)

t16 = np.arange(24).reshape((2, 3, 4))
print(t16)

# t15.shape[0] * t15.shape[1] - 可以获取数组的行和列
t17 = t15.reshape(t15.shape[0] * t15.shape[1])
print(t17)

# flatten方法可以将数组快速的展成一维数组
t18 = t15.flatten()
print(t18)
