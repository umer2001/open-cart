import os
from importer.default import DefaultImporter
import requests
from dotenv import load_dotenv

load_dotenv()


class ShopifyMultiVendorImporter(DefaultImporter):
    def __init__(self):
        super().__init__()
        self.name = 'shopify_mvm'
        self.url = os.getenv('MVM_ENDPOINT', "https://mvmapi.webkul.com")
        self.api_key = os.getenv('MVM_ACCESS_TOKEN')

    def fetch_products(self, total_products, limit_per_page=250):
        page = 1
        go_till = total_products/limit_per_page+1
        products = []
        while page <= go_till:
            print(f"Fetching products page {page}")
            products.extend(requests.get(f"{self.url}/api/v2/products.json?limit={limit_per_page}&page={page}",
                            headers={
                                'Authorization': f'Bearer {self.api_key}',
                                'Content-Type': 'application/json'
                            }
            ).json().get('products'))
            page += 1
        return products
