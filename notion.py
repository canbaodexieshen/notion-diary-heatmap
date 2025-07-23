import os, requests, json

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

def get_diary_dates():
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    all_dates = []
    next_cursor = None

    while True:
        payload = {"page_size": 100}
        if next_cursor:
            payload["start_cursor"] = next_cursor

        res = requests.post(url, headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()

        for r in data["results"]:
            d = r["properties"]["日期"]["date"]
            if d and d.get("start"):
                all_dates.append(d["start"])

        if not data.get("has_more"):
            break
        next_cursor = data.get("next_cursor")
    return all_dates

if __name__ == "__main__":
    dates = get_diary_dates()
    print(json.dumps(dates))
