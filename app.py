import requests
from bs4 import BeautifulSoup as bs

BASE_URL = 'https://store.google.com/us'
URL = 'https://store.google.com/us/?hl=en-US'

product_urls = []
product_names = []
product_status = []

# Scrape product URLs
def get_product_urls():
    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')

    for link in soup.find_all('a'):
        try:
            if '/product' in link.get('href'):
                product_urls.append(link.get('href'))
                # print(link.get('href'))
        except:
            pass


# Scrape product pages
def get_product_info():
    for product in product_urls:
        # print(f'{BASE_URL}{product}')
        req = requests.get(f'{BASE_URL}{product}')
        soup = bs(req.text, 'html.parser')
        for name in soup.find_all('h1'):
            product_names.append(name.text)

        cta_btns = soup.find('button', {'class' :"transaction"})
        if cta_btns is not None:
            for cta in cta_btns:
                product_status.append(cta)


# Run
get_product_urls()
get_product_info()