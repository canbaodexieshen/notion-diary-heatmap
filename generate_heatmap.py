import os
from github_contributions_heatmap import Contributions

# 获取 Notion 同步后的 GitHub 账号数据（或手动创建 Contribution 对象）
# 示例数据：你需要替换成你同步后的实际数据逻辑
dates = [
    "2024-01-01", "2024-01-02", "2024-01-04", "2024-01-06", "2024-01-09",
    "2024-01-15", "2024-01-20", "2024-01-25", "2024-02-01", "2024-02-05",
]

c = Contributions()
for date in dates:
    c.add(date)

# 生成 HTML 内容
html = c.get_html(
    title="🌱 Notion 日记热力图",
    color="green",  # GitHub 风格绿色
)

# 确保 output 目录存在
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# 写入 HTML 文件到 output/index.html
with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("✅ 热力图已生成到 output/index.html")
