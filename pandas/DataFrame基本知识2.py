"""
    DataFrame基本知识2:
        1.读取本地文件
        2.排序
        3.切片和索引
            取行和取列
            布尔索引
        4.缺失值处理
            NaN处理: 删除和填充
            0处理: 变为NaN
"""
# 导入
import pandas索引学习 as pd
import numpy as np
# 读取本地文件
df = pd.read_csv("./dogNames2.csv")
# print(df.head())
# print(df.info())

# 进行排序
df = df.sort_values(by="Count_AnimalName", ascending=False)
print(df.head(10))

# DataFrame的切片和索引
# 取行或列(方括号内写数字表示取行,对行进行操作;写字符串表示取列索引,对列进行操作)
print(df[:20])  # 取前20行
print(df["Row_Labels"])  # 取列索引名为Row_Labels的列

# DataFrame的布尔索引
t = df[(df["Row_Labels"].str.len() > 4) & (df["Count_AnimalName"] > 700)]
print(t)

# 缺失值处理
# 缺失值情况:为NaN或0
# 创建缺失值DataFrame数组
t1 = np.arange(100).reshape(10, 10).astype("float")
t1[3:6, 6:9] = np.nan
t2 = pd.DataFrame(t1, columns=list("ABCDEFGHIJ"))
print(t2)
print(pd.isnull(t2))
# 处理0方式 - 将0赋值为NaN,按照NaN的方式处理
# 处理NaN方式
# 1.删除
t3 = t2.dropna(axis=0, how="any")
print(t3)
# 2.填充数据
t4 = t2.fillna(t2.mean())
print(t4)
