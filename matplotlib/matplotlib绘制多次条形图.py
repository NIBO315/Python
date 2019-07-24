"""
    绘制多次条形图
    例:2017-4-14,4-15,4-16,三天票房数据变化
"""
# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

# 输入数据
a = ["猩球崛起3:终极之战", "敦刻尔克", "蜘蛛侠:英雄归来", "战狼2"]
b_14 = [2358, 399, 2358, 362]
b_15 = [12357, 156, 2045, 168]
b_16 = [15746, 312, 4497, 319]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]

plt.bar(range(len(a)), b_14, width=bar_width, label="2017-4-14")
plt.bar(x_15, b_15, width=bar_width, label="2017-4-15")
plt.bar(x_16, b_16, width=bar_width, label="2017-4-16")

# 设置X轴的刻度
plt.xticks(x_15, a, fontproperties=my_font)

# 添加描述信息
plt.xlabel("电影名", fontproperties=my_font)
plt.ylabel("票房数据 单位(万)", fontproperties=my_font)
plt.title("2017年4月14日,15日,16日电影票房数据", fontproperties=my_font)

# 添加图例
plt.legend(prop=my_font)

# 添加网格
plt.grid(alpha=0.3)

# 展示
plt.show()
