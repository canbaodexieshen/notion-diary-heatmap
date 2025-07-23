import requests
import os
import datetime

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

def get_diary_dates():
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {
        "page_size": 100
    }

    res = requests.post(url, headers=headers, json=payload)
    data = res.json()

    dates = []
    for result in data["results"]:
        props = result["properties"]
        if "日期" in props and props["日期"]["date"]:
            date_str = props["日期"]["date"]["start"]
            dates.append(date_str)

    return dates

if __name__ == "__main__":
    print(get_diary_dates())
