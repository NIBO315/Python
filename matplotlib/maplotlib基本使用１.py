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

from matplotlib import pyplot as plt
import random
from matplotlib import font_manager
# import matplotlib

# linux和windows设置字体的方式
# font = {'family': 'monospace',
#         'weight': 'bold',
#         'size': 'larger'}

# matplotlib.rc("front", **font)

# 另外一种设置字体的方式
# /usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc - 通过在终端输入fic-list :lang=zh查找中文路径
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

# 输入x轴和y轴的信息
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 调整X轴刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
# 取步长,数字和字符串一一对应,数据的长度一样
# rotation-旋转的度数
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位('C)", fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况", fontproperties=my_font)

# 绘图
plt.plot(x, y)

# 展示图形
plt.show()

# 保存本地
plt.savefig("./sig_size.png")
