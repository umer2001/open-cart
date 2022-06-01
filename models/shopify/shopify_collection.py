from typing import List
from typing import Any
import json

from typing import Any, List, TypeVar, Type, cast, Callable

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = shopify_collection_from_dict(json.loads(json_string))


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class ShopifyCollectionImage:
    id: str
    src: str
    alt_text: str

    def __init__(self, id: str, src: str, alt_text: str) -> None:
        self.id = id
        self.src = src
        self.alt_text = alt_text

    @staticmethod
    def from_dict(obj: Any) -> 'ShopifyCollectionImage':
        assert isinstance(obj, dict)
        if obj.get("id") is not None:
            id = from_str(obj.get("id"))
        else:
            id = None
        if obj.get("src") is not None:
            src = from_str(obj.get("src"))
        else:
            src = None
        if obj.get("altText") is not None:
            alt_text = from_str(obj.get("altText"))
        else:
            alt_text = None
        return ShopifyCollectionImage(id, src, alt_text)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_str(self.id)
        if self.src is not None:
            result["src"] = from_str(self.src)
        if self.alt_text is not None:
            result["altText"] = from_str(self.alt_text)
        return result


class Metafield:
    id: str
    key: str
    description: str
    namespace: str
    type: str
    value: str

    def __init__(self, id: str, key: str, description: str, namespace: str, type: str, value: str) -> None:
        self.id = id
        self.key = key
        self.description = description
        self.namespace = namespace
        self.type = type
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'Metafield':
        assert isinstance(obj, dict)
        if obj.get("id") is not None:
            id = from_str(obj.get("id"))
        else:
            id = None
        if obj.get("key") is not None:
            key = from_str(obj.get("key"))
        else:
            key = None
        if obj.get("description") is not None:
            description = from_str(obj.get("description"))
        else:
            description = None
        if obj.get("namespace") is not None:
            namespace = from_str(obj.get("namespace"))
        else:
            namespace = None
        if obj.get("type") is not None:
            type = from_str(obj.get("type"))
        else:
            type = None
        if obj.get("value") is not None:
            value = from_str(obj.get("value"))
        else:
            value = None
        return Metafield(id, key, description, namespace, type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_str(self.id)
        if self.key is not None:
            result["key"] = from_str(self.key)
        if self.description is not None:
            result["description"] = from_str(self.description)
        if self.namespace is not None:
            result["namespace"] = from_str(self.namespace)
        if self.type is not None:
            result["type"] = from_str(self.type)
        if self.value is not None:
            result["value"] = from_str(self.value)
        return result


class ValueInput:
    value: str
    value_type: str

    def __init__(self, value: str, value_type: str) -> None:
        self.value = value
        self.value_type = value_type

    @staticmethod
    def from_dict(obj: Any) -> 'ValueInput':
        assert isinstance(obj, dict)
        if obj.get("AAA") is not None:
            value = from_str(obj.get("value"))
        else:
            value = None
        if obj.get("AAA") is not None:
            value_type = from_str(obj.get("valueType"))
        else:
            value_type = None
        return ValueInput(value, value_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.value is not None:
            result["value"] = from_str(self.value)
        if self.value_type is not None:
            result["valueType"] = from_str(self.value_type)
        return result


class PrivateMetafield:
    key: str
    namespace: str
    owner: str
    value_input: ValueInput

    def __init__(self, key: str, namespace: str, owner: str, value_input: ValueInput) -> None:
        self.key = key
        self.namespace = namespace
        self.owner = owner
        self.value_input = value_input

    @staticmethod
    def from_dict(obj: Any) -> 'PrivateMetafield':
        assert isinstance(obj, dict)
        if obj.get("key") is not None:
            key = from_str(obj.get("key"))
        else:
            key = None
        if obj.get("namespace") is not None:
            namespace = from_str(obj.get("namespace"))
        else:
            namespace = None
        if obj.get("owner") is not None:
            owner = from_str(obj.get("owner"))
        else:
            owner = None
        if obj.get("valueInput") is not None:
            value_input = ValueInput.from_dict(obj.get("valueInput"))
        else:
            value_input = None
        return PrivateMetafield(key, namespace, owner, value_input)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_str(self.key)
        if self.namespace is not None:
            result["namespace"] = from_str(self.namespace)
        if self.owner is not None:
            result["owner"] = from_str(self.owner)
        if self.value_input is not None:
            result["valueInput"] = to_class(ValueInput, self.value_input)
        return result


class Publication:
    channel_handle: str
    channel_id: str
    publication_id: str

    def __init__(self, channel_handle: str, channel_id: str, publication_id: str) -> None:
        self.channel_handle = channel_handle
        self.channel_id = channel_id
        self.publication_id = publication_id

    @staticmethod
    def from_dict(obj: Any) -> 'Publication':
        assert isinstance(obj, dict)
        if obj.get("channelHandle") is not None:
            channel_handle = from_str(obj.get("channelHandle"))
        else:
            channel_handle = None
        if obj.get("channelId") is not None:
            channel_id = from_str(obj.get("channelId"))
        else:
            channel_id = None
        if obj.get("publicationId") is not None:
            publication_id = from_str(obj.get("publicationId"))
        else:
            publication_id = None
        return Publication(channel_handle, channel_id, publication_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.channel_handle is not None:
            result["channelHandle"] = from_str(self.channel_handle)
        if self.channel_id is not None:
            result["channelId"] = from_str(self.channel_id)
        if self.publication_id is not None:
            result["publicationId"] = from_str(self.publication_id)
        return result


class Rules:
    column: str
    condition: str
    relation: str

    def __init__(self, column: str, condition: str, relation: str) -> None:
        self.column = column
        self.condition = condition
        self.relation = relation

    @staticmethod
    def from_dict(obj: Any) -> 'Rules':
        assert isinstance(obj, dict)
        column = from_str(obj.get("column"))
        condition = from_str(obj.get("condition"))
        relation = from_str(obj.get("relation"))
        return Rules(column, condition, relation)

    def to_dict(self) -> dict:
        result: dict = {}
        result["column"] = from_str(self.column)
        result["condition"] = from_str(self.condition)
        result["relation"] = from_str(self.relation)
        return result


class RuleSet:
    applied_disjunctively: bool
    rules: Rules

    def __init__(self, applied_disjunctively: bool, rules: Rules) -> None:
        self.applied_disjunctively = applied_disjunctively
        self.rules = rules

    @staticmethod
    def from_dict(obj: Any) -> 'RuleSet':
        assert isinstance(obj, dict)
        if obj.get("appliedDisjunctively") is not None:
            applied_disjunctively = from_bool(obj.get("appliedDisjunctively"))
        else:
            applied_disjunctively = None
        if obj.get("rules") is not None:
            rules = Rules.from_dict(obj.get("rules"))
        else:
            rules = None
        return RuleSet(applied_disjunctively, rules)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.applied_disjunctively is not None:
            result["appliedDisjunctively"] = from_bool(
                self.applied_disjunctively)
        if self.rules is not None:
            result["rules"] = to_class(Rules, self.rules)
        return result


class SEO:
    description: str
    title: str

    def __init__(self, description: str, title: str) -> None:
        self.description = description
        self.title = title

    @staticmethod
    def from_dict(obj: Any) -> 'SEO':
        assert isinstance(obj, dict)
        if obj.get("description") is not None:
            description = from_str(obj.get("description"))
        else:
            description = None
        if obj.get("title") is not None:
            title = from_str(obj.get("title"))
        else:
            title = None
        return SEO(description, title)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_str(self.description)
        if self.title is not None:
            result["title"] = from_str(self.title)
        return result


class ShopifyCollection:
    id: str
    title: str
    description_html: str
    sort_order: str
    template_suffix: str
    handle: str
    image: ShopifyCollectionImage
    metafields: List[Metafield]
    private_metafields: List[PrivateMetafield]
    products: List[str]
    publications: List[Publication]
    redirect_new_handle: bool
    rule_set: RuleSet
    seo: SEO

    def __init__(self, id: str, title: str, description_html: str, sort_order: str, template_suffix: str, handle: str, image: ShopifyCollectionImage, metafields: List[Metafield], private_metafields: List[PrivateMetafield], products: List[str], publications: List[Publication], redirect_new_handle: bool, rule_set: RuleSet, seo: SEO) -> None:
        self.id = id
        self.title = title
        self.description_html = description_html
        self.sort_order = sort_order
        self.template_suffix = template_suffix
        self.handle = handle
        self.image = image
        self.metafields = metafields
        self.private_metafields = private_metafields
        self.products = products
        self.publications = publications
        self.redirect_new_handle = redirect_new_handle
        self.rule_set = rule_set
        self.seo = seo

    @staticmethod
    def from_dict(obj: Any) -> 'ShopifyCollection':
        assert isinstance(obj, dict)
        if obj.get("id") is not None:
            id = from_str(obj.get("id"))
        else:
            id = None
        if obj.get("title") is not None:
            title = from_str(obj.get("title"))
        else:
            title = None
        if obj.get("descriptionHtml") is not None:
            description_html = from_str(obj.get("descriptionHtml"))
        else:
            description_html = None
        if obj.get("sortOrder") is not None:
            sort_order = from_str(obj.get("sortOrder"))
        else:
            sort_order = None
        if obj.get("templateSuffix") is not None:
            template_suffix = from_str(obj.get("templateSuffix"))
        else:
            template_suffix = None
        if obj.get("handle") is not None:
            handle = from_str(obj.get("handle"))
        else:
            handle = None
        if obj.get("image") is not None:
            image = ShopifyCollectionImage.from_dict(obj.get("image"))
        else:
            image = None
        if obj.get("metafields") is not None:
            metafields = from_list(Metafield.from_dict, obj.get("metafields"))
        else:
            metafields = []
        if obj.get("privateMetafields") is not None:
            private_metafields = from_list(
                PrivateMetafield.from_dict, obj.get("privateMetafields"))
        else:
            private_metafields = []
        if obj.get("products") is not None:
            products = from_list(from_str, obj.get("products"))
        else:
            products = []
        if obj.get("publications") is not None:
            publications = from_list(
                Publication.from_dict, obj.get("publications"))
        else:
            publications = []
        if obj.get("redirectNewHandle") is not None:
            redirect_new_handle = from_bool(obj.get("redirectNewHandle"))
        else:
            redirect_new_handle = None
        if obj.get("ruleSet") is not None:
            rule_set = RuleSet.from_dict(obj.get("ruleSet"))
        else:
            rule_set = None
        if obj.get("seo") is not None:
            seo = SEO.from_dict(obj.get("seo"))
        else:
            seo = None
        return ShopifyCollection(id, title, description_html, sort_order, template_suffix, handle, image, metafields, private_metafields, products, publications, redirect_new_handle, rule_set, seo)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_str(self.id)
        if self.title is not None:
            result["title"] = from_str(self.title)
        if self.description_html is not None:
            result["descriptionHtml"] = from_str(self.description_html)
        if self.sort_order is not None:
            result["sortOrder"] = from_str(self.sort_order)
        if self.template_suffix is not None:
            result["templateSuffix"] = from_str(self.template_suffix)
        if self.handle is not None:
            result["handle"] = from_str(self.handle)
        if self.image is not None:
            result["image"] = to_class(ShopifyCollectionImage, self.image)
        if self.metafields is not None:
            result["metafields"] = from_list(
                lambda x: to_class(Metafield, x), self.metafields)
        if self.private_metafields is not None:
            result["privateMetafields"] = from_list(
                lambda x: to_class(PrivateMetafield, x), self.private_metafields)
        if self.products is not None:
            result["products"] = from_list(from_str, self.products)
        if self.publications is not None:
            result["publications"] = from_list(
                lambda x: to_class(Publication, x), self.publications)
        if self.redirect_new_handle is not None:
            result["redirectNewHandle"] = from_bool(self.redirect_new_handle)
        if self.rule_set is not None:
            result["ruleSet"] = to_class(RuleSet, self.rule_set)
        if self.seo is not None:
            result["seo"] = to_class(SEO, self.seo)
        return result


def shopify_collection_from_dict(s: Any) -> ShopifyCollection:
    return ShopifyCollection.from_dict(s)


def shopify_collection_to_dict(x: ShopifyCollection) -> Any:
    return to_class(ShopifyCollection, x)
