import csv
from datetime import datetime

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# 需要加载font_manager模块
from matplotlib import font_manager


# 设置字体,可以设置多个字体
font1 = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf", size=14)
font2 = font_manager.FontProperties(fname="C:\Windows\Fonts\simfang.ttf", size=24)
# 解决负号显示问题
plt.rcParams["axes.unicode_minus"] = False


filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:

        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])

        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plt.style.use("seaborn-v0_8")
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# 设置图形的格式
ax.set_title(
    "2018年每日最高气温\n 美国加利福尼亚死亡谷", fontproperties=font2, fontsize=20
)
ax.set_xlabel("日期", fontproperties=font2, fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("温度 (F)", fontproperties=font2, fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()
