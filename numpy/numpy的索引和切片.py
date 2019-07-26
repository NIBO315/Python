# 导入
import numpy as np
import random

# 创建10*10的二维数组
t1 = np.array([random.randint(0, 100) for i in range(100)]).reshape((10, 10))

print(t1)

print("-" * 100)

# 矩阵的逆置
print(t1.T)
print("-" * 100)

# 取一行 - 取第二行
print(t1[1])
print(t1[1, :])

# 取连续的几行
print(t1[2:4])
print(t1[2:4, :])

# 取不连续的几行
print(t1[[2, 5, 8], :])

# 取一列
print(t1[:, 0])

# 取连续的几列
print(t1[:, 2:5])

# 取不连续的几列
print(t1[:, [2, 4, 5, 6]])

# 取行和列 - 取某个值
print(t1[3, 4])

# 取某几行和某几列
print(t1[2:4, 5:8])

# 取某几个点
print(t1[[2, 5, 6], [0, 4, 7]])
