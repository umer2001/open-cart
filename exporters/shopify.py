import binascii
import json
import os

import requests
from exporters.base import BaseExporter
import shopify

from models.shopify.shopify_customer import ShopifyCustomer


class ShopifyExporter(BaseExporter):
    def __init__(self):
        super().__init__()
        self.shop_url = os.getenv('SHOP')
        self.api_version = "2022-04"
        self.endpoint = "{}/admin/api/{}/graphql.json".format(
            self.shop_url, self.api_version)
        self.headers = {
            'X-Shopify-Access-Token': os.getenv('ACCESS_TOKEN'),
            'Content-Type': 'application/json'
        }
        self.api_key = os.getenv('API_KEY')
        self.api_secret = os.getenv('API_SECRET_KEY')
        self.access_token = os.getenv('ACCESS_TOKEN')
        self.session = shopify.Session(
            self.shop_url, self.api_version, self.access_token)

    def authentication(self):
        shopify.ShopifyResource.activate_session(self.session)
        shop = shopify.Shop.current()  # Get the current shop
        print(shop)

    def create_bulk_upload_url(self, file_name):
        client = shopify.GraphQL()
        client.endpoint = self.endpoint
        client.headers = self.headers
        upload_info_res = client.execute(
            """mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
                        stagedUploadsCreate(input: $input) {
                            stagedTargets {
                            parameters {
                                name
                                value
                            }
                            resourceUrl
                            url
                            }
                            userErrors {
                            field
                            message
                            }
                        }
                    }""",
            variables={
                "input": {
                    "filename": f"{file_name}",
                    "httpMethod": "POST",
                    "mimeType": "text/jsonl",
                    "resource": "BULK_MUTATION_VARIABLES"
                }
            }
        )
        return json.loads(upload_info_res).get('data')

    def upload_file(self, upload_info, file_path):
        upload_result = requests.post(
            upload_info['stagedUploadsCreate']['stagedTargets'][0]['url'],
            data={
                "x-amz-credential": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][5]['value'],
                "x-amz-algorithm": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][6]['value'],
                "x-amz-date": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][7]['value'],
                "x-amz-signature": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][8]['value'],
                "policy": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][4]['value'],
                "acl": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][3]['value'],
                "Content-Type": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][1]['value'],
                "success_action_status": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][2]['value'],
                'key': upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][0]['value'],
            },
            files={"file": open(file_path, 'rb')}
        ).text

    def bulk_mutation_status(self, bulk_operation_id):
        client = shopify.GraphQL()
        client.endpoint = self.endpoint
        client.headers = self.headers
        return client.execute(
            """query status($id: ID!) {
                    node(id: $id) {
                        ... on BulkOperation {
                        url
                        partialDataUrl
                        }
                    }
                }""",
            variables={
                "id": bulk_operation_id
            }
        )

    def export_product(self):
        # Add product through GraphQl
        client = shopify.GraphQL()
        client.endpoint = self.endpoint
        client.headers = self.headers
        return client.execute(
            """mutation {
                productCreate(input: {
                    title: "Timmy"
                    descriptionHtml: "..."
                    bodyHtml: "..."
                    images: []
                    tags: []
                    collectionsToJoin: []
                    variants: []
                    vendor: ""
                })
                {
                    product {
                    id
                    }
                }
            }"""
        )

    def export_customer(self, customer: ShopifyCustomer):
        client = shopify.GraphQL()
        client.endpoint = self.endpoint
        client.headers = self.headers
        print(customer.to_dict())
        return client.execute(
            """mutation customerCreate($input: CustomerInput!) {
                    customerCreate(input: $input) {
                        customer {
                        id
                        firstName
                        }
                        userErrors {
                        field
                        message
                        }
                    }
                }""",
            variables={
                "input": customer.to_dict()
            }
        )

    def bulk_export_products(self, file_name, file_path):
        upload_info = self.create_bulk_upload_url(file_name=file_name)
        # POST request to staged upload with parameters as form inputs in the request body.
        self.upload_file(upload_info=upload_info, file_path=file_path)

        # Add products through GraphQl
        client = shopify.GraphQL()
        client.endpoint = self.endpoint
        client.headers = self.headers

        mutation_res = client.execute(
            """mutation bulkOperationRunMutation($stagedUploadPath: String!) {
                bulkOperationRunMutation(
                    mutation: "mutation call($input: ProductInput!) { productCreate(input: $input) { product {id title variants(first: 10) {edges {node {id title inventoryQuantity }}}} userErrors { message field } } }",
                    stagedUploadPath: $stagedUploadPath
                ) {
                    bulkOperation {
                    id
                    url
                    partialDataUrl
                    status
                    }
                    userErrors {
                    message
                    field
                    }
                }
            }""",
            variables={
                "stagedUploadPath": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][0]['value']
            }
        )
        mutation_result = json.loads(mutation_res).get('data')
        print("upload_info", mutation_result)

    def bulk_export_collections(self, file_name, file_path):
        print("making bulk upload URL")
        upload_info = self.create_bulk_upload_url(file_name=file_name)
        # POST request to staged upload with parameters as form inputs in the request body.
        print("uploading file")
        self.upload_file(upload_info=upload_info, file_path=file_path)
        print("making bulk export")
        # Add products through GraphQl
        client = shopify.GraphQL()
        client.endpoint = self.endpoint
        client.headers = self.headers

        mutation_res = client.execute(
            """mutation bulkOperationRunMutation($stagedUploadPath: String!) {
                bulkOperationRunMutation(
                    mutation: "mutation call($input: CollectionInput!) { collectionCreate(input: $input) { collection {id title } userErrors { message field } } }",
                    stagedUploadPath: $stagedUploadPath
                ) {
                    bulkOperation {
                    id
                    url
                    partialDataUrl
                    status
                    }
                    userErrors {
                    message
                    field
                    }
                }
            }""",
            variables={
                "stagedUploadPath": upload_info['stagedUploadsCreate']['stagedTargets'][0]['parameters'][0]['value']
            }
        )
        mutation_result = json.loads(mutation_res).get('data')
        print("upload_info", mutation_result)
