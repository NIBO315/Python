# 导入
import pandas as pd
import numpy as np

# 创建DataFrame数组
# 普通创建
t1 = pd.DataFrame(np.arange(12).reshape(3, 4))
t2 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("ABC"), columns=list("WXYZ"))
print(t1)
print(t2)

print("*" * 100)
# 通过字典创建
d1 = {"name": ["xiaoming", "xiaohong", "xiangzhuang", "xiaohei", "xiaobai"],
      "age": [20, 23, 22, 21, 24],
      "tel": [10086, 10010, 10011, 10023, 11011]}

d1 = pd.DataFrame(d1)

d2 = [{"name": "xiaoming", "tel": 10086},
      {"name": "xiaohong", "age": 23},
      {"name": "xiaoni", "age": 24}]
print(pd.DataFrame(d2))

print("*" * 100)
# DataFrame的基本属性
print(d1.index)
print(d1.columns)
print(d1.values)
print(d1.shape)
print(d1.dtypes)
print(d1.ndim)

print("*" * 100)
# DataFrame整体情况查询
df = pd.DataFrame(d1)
print(df.head(3))
print(df.tail(2))
print(df.info())
print(df.describe())
