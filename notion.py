# notion.py
import os
import requests

NOTION_API_KEY = os.getenv("NOTION_API_KEY", "").strip()
DATABASE_ID = os.getenv("NOTION_DATABASE_ID", "").strip()

if not NOTION_API_KEY or not DATABASE_ID:
    raise RuntimeError("请确保 NOTION_API_KEY 和 NOTION_DATABASE_ID 已设置为环境变量。")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def fetch_diary_dates():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    has_more = True
    next_cursor = None
    dates = set()

    while has_more:
        payload = {"page_size": 100}
        if next_cursor:
            payload["start_cursor"] = next_cursor

        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()

        for result in data.get("results", []):
            date_value = result.get("properties", {}).get("日期", {}).get("date", {})
            if date_value and "start" in date_value:
                dates.add(date_value["start"])

        has_more = data.get("has_more", False)
        next_cursor = data.get("next_cursor")

    return sorted(dates)
