#import total
import requests
import time
import random
import re
import json
#import from
from time import sleep
from random import choice
from bs4 import BeautifulSoup


def FetchHTML(url):
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

def ScrapeRetailer(retailer, url):
    html = FetchHTML(url)
    if html:
        try:
            match retailer:
                case "amazon":
                    title, price = ExtractAmazonData(html)
                case "walmart":
                    title, price = ExtractWalmartData(html)
                case "target":
                    title, price = ExtractTargetData(html)
                case "costco":
                    title, price = ExtractCostcoData(html)
                case "homedepot":
                    title, price = ExtractHomedepotData(html)
#                case "walmart":
#                    title, price = ExtractWalmartData(html)
                case _:
                    print(f"Retailer {retailer} not supported")
                    return None, None # Return None values
            time.sleep(2)
            return title, price
        except Exception as e:
            print(f"An unexpected error occurred during scraping: {e}")
            return None, None
    else:
        return None, None # Return None values if HTML fetch fails
    










def ExtractAmazonData(html):
    soup = BeautifulSoup(html, "html.parser")
    title_element = soup.find("span", id="productTitle")
    title = title_element.text.strip() if title_element else "Title not found"
    price_element = soup.find("span", class_="a-offscreen")
    price = price_element.text.strip() if price_element else "Price not found"
    return (title, price)

def ExtractWalmartData(html):
    soup = BeautifulSoup(html, "html.parser")
    title_element = soup.find("meta", property="og:title")
    title = title_element['content'].strip() if title_element else "Title not found"
    price_element = soup.find("span", itemprop="price")
    price_text = price_element.text.strip() if price_element else "Price not found"
    if price_text != "Price not found":
        cleaned_price = re.sub(r"[^\d.]", "", price_text)
        if cleaned_price:
            price = cleaned_price
        else:
            price = "Price not found"
    else:
        price = "Price not found"
    return (title, price)

def ExtractTargetData(html):#Issue with Price Scraping
    soup = BeautifulSoup(html, "html.parser")
    title_element = soup.find("meta", property="og:title")
    title = title_element['content'].strip() if title_element else "Title not found"
    price_element = soup.find("span", datatest="product-price")
    price_text = price_element.text.strip() if price_element else "Price not found"
    if price_text != "Price not found":
        cleaned_price = re.sub(r"[^\d.]", "", price_text)
        if cleaned_price:
            price = cleaned_price
        else:
            price = "Price not found"
    else:
        price = "Price not found"
    return (title, price)

def ExtractCostcoData(html):#Issue with Price Scrapingp
    soup = BeautifulSoup(html, "html.parser")
    title = "Title not found"
    price = "Price not found"

    script_tag = soup.find("script", string=lambda text: "window.digitalData" in text if text else False)
    if script_tag:
        script_content = script_tag.string
        if script_content:
            try:
                json_string = script_content.split("window.digitalData = ")[1].split("window.digitalDataEvents")[0].strip().rstrip(';')

                # Replace single quotes with double quotes for valid JSON
                json_string = re.sub(r"(\w+)\s*:", r'"\1":', json_string) #This is the important part
                data = json.loads(json_string)
                if data and "product" in data and "name" in data["product"]:
                    title = data["product"]["name"]
                if data and "product" in data and "priceMax" in data["product"]:
                    price_text = data["product"]["priceMax"]
                    cleaned_price = re.sub(r"[^\d.]", "", price_text)
                    if cleaned_price:
                        price = cleaned_price
            except (IndexError, json.JSONDecodeError, KeyError,TypeError) as e:
                print(f"Error parsing JSON: {e}")
                pass
    return (title, price)

def ExtractHomedepotData(html):#Issue with everything
    soup = BeautifulSoup(html, "html.parser")
    title_element = soup.find("meta", property="og:title")
    title = title_element['content'].strip() if title_element else "Title not found"
