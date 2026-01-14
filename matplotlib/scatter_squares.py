import matplotlib.pyplot as plt

# 需要加载font_manager模块
from matplotlib import font_manager


# 设置字体,可以设置多个字体
font1 = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf", size=14)
font2 = font_manager.FontProperties(fname="C:\Windows\Fonts\simfang.ttf", size=24)
# 解决负号显示问题
plt.rcParams["axes.unicode_minus"] = False

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.set_title("平方数", fontproperties=font1, fontsize=24)
ax.set_xlabel("值", fontproperties=font2, fontsize=14)
ax.set_ylabel("值的平方", fontproperties=font2, fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

# 显示plot
plt.show()

# 保存图片
# plt.savefig("squares_plot.png", bbox_inches="tight")
