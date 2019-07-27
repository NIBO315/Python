# 导入
import numpy as np
import random

# 创建数组
t1 = np.array([random.randint(1, 100) for i in range(100)]).reshape((10,10))
t2 = np.array([random.randint(1, 100) for i in range(100)]).reshape((10,10))

# print(t1)
print(t2)
print("-" * 100)

# 竖直拼接
print(np.vstack((t1, t2)))
print("-" * 100)

# 水平拼接
print(np.hstack((t1, t2)))

# 数组的行交换
t1[[1, 3], :] = t1[[3, 1], :]
print(t1)

# 数组的列交换
t2[:, [0, 2]] = t2[:, [2, 0]]
print(t2)
