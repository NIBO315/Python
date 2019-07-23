"""
    散点图:判断变量之间是否存在数量关联趋势,展示离群点(分布规律)
    应用场景:不同条件(维度)之间的内在关联关系
            观察数据的离散聚合程度
    例：３月份和十月份每日的气温变化
"""
# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文字体
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

# 输入数据
y_3 = [11, 17, 16, 11, 12, 11, 12, 16, 16, 17, 18, 19, 12, 15,
       14, 17, 18, 21, 22, 23, 23, 24, 15, 20, 26, 21, 19, 20,
       23, 25, 22]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 21, 23, 17, 20, 19,
        18, 20, 23, 23, 24, 21, 26, 25, 27, 22, 20, 19, 17, 18,
        22, 24, 23]
x_3 = range(1, 32)
x_10 = range(34, 65)

# 调整图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 调整ｘ轴刻度
_x = list(x_3) + list(x_10)
_xticks_label = ["3月{}日".format(i) for i in x_3]
_xticks_label += ["10月{}日".format(i-33) for i in x_10]
plt.xticks(_x[::3], _xticks_label[::3], fontproperties=my_font, rotation=45)

# 使用scatter方法绘制散点图
plt.scatter(x_3, y_3, label="3月份")
plt.scatter(x_10, y_10, label="10月份")

# 添加信息
plt.xlabel("日期", fontproperties=my_font)
plt.ylabel("温度　单位('C)", fontproperties=my_font)

# 添加图例
plt.legend(prop=my_font)

# 显示
plt.show()
