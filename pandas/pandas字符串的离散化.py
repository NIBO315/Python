"""
    2006-2016电影信息表
    对电影的种类进行统计,算出每类电影的数量总和,并画图
"""
# 导入
import pandas索引学习 as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# print(df.head(2).columns)
# print(df["Genre"])

# 统计分类的列表
temp_list = df["Genre"].str.split(",").tolist()  # [[],[],[],....]
genre_list = list(set([i for j in temp_list for i in j]))  # set()函数用于去重

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
# print(zeros_df)

# 给每个电影出现的位置赋值1
for i in range(df.shape[0]):
    # zeros_df[0,["Sci-fi","Mucical"]] =1
    zeros_df.loc[i, temp_list[i]] = 1
# print(zeros_df.head(3))

# 统计每个分类的电影的数量和
genre_count = zeros_df.sum(axis=0)

# 进行排序
genre_count = genre_count.sort_values()
print(genre_count)

# 画图 - 条形图
_x = genre_count.index
_y = genre_count.values

plt.figure(figsize=(20, 8), dpi=80)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x)
plt.show()
