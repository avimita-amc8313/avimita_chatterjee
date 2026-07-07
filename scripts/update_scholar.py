from scholarly import scholarly
import yaml

SCHOLAR_ID = "TT9m3j0AAAAJ"

author = scholarly.search_author_id(SCHOLAR_ID)
author = scholarly.fill(author, sections=["indices"])

data = {
    "citations": author.get("citedby", 0),
    "h_index": author.get("hindex", 0),
    "i10_index": author.get("i10index", 0),
}

with open("_data/scholar.yml", "w") as f:
    yaml.dump(data, f, sort_keys=False)
