"""
    pandas索引和复合索引
"""

import pandas as pd

file_path = "./directory.csv"
df = pd.read_csv(file_path)

grouped = df[["Store Number"]].groupby(by=[df["Country"], df["State/Province"]]).count()

# 索引的方法和属性
print(grouped.index)

