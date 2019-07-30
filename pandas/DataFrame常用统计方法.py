# 导入
import pandas as pd
import numpy as np

# 导入本地文件
file_path = "IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

# 查看统计信息
print(df.info())

# 查看首行
print(df.head(1))

# 获取电影的平均评分
print(df["Rating"].mean())

# 获取导演的人数
print(len(set(df["Director"].tolist())))
# print(len(df["Director"].unique()))

# 获取演员人数
temp_actors_list = df["Actors"].str.split(",").tolist()
# actors_list = np.array(temp_actors_list).flatten()  # 有疑问
actors_list = [i for j in temp_actors_list for i in j]  # 有疑问
actors_num = len(set(actors_list))
print(actors_num)

print("-" * 100)
# 获取电影时长的最值及位置
max_runtime = df["Runtime (Minutes)"].max()
max_runtime_index = df["Runtime (Minutes)"].argmax()
min_runtime = df["Runtime (Minutes)"].min()
min_runtime_index = df["Runtime (Minutes)"].argmin()
print(max_runtime)
print(max_runtime_index)
print(min_runtime)
print(min_runtime_index)

# 获取电影时长中值
runtime_median = df["Runtime (Minutes)"].median()
print(runtime_median)
