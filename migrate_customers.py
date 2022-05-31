import json
from exporters.shopify import ShopifyExporter
from exporters.shopify_multi_vendor import ShopifyMultiVendorExporter
from importer.opencart import OpencartImporter
from models.open_cart.open_cart_customer import open_cart_customer_from_dict


def migrate_customers_from_open_cart_to_shopify(test_item_count=0):
    importer = OpencartImporter()
    customers = importer.fetch_customers(total_customers=7787)

    # write customers to  json file
    json.dump(customers, open(
        "source/opencart/opencart_customers.json", "w"))

    # read customers from json file
    customers = json.load(open(
        "source/opencart/opencart_customers.json", "r"))

    open_cart_customers = [open_cart_customer_from_dict(
        customer) for customer in customers]

    # loop over 3 customers
    items_to_migrate_count = test_item_count if test_item_count > 0 else len(
        open_cart_customers)
    shopify_customers = [
        open_cart_customers[index].to_shopify_customer() for index in range(items_to_migrate_count)]

    # push to shopify
    exporter = ShopifyExporter()
    exporter.authentication()

    failures = []
    successes: dict = {}
    try:
        for customerIndex in range(0, len(shopify_customers)):
            print(f"customerIndex: {customerIndex}")
            result = json.loads(exporter.export_customer(
                shopify_customers[customerIndex]))
            if result["data"]["customerCreate"]["userErrors"] or result.get("errors", []):
                print(result)
                failures.append(shopify_customers[customerIndex].to_dict())
                json.dump(failures, open(
                    "output/failures/opencart_customers_failures.json", "w"))
            else:
                if result["data"]["customerCreate"]["customer"]["id"]:
                    successes[shopify_customers[customerIndex].email] = result["data"]["customerCreate"]["customer"]["id"]
                    json.dump(successes, open(
                        "output/successes/opencart_customers_successes.json", "w"))
            customerIndex += 1
    except Exception as e:
        print(e)


def main():
    print("Welcome to Customer Migration Menu")
    print("1. Migrate Customers from OpenCart to Shopify")

    choice = int(input("Enter your choice: "))
    test_item_count = int(
        input("Enter the number of items to migrate (0 for all): "))

    if choice == 1:
        migrate_customers_from_open_cart_to_shopify(
            test_item_count=test_item_count)


# Call Main
main()
