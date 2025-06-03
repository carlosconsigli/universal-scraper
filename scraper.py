import requests
from bs4 import BeautifulSoup
import re
import spacy

nlp = spacy.load("en_core_web_sm")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def extract_price(text):
    match = re.search(r'(\$|USD|€)\s?\d[\d.,]*', text)
    return match.group(0) if match else None

def extract_stock_info(text):
    keywords = ["en stock", "in stock", "disponible", "available", "out of stock", "agotado", "sin stock"]
    for word in keywords:
        if word.lower() in text.lower():
            return word
    return "Sin información"

def get_product_blocks(soup):
    tags = soup.find_all(["div", "li", "article"])
    candidates = []
    for tag in tags:
        text = clean_text(tag.get_text())
        if len(text) > 30 and len(text) < 1000:
            candidates.append(tag)
    return candidates

def analyze_block(block, query):
    text = clean_text(block.get_text())

    if query.lower() not in text.lower():
        return None

    price = extract_price(text)
    stock = extract_stock_info(text)

    # Heurística para nombre (línea principal sin precio ni stock)
    name_lines = [line for line in text.split('\n') if query.lower() in line.lower()]
    name = name_lines[0] if name_lines else "Nombre no encontrado"

    return {
        "name": name,
        "price": price or "Precio no encontrado",
        "stock": stock,
    }

def scrape_products(url, query):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        blocks = get_product_blocks(soup)
        found = []

        for block in blocks:
            product = analyze_block(block, query)
            if product:
                found.append(product)

        if not found:
            return {
                "success": True,
                "products": [],
                "message": "No se encontraron productos coincidentes en esta página."
            }

        return {
            "success": True,
            "products": found,
            "message": f"Se encontraron {len(found)} productos coincidentes."
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
