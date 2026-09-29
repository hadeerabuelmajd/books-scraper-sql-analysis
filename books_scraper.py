import requests
from bs4 import BeautifulSoup
import csv

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

BASE_URL = "http://books.toscrape.com/"


def extract_book_data(book):
    #title
    title = book.find("h3").find("a")["title"]

    #Price
    price_text = book.find("p", class_="price_color").text
    price = float(price_text.replace("£", "").strip())

    #rating
    rating_class = book.find("p", class_="star-rating")["class"][1]
    rating = RATING_MAP.get(rating_class, 0)

    #stok
    stock_text = book.find("p", class_="instock availability").text.strip()
    in_stock = "In stock" in stock_text
    
    #url
    relative_url = book.find("h3").find("a")["href"]
    clean_url = relative_url.replace("../", "")
    full_url = BASE_URL + "catalogue/" + clean_url if not clean_url.startswith("catalogue/") else BASE_URL + clean_url

    
    return {
        "title": title,
        "price": price,
        "rating": rating,
        "in_stock": in_stock,
        "url": full_url
    }


all_books = []

for page_num in range(1, 6):
    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        book_data = extract_book_data(book)
        all_books.append(book_data)

print(f"Successfully collected {len(all_books)} books")

#headers
keys = ["title", "price", "rating", "in_stock", "url"]

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    dict_writer = csv.DictWriter(file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_books)

print("file created successfully")
