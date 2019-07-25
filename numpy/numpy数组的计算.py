# 导入
import numpy as np
import random

# 创建数组并改变形状
t1 = np.array([random.randint(1, 100) for i in range(12)])
print(t1)

t2 = t1.reshape((3, 4))
print(t2)

print("-" * 100)
# 数组和数的计算 - 广播性质,每个数都+-*/2
print(t1 + 2)
print(t2 - 2)
print(t1 * 2)
print(t1 / 0)

print("-" * 100)
# 数组和数组的计算 - 数组形状相同时,对应位置的数进行加减乘除
# 形状不完全相同时,对应的行或列进行计算
# 形状完全不同时,不可进行计算
t3 = np.arange(100, 124).reshape((4, 6))
t4 = np.arange(10, 34).reshape((4, 6))
t5 = np.arange(10, 16)
t6 = np.array(range(10))
print(t3)
print(t4)
print(t3 + t4)
print(t3 * t4)
print(t3 - t4)
print(t3 / t4)
print(t4 - t5)
# print(t4 + t6)
print("-" * 100)
