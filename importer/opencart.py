import os
from importer.default import DefaultImporter
import requests
from dotenv import load_dotenv

load_dotenv()


class OpencartImporter(DefaultImporter):
    def __init__(self):
        super().__init__()
        self.name = 'opencart'
        self.url = os.getenv('OPEN_CART_URL')
        self.api_key = os.getenv('OPEN_CART_ADMIN_API_KEY')

    def authentication(self):
        pass

    def write_to_json(self):
        pass

    def fetch_categories(self):
        return requests.get(f"{self.url}/index.php?route=rest/category_admin/category",
                            headers={
                                'X-Oc-Restadmin-Id': self.api_key
                            }
                            ).json().get('data')

    def fetch_products(self, total_products, limit_per_page=20):
        page = 1
        go_till = total_products/limit_per_page+1
        products = []
        while page <= go_till:
            print(f"Fetching products page {page}")
            products.extend(requests.get(f"{self.url}/index.php?route=rest/product_admin/products&limit={limit_per_page}&page={page}",
                            headers={
                                'X-Oc-Restadmin-Id': self.api_key
                            }
            ).json().get('data'))
            page += 1
        return products

    def fetch_orders(self):
        return requests.get(f"{self.url}/index.php?route=rest/order_admin/orders",
                            headers={
                                'X-Oc-Restadmin-Id': self.api_key
                            }
                            ).json().get('data')

    def fetch_order_detail_by_id(self, order_id):
        return requests.get(f"{self.url}/index.php?route=rest/order_admin/orders&id={order_id}",
                            headers={
                                'X-Oc-Restadmin-Id': self.api_key
                            }
                            ).json().get('data')

    def fetch_customers(self, total_customers, limit_per_page=100):
        page = 1
        go_till = total_customers/limit_per_page+1
        customers = []
        while page <= go_till:
            print(f"Fetching customers page {page}")
            customers.extend(requests.get(f"{self.url}/index.php?route=rest/customer_admin/customers&limit={limit_per_page}&page={page}",
                                          headers={
                                              'X-Oc-Restadmin-Id': self.api_key
                                          }
                                          ).json().get('data'))
            page += 1
        return customers
