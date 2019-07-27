# 导入
import numpy as np
import random

# 创建全为0的数组
print(np.zeros((2, 3)))

# 创建全为1的数组
print(np.ones((3, 4)))

# 创建单元方阵 - 对角线为1,其他均为0
print(np.eye(10))

t1 = np.array([random.randint(1, 1000) for i in range(100)]).reshape((10, 10))
print(t1)

# 求最值所在位置的索引
print(np.argmax(t1, axis=0))  # 按行查找
print(np.argmin(t1, axis=1))  # 按列查找

# numpy生成随机数
print(np.random.rand(2, 3))
print(np.random.randn(2, 3))
print(np.random.randint(10, 20, (3, 4)))

np.random.seed(11)
t = np.random.randint(10, 30, (5, 6))
print(t)
