import requests
from bs4 import BeautifulSoup
import time
import re

def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def extract_amazon_data(html):
    soup = BeautifulSoup(html, "html.parser")
    title_element = soup.find("span", id="productTitle")
    title = title_element.text.strip() if title_element else "Title not found"
    price_element = soup.find("span", class_="a-offscreen")
    price = price_element.text.strip() if price_element else "Price not found"
    return {"title": title, "price": price}


def extract_other_retailer_data(html): # Example for another retailer
    soup = BeautifulSoup(html, "html.parser")
    # Replace these selectors with the actual selectors for the other retailer
    title_element = soup.find("h1", class_="product-name") # Example selector
    title = title_element.text.strip() if title_element else "Title not found"
    price_element = soup.find("div", class_="price") # Example selector
    price = price_element.text.strip() if price_element else "Price not found"

    # Example of extracting multiple prices if available
    prices = soup.find_all("span", class_=re.compile(r"price"))
    all_prices = [p.text.strip() for p in prices]

    return {"title": title, "price": price, "all_prices": all_prices}

def main():
    urls = {
        "amazon": "https://www.amazon.com/SUPERONE-Upgrade-Removable-Kickstand-Accessories/dp/B0CN2Q2RDW/?_encoding=UTF8&pd_rd_w=BLwzY&content-id=amzn1.sym.a602a706-e4fe-481e-98c3-9b75060fd322%3Aamzn1.symc.abfa8731-fff2-4177-9d31-bf48857c2263&pf_rd_p=a602a706-e4fe-481e-98c3-9b75060fd322&pf_rd_r=9YVF9763W74BX7AFS3PT&pd_rd_wg=QxbNu&pd_rd_r=590fcd38-6b53-418f-9bc6-f66140d41cbb&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d&th=1",
    }

    for retailer, url in urls.items():
        print(f"Scraping {retailer}: {url}")
        html = fetch_html(url)
        if html:
            if retailer == "amazon":
                data = extract_amazon_data(html)
            else:
                data = None
                print("Retailer not supported")

            if data:
                print(data)
        time.sleep(2)

main()