import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from collections import Counter

# 读取 Notion 中抓取的日期数据
with open("dates.json", "r") as f:
    dates = json.load(f)

# 统计每一天的写作频次
date_counts = Counter(dates)

# 构建从当年 1 月 1 日至今天的日期序列
start = datetime.date.today().replace(month=1, day=1)
end = datetime.date.today()
days = (end - start).days + 1
date_list = [start + datetime.timedelta(days=i) for i in range(days)]

# 转换为频次值，写过日记的记为 1，没写的为 0
values = [date_counts.get(d.strftime("%Y-%m-%d"), 0) for d in date_list]

# 生成图表
fig, ax = plt.subplots(figsize=(12, 2))
ax.bar(date_list, values, width=1.0, color="#39d353")  # GitHub绿色
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
ax.set_yticks([])
ax.set_xlim(start, end)
ax.set_title("Notion 日记热力图", fontsize=14)

plt.tight_layout()
plt.savefig("heatmap.svg", format="svg")
