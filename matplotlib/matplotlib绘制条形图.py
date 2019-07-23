"""
    条形图:绘制离散的数据,能够一眼看出各个数据的大小,比较数据之间的差别
    例:2017年内地电影票房前10的电影和电影票房数据
"""
# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

# 输入数据,x-电影名,y-票房数据
x = ["战狼", "速度与激情", "羞羞的铁拳", "功夫瑜伽", "西游伏妖篇",
     "变形金刚5\n最后的骑士", "摔跤吧！爸爸", "芳华", "加勒比海盗\n死无对证", "金刚：骷髅岛"]
y = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 添加描述信息
plt.xlabel("电影名", fontproperties=my_font)
plt.ylabel("票房数据 单位(亿)", fontproperties=my_font)
plt.title("2017年内地电影票房前10的电影和电影票房数据", fontproperties=my_font)

# 用bar方法绘制竖形条形图
plt.bar(range(len(x)), y, width=0.5)

# 调整x轴间距,显示中文并旋转方向
plt.xticks(range(len(x)), x, fontproperties=my_font, rotation=45)

# 显示
plt.show()
