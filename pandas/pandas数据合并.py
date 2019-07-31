"""
    数据合并 - join的使用
    join默认情况下把行索引相同的数据合并到一起

    数据合并 - merge的使用
    merge按照指定的列把数据按照一定的方式合并到一起,默认情况下取并集为内连接
"""
# 导入
import pandas索引学习 as pd
import numpy as np

# 创建数组
d1 = pd.DataFrame(np.ones((3, 4)), columns=list("wxyz"), index=list("ABC"))

d2 = pd.DataFrame(np.arange(8).reshape((2, 4)), columns=list("abcd"), index=list("AB"))

d3 = pd.DataFrame(np.ones((2, 3)), columns=list("fbx"))

# join合并
print(d1)
print(d2)
print(d1.join(d2))  # 以d1的格式为准则
print(d2.join(d1))  # 以d2的格式为准则

# merge合并
print(d2)
print(d3)
# 内连接
# print(d2.merge(d3, on="b"))  # 以d2为标准
# print(d3.merge(d2, on="b"))  # 以d3为标准
# 外连接
print(d2.merge(d3, on="b", how="outer"))
# 左连接
print(d2.merge(d3, on="b", how="left"))  # 以d2为标准
# 右连接
print(d2.merge(d3, on="b", how="right"))  # 以d3为标准
