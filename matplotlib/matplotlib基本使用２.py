"""
matplotlib使用的基本要点：
    1.导入
    2.绘图
    3.显示
    4.设置图片大小
    5.保存本地
    6.调整x轴或y轴的刻度
    7.添加x轴y轴的描述信息
    8.设置线条的样式
    9.标记特殊点
    10.给图片添加水印
    11.设置轴的中文字体
    12.绘制网格
    13.增加图例
"""
# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

y_1 = [1, 0, 2, 0, 0, 3, 0, 2, 0, 2, 3, 0, 4, 0, 5]
y_2 = [2, 2, 0, 1, 3, 4, 0, 4, 0, 1, 0, 0, 0, 0, 0]
x = range(11, 26)

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 设置中文字体
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

# 设置坐标轴间距及字体
_x_labels = ["{}岁".format(i) for i in x]

plt.xticks(x, _x_labels, fontproperties=my_font)

# 设置坐标标题及主题
plt.xlabel("年龄", fontproperties=my_font)
plt.ylabel("交友个数 单位(个)", fontproperties=my_font)
plt.title("11岁到25岁的交友情况", fontproperties=my_font)

# 绘制网格,alpha-设置网格的透明度,设置网格的线条格式
plt.grid(alpha=0.4, linestyle='-.')

# 绘图
# color-设置线条颜色,　linestyle-设置线条样式
plt.plot(x, y_1, label="自己", color="orange", linestyle=':')
plt.plot(x, y_2, label="好友", color="cyan", linestyle='-.')

# 添加图例
plt.legend(prop=my_font)

# 保存图片
plt.savefig("./sig_size.png")
# 显示图像
plt.show()
