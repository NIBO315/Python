# 导入
import numpy as np
import random

# 创建数组
t1 = np.array([random.randint(0, 50) for i in range(20)]).reshape((4, 5))

print(t1)
print("-" * 100)
# 修改数值
t1[0, 0] = 0
print(t1)

t1[2:4, 3:5] = 1
print(t1)
print("-" * 100)

# numpy中的布尔索引
print(t1 < 10)
t1[t1 < 10] = 3
print(t1)
print("-" * 100)

# numpy中的三元运算符
t2 = np.where(t1 < 10, 0, 100)
print(t2)

# numpy中的裁剪
t3 = t1.clip(10, 20)
print(t3)

# numpy中nan的赋值
t1 = t1.astype(float)
t1[0, 0] = np.nan
print(t1)
