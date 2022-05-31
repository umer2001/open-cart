import os
import requests
from exporters.base import BaseExporter
from models.shopify_multi_vendor.shopify_multi_vendor_order import ShopifyMultiVendorOrder
from models.shopify_multi_vendor.shopify_multi_vendor_product import ShopifyMultiVendorProduct


class ShopifyMultiVendorExporter(BaseExporter):
    def __init__(self):
        super().__init__()
        self.access_token = os.getenv('MVM_ACCESS_TOKEN')
        self.endpoint = os.getenv('MVM_ENDPOINT')
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }

    def create_product(self, product: ShopifyMultiVendorProduct):
        return requests.post(
            url=f"{self.endpoint}/api/v2/products.json",
            headers=self.headers,
            json=product.to_dict()
        ).json()

    def create_order(self, order: ShopifyMultiVendorOrder):
        return requests.post(
            url=f"{self.endpoint}/api/v2/orders/draft-orders.json",
            headers=self.headers,
            json=order.to_dict()
        ).json()
