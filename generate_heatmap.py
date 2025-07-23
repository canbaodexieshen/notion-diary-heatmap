from github_contributions_heatmap import Contributions

# 读取 dates.txt 中的所有日期
with open("dates.txt", "r", encoding="utf-8") as f:
    dates = [line.strip() for line in f if line.strip()]

# 创建热力图
c = Contributions()
for date in dates:
    c.add(date)

# 获取 HTML 内容
html = c.get_html(
    title="🌱 Notion 日记热力图",
    color="green"
)

# 写入 index.html 到根目录
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ 热力图已生成到 index.html")
