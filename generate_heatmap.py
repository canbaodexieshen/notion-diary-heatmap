import json
from notion import fetch_diary_dates

def generate_heatmap_data():
    dates = fetch_diary_dates()
    data = {}

    for date in dates:
        data[date] = data.get(date, 0) + 1  # 每天记录1次

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    generate_heatmap_data()
