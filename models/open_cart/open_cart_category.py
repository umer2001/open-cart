from typing import Any
from dataclasses import dataclass
import json

from models.shopify.shopify_collection import SEO, Metafield, RuleSet, Rules, ShopifyCollection, ShopifyCollectionImage


@dataclass
class OpenCartCategory:
    category_id: str
    name: str
    description: str
    sort_order: str
    meta_title: str
    meta_description: str
    meta_keyword: str
    language_id: str
    image: str
    original_image: str

    @staticmethod
    def from_dict(obj: Any) -> 'OpenCartCategory':
        if obj.get("category_id") is not None:
            _id = str(obj.get("category_id"))
        else:
            _id = None
        if obj.get("name") is not None:
            _name = str(obj.get("name"))
        else:
            _name = None
        if obj.get("description") is not None:
            _description = str(obj.get("description"))
        else:
            _description = None
        if obj.get("sort_order") is not None:
            _sort_order = str(obj.get("sort_order"))
        else:
            _sort_order = None
        if obj.get("meta_title") is not None:
            _meta_title = str(obj.get("meta_title"))
        else:
            _meta_title = None
        if obj.get("meta_description") is not None:
            _meta_description = str(obj.get("meta_description"))
        else:
            _meta_description = None
        if obj.get("meta_keyword") is not None:
            _meta_keyword = str(obj.get("meta_keyword"))
        else:
            _meta_keyword = None
        if obj.get("language_id") is not None:
            _language_id = str(obj.get("language_id"))
        else:
            _language_id = None
        if obj.get("image") is not None:
            _image = str(obj.get("image"))
        else:
            _image = None
        if obj.get("original_image") is not None:
            _original_image = str(obj.get("original_image"))
        else:
            _original_image = None
        return OpenCartCategory(_id, _name, _description, _sort_order, _meta_title, _meta_description, _meta_keyword, _language_id, _image, _original_image)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.category_id is not None:
            result["category_id"] = self.category_id
        if self.name is not None:
            result["name"] = self.name
        if self.description is not None:
            result["description"] = self.description
        if self.sort_order is not None:
            result["sort_order"] = self.sort_order
        if self.meta_title is not None:
            result["meta_title"] = self.meta_title
        if self.meta_description is not None:
            result["meta_description"] = self.meta_description
        if self.meta_keyword is not None:
            result["meta_keyword"] = self.meta_keyword
        if self.language_id is not None:
            result["language_id"] = self.language_id
        if self.image is not None:
            result["image"] = self.image
        if self.original_image is not None:
            result["original_image"] = self.original_image
        return result

    def to_shopify_collection(self):
        return ShopifyCollection(
            # id=f"gid://shopify/Collection/{self.category_id}",
            id=None,
            title=self.name,
            description_html=self.description,
            sort_order="CREATED_DESC",
            template_suffix=None,
            handle=None,
            redirect_new_handle=None,
            image=ShopifyCollectionImage(
                id=None,
                src=self.original_image,
                alt_text=f"{self.name} image"
            ),
            metafields=[Metafield(
                # id=f"gid://shopify/Metafield/112200",
                id=None,
                description=self.meta_description,
                key="description",
                namespace="description",
                type="multi_line_text_field",
                value=self.meta_description
            )],
            seo=SEO(
                description=self.meta_description,
                title=self.meta_title
            ),
            rule_set=RuleSet(
                applied_disjunctively=True,
                rules=Rules(
                    column="TAG",
                    condition=self.name,
                    relation="EQUALS",
                )
            ),
            products=[],
            private_metafields=[],
            publications=[],
        )
