import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# ---------- Configuration ----------
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile Safari/605.1.15"
]

BASE_URL = "https://www.amazon.in/s?k=soft+toys"
HEADERS = lambda: {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com/"
}


# ---------- Helpers ----------
def get_soup(url):
    try:
        response = requests.get(url, headers=HEADERS(), timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"[!] Error loading page: {e}")
        return None

def extract_price(product):
    whole = product.select_one(".a-price-whole")
    frac = product.select_one(".a-price-fraction")
    if whole:
        return f"{whole.text.strip()}.{frac.text.strip()}" if frac else whole.text.strip()
    return None

def extract_brand(product, title):
    # Try specific brand selectors first
    brand_tag = product.select_one('span.a-size-base-plus')
    if brand_tag:
        brand = brand_tag.text.strip()
        if brand:
            return brand
    # Fallback: assume brand is first word of title
    return title.split()[0] if title else "Unknown"

# ---------- Main Scraper ----------
def scrape_sponsored_products(soup):
    items = []
    results = soup.select("[data-component-type='s-search-result']")
    for item in results:
        try:
            # TEMP: Remove sponsored filter to get all products
            # if "Sponsored" not in item.get_text():
            #     continue

            title_tag = item.h5
            title = title_tag.text.strip() if title_tag else "N/A"

            brand = extract_brand(item, title)

            rating_tag = item.select_one('[aria-label$=" out of 5 stars"]')
            rating = rating_tag['aria-label'].split()[0] if rating_tag else None

            reviews_tag = item.select_one('[aria-label$=" ratings"]')
            reviews = reviews_tag['aria-label'].split()[0].replace(',', '') if reviews_tag else "0"

            price = extract_price(item)

            img_url = item.img['src'] if item.img else None
            link_tag = item.h2.a if item.h2 and item.h2.a else None
            prod_url = "https://www.amazon.in" + link_tag['href'] if link_tag and 'href' in link_tag.attrs else None

            items.append({
                "Title": title,
                "Brand": brand,
                "Rating": rating,
                "Reviews": reviews,
                "Price": price,
                "Image URL": img_url,
                "Product URL": prod_url
            })

            time.sleep(random.uniform(0.5, 1.5))  # Human-like delay

        except Exception:
            continue

    return items

# ---------- Execution ----------
if __name__ == "__main__":
    print("[*] Starting scrape for: soft toys (sponsored only)")
    soup = get_soup(BASE_URL)

    if not soup:
        print("🚫 Could not retrieve page. Aborting.")
        exit()

    data = scrape_sponsored_products(soup)
    df = pd.DataFrame(data)

    # Deduplicate and save
    df.drop_duplicates(subset=["Title", "Product URL"], inplace=True)
    df.to_excel("soft_toys_sponsored.xlsx", index=False)
    df.to_csv("soft_toys_sponsored.csv", index=False)

    print(f"✅ Scrape complete. {len(df)} sponsored products saved.")
    print("📁 Files created:")
    print("   - soft_toys_sponsored.xlsx")
    print("   - soft_toys_sponsored.csv")
