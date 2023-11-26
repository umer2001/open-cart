import json
import time
from os.path import isfile, join
from os import listdir
from shopify import Metafield, Product
from exporters.shopify import ShopifyExporter
from updaters.shopify_multi_vendor import ShopifyMultiVendorUpdater
from importer.opencart import OpencartImporter
from importer.shopify_multi_vendor import ShopifyMultiVendorImporter
from models.shopify_multi_vendor.shopify_multi_vendor_product import mvm_product_from_dict, MvmProductCommission, ShopifyMultiVendorProduct
from models.shopify_multi_vendor.shopify_multi_vendor_product import mvm_product_from_dict


def retry_failed_products(path_to_failurs_file: str, test_item_count=0):
    failures = json.load(open(path_to_failurs_file, "r"))
    shopify_mvm_products = [
        mvm_product_from_dict(failure) for failure in failures
    ]

    # push to shopify Multi Vendor
    exporter = ShopifyMultiVendorExporter()

    failures = []
    successes: dict = {}

    items_to_migrate_count = test_item_count if test_item_count > 0 else len(
        shopify_mvm_products)

    try:
        for productIndex in range(0, items_to_migrate_count):
            print(f"productIndex: {productIndex}")
            result = exporter.create_product(
                shopify_mvm_products[productIndex])
            if result.get("code", None):
                print(result)
                failures.append(shopify_mvm_products[productIndex].to_dict())
                json.dump(failures, open(
                    "output/failures/products/opencart_products_failures.json", "w"))
            else:
                if result["product"]["id"]:
                    successes[shopify_mvm_products[productIndex]
                              .product_name] = result["product"]
                    json.dump(successes, open(
                        "output/successes/products/opencart_products_successes.json", "w"))
            productIndex += 1
    except Exception as e:
        print(e)


def fetch_all_products_from_shopify_multi_vendor(product_count=0):
    importer = ShopifyMultiVendorImporter()
    products = importer.fetch_products(total_products=product_count)
    # write to json file
    json.dump(products, open(
        "source/shopify_multi_vendor/products/shopify_multi_vendor_products.json", "w"))


def update_products(test_item_count=0):
    updater = ShopifyMultiVendorUpdater()
    # read shopify product IDs
    products_ids = json.load(open(
        "source/shopify_multi_vendor/products/shopify_multi_vendor_products.json", "r"))
    # loop over products
    items_to_update_count = test_item_count if test_item_count > 0 else len(
        products_ids)

    failures = []
    successes = []
    for productIndex in range(0, items_to_update_count):
        try:
            product = mvm_product_from_dict(products_ids[productIndex])
            print(f"productIndex: {productIndex}")
            print("product id:", product.id)
            product_price = float(product.price)
            # update logic
            commission_value = None
            if product_price > 250:
                commission_value = "1"
            elif product_price > 75:
                commission_value = "3"
            elif product_price > 30:
                commission_value = "4"
            else:
                commission_value = "5"

            print("commission_value:", commission_value)

            commission = MvmProductCommission(
                commission_type="%",
                value=commission_value,
                sp_id_product=product.id,
                shopify_product_id=product.shopify_product_id
            )

            result = updater.update_product_commissions(product, commission)
            if result.get("product_commission").get("sp_id_product"):
                successes.append(products_ids[productIndex])
                json.dump(successes, open(
                    "output/successes/products/shopify_product_update_successes.json", "w"))
            else:
                failures.append(products_ids[productIndex])
                json.dump(failures, open(
                    "output/failures/products/shopify_product_update_failures.json", "w"))
            productIndex += 1
            # sleep for 30 seconds because of shopify api rate limit
            time.sleep(1)
        except Exception as e:
            print(e)
            print(type(e))    # the exception instance
            print(e.args)


def update_all_products_on_mvm(test_item_count=0):
    fetch_all_products_from_shopify_multi_vendor(product_count=test_item_count)
    update_products(test_item_count=test_item_count)


def main():
    print("Welcome to Product Update Menu")
    print("1. Update Products on Shopify Multi Vendor Market place")
    print("2. Retry Failures")
    print("3. Fetch all products from Shopify Multi Vendor Market place")
    print("4. Update products")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        test_item_count = int(
            input("Enter the number of items to migrate (0 for all): "))
        update_all_products_on_mvm(
            test_item_count=test_item_count)
    elif choice == 2:
        print("Retry Failures")
        print("Enter s.no of the file to retry: ")
        # list all files in /output/failures
        path_to_failures_file = "output/failures/products/"
        onlyfiles = [f for f in listdir(path_to_failures_file) if isfile(
            join(path_to_failures_file, f))]

        for fileIndex in range(len(onlyfiles)):
            print(
                f"{fileIndex + 1}: {path_to_failures_file}{onlyfiles[fileIndex]}")
        choice = int(input("Enter your choice: "))
        test_item_count = int(
            input("Enter the number of items to update (0 for all): "))
        retry_failed_products(
            f"{path_to_failures_file}{onlyfiles[choice - 1]}", test_item_count)
    elif choice == 3:
        test_item_count = int(
            input("Enter the number of items to fetch (more then 250) : "))
        fetch_all_products_from_shopify_multi_vendor(
            product_count=test_item_count)
    elif choice == 4:
        print("Update products")
        test_item_count = int(
            input("Enter the number of items to update (0 for all): "))
        update_products(test_item_count)


# Call Main
main()
