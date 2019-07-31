"""
    pandas数据的分组和聚合:
        分组: df.groupby(by) - 按照某一列进行分组
            DataFrameGroupBy - 分组后的数据元组
        聚合: 通过分组后的数据元组进行聚合操作,如统计数量,平均值等
"""
import pandas索引学习 as pd
import  numpy as np

file_path = "./directory.csv"
df = pd.read_csv(file_path)

# print(df.info())
# print(df.head(1))

# 进行分组
grouped1 = df.groupby(by="Country")
print(grouped1)

# DataFrameGroupBy
# 1.可以进行遍历
for i, j in group:
    print(i)
    print("-" * 100)
    print(j, type(j))
    print("*" * 100)

# 2.调用聚合方法
# 统计每个国家星巴克的数量
country_count = group["Store Number"].count()
print(country_count["US"])
print(country_count["CN"])


# 统计中国各个省份店铺的数量
china_data = df[df["Country"] == "CN"]
grouped = china_data.groupby(by="State/Province").count()["Store Number"]
print(grouped)


# 按照多个数据进行分组 - 返回Series,by的时候若为DataFrame则可以不要加df,若为Series则需要加df
grouped2 = df["Store Number"].groupby(by=[df["Country"], df["State/Province"]]).count()
print(grouped2)
print(type(grouped2))

# 按照多个数据进行分组 - 返回DataFrame
grouped3 = df[["Store Number"]].groupby(by=[df["Country"], df["State/Province"]]).count()
print(grouped3)
print(type(grouped3))
