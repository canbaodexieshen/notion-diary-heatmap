import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from collections import Counter

# 读取 Notion 抓到的日期列表
with open("dates.json", "r") as f:
    dates = json.load(f)

# 统计每一天是否写过日记（值设为1）
date_counts = Counter(dates)
start = datetime.date.today().replace(month=1, day=1)
end = datetime.date.today()

# 构建时间序列数据
days = (end - start).days + 1
date_list = [start + datetime.timedelta(days=i) for i in range(days)]
values = [date_counts.get(d.strftime("%Y-%m-%d"), 0) for d in date_list]

# 绘图
fig, ax = plt.subplots(figsize=(12, 2))
ax.bar(date_list, values, width=1.0, color="#39d353")  # GitHub绿
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
ax.set_yticks([])
ax.set_xlim(start, end)
ax.set_title("Notion 日记热力图", fontsize=14)

plt.tight_layout()
plt.savefig("heatmap.svg", format="svg")
