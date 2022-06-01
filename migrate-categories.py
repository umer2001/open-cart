import json
import os
from exporters.shopify import ShopifyExporter
from importer.opencart import OpencartImporter
from models.open_cart.open_cart_category import OpenCartCategory
from models.shopify.shopify_collection import shopify_collection_to_dict
from utils import download_file


def migrate_categories_from_open_cart_to_shopify(test_item_count=0):
    importer = OpencartImporter()
    categories = importer.fetch_categories()

    open_cart_categories = [OpenCartCategory.from_dict(
        category) for category in categories]

    # loop over categories
    items_to_migrate_count = test_item_count if test_item_count > 0 else len(
        open_cart_categories)
    arr = [shopify_collection_to_dict(
        open_cart_categories[index].to_shopify_collection()) for index in range(items_to_migrate_count)]

    # write to JSONL file
    file_path = "tmp/shopify_collections.jsonl"

    if os.path.exists(file_path):
        os.remove(file_path)

    for category in arr:
        json.dump({"input": category}, open(
            file_path, "a"))
        open(file_path, "a").write("\n")

    # exporting to Shopify
    exporter = ShopifyExporter()
    exporter.authentication()

    print(exporter.bulk_export_collections(
        file_name="shopify_collections", file_path=file_path)
    )


def fetch_bulk_qery_status(id):
    exporter = ShopifyExporter()
    exporter.authentication()
    result = json.loads(exporter.bulk_mutation_status(id))
    print(result)
    if result["data"]["node"]["url"] != None:
        download_file(result["data"]["node"]["url"],
                      "output/shopify_collections.jsonl")
    elif result["data"]["node"]["partialDataUrl"] != None:
        download_file(result["data"]["node"]["partialDataUrl"],
                      "output/shopify_collections.jsonl")


def main():
    print("Welcome to Categories Migration Menu")
    print("1. Migrate Categories from OpenCart to Shopify")
    print("2. Get status of bulk migration operation")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        test_item_count = int(
            input("Enter the number of items to migrate (0 for all): "))
        migrate_categories_from_open_cart_to_shopify(
            test_item_count=test_item_count)
    elif choice == 2:
        print("Get Status of Bulk Migration Operation")
        print("Enter ID of the migration operation : ")
        migration_id = str(input())
        fetch_bulk_qery_status(migration_id)


# Call Main
main()
