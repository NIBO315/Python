"""
    pandas索引和复合索引
"""
# 导入
import pandas as pd
import numpy as np
import random

# 索引的方法和属性

df = pd.DataFrame(np.array([random.randint(0, 100) for i in range(12)]).reshape((3, 4)), index=list("ABC"))
print(df)

# 1.显示索引
print(df.index)

# 2.更改索引
df.index = ["a", "b", "c"]
print(df)

# 3.从df中取出a,f两行,有则取出,无则赋值为NaN并构成一个新的数组
df1 = df.reindex(["a", "f"])
print(df1)

# 4.从df中取一列作为所有行的索引,并构造一个新数组,原数组不改变
df2 = df.set_index(0)
print(df2)

# 5.设置复合索引
df3 = df.set_index([0, 1])
print(df3)

# 复合索引取值
# 1.构造复合索引
a = pd.DataFrame({'a': range(7),
                  'b': range(7, 0, -1),
                  'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                  'd': list("hijklmo")})
print(a)
print("*" * 100)
# 2.构造DataFrame类型的复合索引
b = a.set_index(["c", "d"])
print(b)

# DataFrame复合索引取值
print(b.loc["one"].loc["h"])
print(b.swaplevel().loc["h"])

print("*" * 100)
# 3.构造Series类型的复合索引
c = b["a"]
print(c)

# Series复合索引的取值
print(c["one"])
print(c["one"]["j"])

d = a.set_index(["d", "c"])["a"]
print(d)
# 交换内外索引
e = d.swaplevel()
print(e)
print(e["one"])
