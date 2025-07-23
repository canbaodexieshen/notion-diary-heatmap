import json
from notion import fetch_diary_dates

def generate_heatmap_data():
    dates = fetch_diary_dates()
    data = {date: 1 for date in dates}
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    generate_heatmap_data()
