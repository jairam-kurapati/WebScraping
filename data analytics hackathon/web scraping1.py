import requests
import pandas as pd
import time
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

base_url = "https://www.flipkart.com/search?q=mobiles+under+50000"

products = []

# STEP 1: Get product URLs
r = requests.get(base_url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")

product_links = set()

for a in soup.find_all("a", href=True):
    if "/p/" in a["href"]:
        product_links.add("https://www.flipkart.com" + a["href"].split("?")[0])

product_links = list(product_links)[:20]  # limit for safety

# STEP 2: Visit each product page
for link in product_links:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    try:
        name = soup.find("span", class_="VU-ZEz").text
    except:
        name = None

    try:
        brand = name.split()[0]
    except:
        brand = None

    try:
        price = soup.find("div", class_="Nx9bqj CxhGGd").text
    except:
        price = None

    try:
        mrp = soup.find("div", class_="yRaY8j A6+E6v").text
    except:
        mrp = None

    try:
        rating = soup.find("div", class_="_3LWZlK").text
    except:
        rating = None

    try:
        reviews = soup.find("span", class_="Wphh3N").text
    except:
        reviews = None

    try:
        availability = soup.find("div", class_="_16FRp0").text
    except:
        availability = "Available"

    try:
        delivery = soup.find("div", class_="_8vKfqZ").text
    except:
        delivery = None

    products.append([
        name, brand, price, mrp, rating, reviews, availability, delivery
    ])

    time.sleep(2)

# STEP 3: Create DataFrame
df = pd.DataFrame(products, columns=[
    "Product_Name", "Brand", "Selling_Price", "MRP",
    "Rating", "Review_Count", "Availability", "Delivery"
])

# STEP 4: Save CSV
df.to_csv("flipkart_complete_dataset.csv", index=False)

print("Dataset created successfully!")
