import json
from os.path import isfile, join
from os import listdir
from exporters.shopify_multi_vendor import ShopifyMultiVendorExporter
from importer.opencart import OpencartImporter
from models.open_cart.openCartProduct import OpenCartProduct_from_dict
from models.shopify_multi_vendor.shopify_multi_vendor_product import mvm_product_from_dict


def migrate_products_from_open_cart_to_mvm(test_item_count=0):
    importer = OpencartImporter()
    products = importer.fetch_products(total_products=3280)

    # write products to  json file
    json.dump(products, open(
        "source/opencart/opencart_products.json", "w"))

    # read products from json file
    products = json.load(open(
        "source/opencart/opencart_products.json", "r"))

    open_cart_products = [
        OpenCartProduct_from_dict(
            product) for product in products
    ]

    # loop over products
    items_to_migrate_count = test_item_count if test_item_count > 0 else len(
        open_cart_products)
    shopify_mvm_products = [
        open_cart_products[index].to_shipify_multi_vendor_product() for index in range(items_to_migrate_count)]

    exporter = ShopifyMultiVendorExporter()

    failures = []
    successes: dict = {}
    try:
        for productIndex in range(0, len(shopify_mvm_products)):
            print(f"productIndex: {productIndex}")
            result = exporter.create_product(
                shopify_mvm_products[productIndex])
            if result.get("code", None):
                print(result)
                failures.append(shopify_mvm_products[productIndex].to_dict())
                json.dump(failures, open(
                    "output/failures/opencart_products_failures.json", "w"))
            else:
                if result["product"]["id"]:
                    successes[shopify_mvm_products[productIndex].product_name] = result["product"]
                    json.dump(successes, open(
                        "output/successes/opencart_products_successes.json", "w"))
            productIndex += 1
    except Exception as e:
        print(e)


def retry_failed_customers(path_to_failurs_file: str, test_item_count=0):
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
            result = json.loads(exporter.create_product(
                shopify_mvm_products[productIndex]))
            if result.get("code", None):
                print(result)
                failures.append(shopify_mvm_products[productIndex].to_dict())
                json.dump(failures, open(
                    "output/failures/opencart_products_failures.json", "w"))
            else:
                if result["product"]["id"]:
                    successes[shopify_mvm_products[productIndex]
                              .product_name] = result["product"]
                    json.dump(successes, open(
                        "output/successes/opencart_products_successes.json", "w"))
            productIndex += 1
    except Exception as e:
        print(e)


def main():
    print("Welcome to Product Migration Menu")
    print("1. Migrate Products from OpenCart to Shopify Multi Vendor Market place")
    print("2. Retry Failures")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        test_item_count = int(
            input("Enter the number of items to migrate (0 for all): "))
        migrate_products_from_open_cart_to_mvm(
            test_item_count=test_item_count)
    elif choice == 2:
        print("Retry Failures")
        print("Enter s.no of the file to retry: ")
        # list all files in /output/failures
        path_to_failures_file = "output/failures/"
        onlyfiles = [f for f in listdir(path_to_failures_file) if isfile(
            join(path_to_failures_file, f))]

        for fileIndex in range(len(onlyfiles)):
            print(
                f"{fileIndex + 1}: {path_to_failures_file}{onlyfiles[fileIndex]}")
        choice = int(input("Enter your choice: "))
        test_item_count = int(
            input("Enter the number of items to migrate (0 for all): "))
        retry_failed_customers(
            f"{path_to_failures_file}{onlyfiles[choice - 1]}", test_item_count)


# Call Main
main()
