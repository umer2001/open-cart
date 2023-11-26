import os
import json
import requests
from models.shopify_multi_vendor.shopify_multi_vendor_order import ShopifyMultiVendorOrder
from models.shopify_multi_vendor.shopify_multi_vendor_product import ShopifyMultiVendorProduct, MvmProductCommission


class ShopifyMultiVendorUpdater:
    def __init__(self):
        super().__init__()
        self.access_token = os.getenv('MVM_ACCESS_TOKEN')
        self.endpoint = os.getenv('MVM_ENDPOINT')
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }

    def update_product_commissions(self, product: ShopifyMultiVendorProduct, commission: MvmProductCommission):
        return requests.put(
            url=f"{self.endpoint}/api/v2/products/{product.id}/commission.json",
            headers=self.headers,
            json={
                "commission_type": commission.commission_type,
                "value": commission.value
            }
        ).json()
