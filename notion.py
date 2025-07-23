import requests

NOTION_API_KEY = "你的 Notion Integration Token"
DATABASE_ID = "你的数据库 ID"

headers = {
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
        payload = {
            "page_size": 100
        }
        if next_cursor:
            payload["start_cursor"] = next_cursor

        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        for result in data.get("results", []):
            properties = result.get("properties", {})
            date_field = properties.get("日期", {})
            date_value = date_field.get("date", {})
            if "start" in date_value:
                dates.add(date_value["start"])

        has_more = data.get("has_more", False)
        next_cursor = data.get("next_cursor", None)

    return sorted(dates)
