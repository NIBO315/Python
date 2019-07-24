"""
    由条形图转变为直方图
    例:从家里到上班地点所需的时间统计
"""
# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

# 输入数据
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]  # 家里到上班地点需要的时间
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]  # 组距
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.bar(range(12), quantity, width=1)

# 设置x轴刻度
_x = [i-0.5 for i in range(13)]
_xticks_label = interval+[150]
plt.xticks(_x, _xticks_label)

# 添加描述信息
plt.xlabel("时间段", fontproperties=my_font)
plt.ylabel("人数", fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.3)

# 展示
plt.show()
