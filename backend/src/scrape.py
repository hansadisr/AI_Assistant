import requests
from bs4 import BeautifulSoup
import json
import time
import sys, os

sys.path.append(os.path.dirname(__file__))
from config import RAW_DATA_PATH

PAGES = [
    "https://moderta.com/",
    "https://moderta.com/services/",
    "https://moderta.com/software-by-moderta/",
    "https://moderta.com/sustainability-education/",
    "https://moderta.com/blog/",
    "https://moderta.com/careers/",
]

def scrape_page(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.content, "html.parser")

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    lines = [line for line in text.split("\n") if len(line) > 3]
    return "\n".join(lines)

if __name__ == "__main__":
    documents = []
    for url in PAGES:
        print(f"Scraping {url} ...")
        content = scrape_page(url)
        documents.append({"url": url, "content": content})
        time.sleep(1)

    with open(RAW_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Done! Scraped {len(documents)} pages.")
    print(f"Saved to {RAW_DATA_PATH}")