import os
import requests
import yaml
from datetime import datetime, timezone

SCHOLAR_ID = "TT9m3j0AAAAJ"
API_KEY = os.environ["SERPAPI_KEY"]

url = "https://serpapi.com/search.json"

params = {
    "engine": "google_scholar_author",
    "author_id": SCHOLAR_ID,
    "api_key": API_KEY,
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data_json = response.json()
cited_by = data_json.get("cited_by", {}).get("table", [])

citations = cited_by[0]["citations"]["all"] if len(cited_by) > 0 else 0
h_index = cited_by[1]["h_index"]["all"] if len(cited_by) > 1 else 0
i10_index = cited_by[2]["i10_index"]["all"] if len(cited_by) > 2 else 0

data = {
    "citations": citations,
    "h_index": h_index,
    "i10_index": i10_index,
    "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
}

with open("_data/scholar.yml", "w") as f:
    yaml.dump(data, f, sort_keys=False)
