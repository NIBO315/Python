# 导入
import pandas as pd
import numpy as np
import string

# 创建Series数组
t1 = pd.Series([34, 12, 5, 47, 9])
print(t1)

t2 = pd.Series([3, 4, 5, 6, 7], index=list("abcde"))
print(t2)

temp_dict = {"name": "xiaoming", "age": 20, "tel": 10086}
t3 = pd.Series(temp_dict)
print(t3)

a = {string.ascii_uppercase[i]: i for i in range(10)}
print(pd.Series(a, index=list(string.ascii_uppercase[5:15])))

t = pd.Series(np.arange(10), index=list(string.ascii_uppercase[:10]))
print(t)

print("-" * 100)

# pandas的切片和索引

# 切片的相关方法
# 取单值
print(t1[2])
# 取连续值
print(t1[:4])
# 字典取值
print(t3["age"])
print(t3[0])
print(t3[["age", "name"]])
# 取不连续值
print(t3[[0, 2]])

# 索引的相关知识
print(t.index)
print(t.values)

# where方法
s = pd.Series(range(5))
print(s)
t = s.where(s > 2, 10)
print(t)

