# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = OpenCartProduct_from_dict(json.loads(json_string))

import random
# from time import pthread_getcpuclockid
from typing import Optional, Any, Dict, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser

from models.shopify.shopify_product import ShopifyProduct, ShopifyProductImage, Variant
from models.shopify_multi_vendor.shopify_multi_vendor_product import MvmImage, MvmOption, MvmVariant, ShopifyMultiVendorProduct
from utils import evaluate_seller_id


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


class ProductDescription:
    category_id: Optional[int]
    name: str
    description: str
    sort_order: Optional[int]
    meta_title: str
    meta_description: str
    meta_keyword: str
    language_id: int
    tag: Optional[str]

    def __init__(self, category_id: Optional[int], name: str, description: str, sort_order: Optional[int], meta_title: str, meta_description: str, meta_keyword: str, language_id: int, tag: Optional[str]) -> None:
        self.category_id = category_id
        self.name = name
        self.description = description
        self.sort_order = sort_order
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keyword = meta_keyword
        self.language_id = language_id
        self.tag = tag

    @staticmethod
    def from_dict(obj: Any) -> 'ProductDescription':
        assert isinstance(obj, dict)
        category_id = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("category_id"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        sort_order = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("sort_order"))
        meta_title = from_str(obj.get("meta_title"))
        meta_description = from_str(obj.get("meta_description"))
        meta_keyword = from_str(obj.get("meta_keyword"))
        language_id = int(from_str(obj.get("language_id")))
        tag = from_union([from_str, from_none], obj.get("tag"))
        return ProductDescription(category_id, name, description, sort_order, meta_title, meta_description, meta_keyword, language_id, tag)

    def to_dict(self) -> dict:
        result: dict = {}
        result["category_id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
            x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.category_id)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["sort_order"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
            x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.sort_order)
        result["meta_title"] = from_str(self.meta_title)
        result["meta_description"] = from_str(self.meta_description)
        result["meta_keyword"] = from_str(self.meta_keyword)
        result["language_id"] = from_str(str(self.language_id))
        result["tag"] = from_union([from_str, from_none], self.tag)
        return result


class Keyword:
    the_1: str

    def __init__(self, the_1: str) -> None:
        self.the_1 = the_1

    @staticmethod
    def from_dict(obj: Any) -> 'Keyword':
        assert isinstance(obj, dict)
        the_1 = from_str(obj.get("1"))
        return Keyword(the_1)

    def to_dict(self) -> dict:
        result: dict = {}
        result["1"] = from_str(self.the_1)
        return result


class The1:
    attribute_id: int
    name: str
    text: str
    attribute_group_id: int
    language_id: int

    def __init__(self, attribute_id: int, name: str, text: str, attribute_group_id: int, language_id: int) -> None:
        self.attribute_id = attribute_id
        self.name = name
        self.text = text
        self.attribute_group_id = attribute_group_id
        self.language_id = language_id

    @staticmethod
    def from_dict(obj: Any) -> 'The1':
        assert isinstance(obj, dict)
        attribute_id = int(from_str(obj.get("attribute_id")))
        name = from_str(obj.get("name"))
        text = from_str(obj.get("text"))
        attribute_group_id = int(from_str(obj.get("attribute_group_id")))
        language_id = int(from_str(obj.get("language_id")))
        return The1(attribute_id, name, text, attribute_group_id, language_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["attribute_id"] = from_str(str(self.attribute_id))
        result["name"] = from_str(self.name)
        result["text"] = from_str(self.text)
        result["attribute_group_id"] = from_str(str(self.attribute_group_id))
        result["language_id"] = from_str(str(self.language_id))
        return result


class Attribute:
    the_1: The1

    def __init__(self, the_1: The1) -> None:
        self.the_1 = the_1

    @staticmethod
    def from_dict(obj: Any) -> 'Attribute':
        assert isinstance(obj, dict)
        the_1 = The1.from_dict(obj.get("1"))
        return Attribute(the_1)

    def to_dict(self) -> dict:
        result: dict = {}
        result["1"] = to_class(The1, self.the_1)
        return result


class ProductAttributes:
    attributes: Dict[str, Attribute]

    def __init__(self, attributes: Dict[str, Attribute]) -> None:
        self.attributes = attributes

    @staticmethod
    def from_dict(obj: Any) -> 'ProductAttributes':
        if isinstance(obj, list):
            return ProductAttributes({})
        assert isinstance(obj, dict)
        if obj.get("attributes") is not None:
            attributes = from_dict(Attribute.from_dict, obj.get("attributes"))
        else:
            attributes = {}
        return ProductAttributes(attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.attributes is not None:
            result["attributes"] = from_dict(
                lambda x: to_class(Attribute, x), self.attributes)
        return result


class Reviews:
    review_total: int

    def __init__(self, review_total: int) -> None:
        self.review_total = review_total

    @staticmethod
    def from_dict(obj: Any) -> 'Reviews':
        assert isinstance(obj, dict)
        review_total = int(from_str(obj.get("review_total")))
        return Reviews(review_total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["review_total"] = from_str(str(self.review_total))
        return result


class Special:
    customer_group_id: int
    priority: int
    price: str
    date_start: datetime
    date_end: datetime

    def __init__(self, customer_group_id: int, priority: int, price: str, date_start: datetime, date_end: datetime) -> None:
        self.customer_group_id = customer_group_id
        self.priority = priority
        self.price = price
        self.date_start = date_start
        self.date_end = date_end

    @staticmethod
    def from_dict(obj: Any) -> 'Special':
        assert isinstance(obj, dict)
        if obj.get("customer_group_id") is not None:
            customer_group_id = int(from_str(obj.get("customer_group_id")))
        else:
            customer_group_id = None
        if obj.get("priority") is not None:
            priority = int(from_str(obj.get("priority")))
        else:
            priority = None
        if obj.get("price") is not None:
            price = from_str(obj.get("price"))
        else:
            price = None
        if obj.get("date_start") is not None:
            date_start = from_datetime(obj.get("date_start"))
        else:
            date_start = None
        if obj.get("date_end") is not None:
            date_end = from_datetime(obj.get("date_end"))
        else:
            date_end = None
        return Special(customer_group_id, priority, price, date_start, date_end)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.customer_group_id is not None:
            result["customer_group_id"] = from_str(str(self.customer_group_id))
        if self.priority is not None:
            result["priority"] = from_str(str(self.priority))
        if self.price is not None:
            result["price"] = from_str(self.price)
        if self.date_start is not None:
            result["date_start"] = self.date_start.isoformat()
        if self.date_end is not None:
            result["date_end"] = self.date_end.isoformat()
        return result


class OpenCartProduct:
    id: int
    manufacturer: str
    sku: str
    model: str
    image: str
    images: List[str]
    original_image: str
    original_images: List[str]
    price: str
    tax_value: int
    price_formated: str
    rating: int
    product_description: List[ProductDescription]
    product_attributes: ProductAttributes
    special: List[Special]
    discounts: List[Any]
    options: List[Any]
    minimum: int
    upc: str
    ean: str
    jan: str
    isbn: str
    mpn: str
    location: str
    stock_status: str
    manufacturer_id: int
    tax_class_id: int
    date_available: datetime
    weight: str
    weight_class_id: int
    length: str
    width: str
    height: str
    length_class_id: int
    subtract: int
    sort_order: int
    status: int
    stock_status_id: int
    date_added: datetime
    date_modified: datetime
    viewed: int
    weight_class: str
    length_class: str
    reward: str
    points: int
    keyword: List[Keyword]
    shipping: int
    category: List[List[ProductDescription]]
    quantity: int
    reviews: Reviews
    product_relateds: List[int]
    filters: List[int]
    currency_id: int
    currency_code: str
    currency_value: str

    def __init__(self, id: int, manufacturer: str, sku: str, model: str, image: str, images: List[str], original_image: str, original_images: List[str], price: str, tax_value: int, price_formated: str, rating: int, product_description: List[ProductDescription], product_attributes: ProductAttributes, special: List[Special], discounts: List[Any], options: List[Any], minimum: int, upc: str, ean: str, jan: str, isbn: str, mpn: str, location: str, stock_status: str, manufacturer_id: int, tax_class_id: int, date_available: datetime, weight: str, weight_class_id: int, length: str, width: str, height: str, length_class_id: int, subtract: int, sort_order: int, status: int, stock_status_id: int, date_added: datetime, date_modified: datetime, viewed: int, weight_class: str, length_class: str, reward: str, points: int, keyword: List[Keyword], shipping: int, category: List[List[ProductDescription]], quantity: int, reviews: Reviews, product_relateds: List[int], filters: List[int], currency_id: int, currency_code: str, currency_value: str) -> None:
        self.id = id
        self.manufacturer = manufacturer
        self.sku = sku
        self.model = model
        self.image = image
        self.images = images
        self.original_image = original_image
        self.original_images = original_images
        self.price = price
        self.tax_value = tax_value
        self.price_formated = price_formated
        self.rating = rating
        self.product_description = product_description
        self.product_attributes = product_attributes
        self.special = special
        self.discounts = discounts
        self.options = options
        self.minimum = minimum
        self.upc = upc
        self.ean = ean
        self.jan = jan
        self.isbn = isbn
        self.mpn = mpn
        self.location = location
        self.stock_status = stock_status
        self.manufacturer_id = manufacturer_id
        self.tax_class_id = tax_class_id
        self.date_available = date_available
        self.weight = weight
        self.weight_class_id = weight_class_id
        self.length = length
        self.width = width
        self.height = height
        self.length_class_id = length_class_id
        self.subtract = subtract
        self.sort_order = sort_order
        self.status = status
        self.stock_status_id = stock_status_id
        self.date_added = date_added
        self.date_modified = date_modified
        self.viewed = viewed
        self.weight_class = weight_class
        self.length_class = length_class
        self.reward = reward
        self.points = points
        self.keyword = keyword
        self.shipping = shipping
        self.category = category
        self.quantity = quantity
        self.reviews = reviews
        self.product_relateds = product_relateds
        self.filters = filters
        self.currency_id = currency_id
        self.currency_code = currency_code
        self.currency_value = currency_value

    @staticmethod
    def from_dict(obj: Any) -> 'OpenCartProduct':
        assert isinstance(obj, dict)
        if obj.get("id") is not None:
            id = int(from_str(obj.get("id")))
        else:
            id = None
        if obj.get("manufacturer") is not None:
            manufacturer = from_str(obj.get("manufacturer"))
        else:
            manufacturer = None
        if obj.get("sku") is not None:
            sku = from_str(obj.get("sku"))
        else:
            sku = None
        if obj.get("model") is not None:
            model = from_str(obj.get("model"))
        else:
            model = None
        if obj.get("image") is not None:
            image = from_str(obj.get("image"))
        else:
            image = None
        if obj.get("images") is not None:
            images = from_list(from_str, obj.get("images"))
        else:
            images = []
        if obj.get("original_image") is not None:
            original_image = from_str(obj.get("original_image"))
        else:
            original_image = None
        if obj.get("original_images") is not None:
            original_images = from_list(from_str, obj.get("original_images"))
        else:
            original_images = []
        if obj.get("price") is not None:
            price = from_str(obj.get("price"))
        else:
            price = None
        if obj.get("tax_value") is not None:
            tax_value = from_int(obj.get("tax_value"))
        else:
            tax_value = None
        if obj.get("price_formated") is not None:
            price_formated = from_str(obj.get("price_formated"))
        else:
            price_formated = None
        if obj.get("rating") is not None:
            rating = from_int(obj.get("rating"))
        else:
            rating = None
        if obj.get("product_description") is not None:
            product_description = from_list(
                ProductDescription.from_dict, obj.get("product_description"))
        else:
            product_description = []
        if obj.get("product_attributes") is not None:
            product_attributes = ProductAttributes.from_dict(
                obj.get("product_attributes"))
        else:
            product_attributes = None
        if obj.get("special") is not None:
            special = from_list(Special.from_dict, obj.get("special"))
        else:
            special = []
        if obj.get("discounts") is not None:
            discounts = from_list(lambda x: x, obj.get("discounts"))
        else:
            discounts = []
        if obj.get("options") is not None:
            options = from_list(lambda x: x, obj.get("options"))
        else:
            options = []
        if obj.get("minimum") is not None:
            minimum = int(from_str(obj.get("minimum")))
        else:
            minimum = None
        if obj.get("upc") is not None:
            upc = from_str(obj.get("upc"))
        else:
            upc = None
        if obj.get("ean") is not None:
            ean = from_str(obj.get("ean"))
        else:
            ean = None
        if obj.get("jan") is not None:
            jan = from_str(obj.get("jan"))
        else:
            jan = None
        if obj.get("isbn") is not None:
            isbn = from_str(obj.get("isbn"))
        else:
            isbn = None
        if obj.get("mpn") is not None:
            mpn = from_str(obj.get("mpn"))
        else:
            mpn = None
        if obj.get("location") is not None:
            location = from_str(obj.get("location"))
        else:
            location = None
        if obj.get("stock_status") is not None:
            stock_status = from_str(obj.get("stock_status"))
        else:
            stock_status = None
        if obj.get("manufacturer_id") is not None and obj.get("manufacturer_id") != "":
            manufacturer_id = int(from_str(obj.get("manufacturer_id")))
        else:
            manufacturer_id = None
        if obj.get("tax_class_id") is not None:
            tax_class_id = int(from_str(obj.get("tax_class_id")))
        else:
            tax_class_id = None
        if obj.get("date_available") is not None:
            date_available = from_datetime(obj.get("date_available"))
        else:
            date_available = None
        if obj.get("weight") is not None:
            weight = from_str(obj.get("weight"))
        else:
            weight = None
        if obj.get("weight_class_id") is not None:
            weight_class_id = int(from_str(obj.get("weight_class_id")))
        else:
            weight_class_id = None
        if obj.get("length") is not None:
            length = from_str(obj.get("length"))
        else:
            length = None
        if obj.get("width") is not None:
            width = from_str(obj.get("width"))
        else:
            width = None
        if obj.get("height") is not None:
            height = from_str(obj.get("height"))
        else:
            height = None
        if obj.get("length_class_id") is not None:
            length_class_id = int(from_str(obj.get("length_class_id")))
        else:
            length_class_id = None
        if obj.get("subtract") is not None:
            subtract = int(from_str(obj.get("subtract")))
        else:
            subtract = None
        if obj.get("sort_order") is not None:
            sort_order = int(from_str(obj.get("sort_order")))
        else:
            sort_order = None
        if obj.get("status") is not None:
            status = int(from_str(obj.get("status")))
        else:
            status = None
        if obj.get("stock_status_id") is not None:
            stock_status_id = int(from_str(obj.get("stock_status_id")))
        else:
            stock_status_id = None
        if obj.get("date_added") is not None:
            date_added = from_datetime(obj.get("date_added"))
        else:
            some = None
        if obj.get("date_modified") is not None:
            date_modified = from_datetime(obj.get("date_modified"))
        else:
            date_modified = None
        if obj.get("viewed") is not None:
            viewed = int(from_str(obj.get("viewed")))
        else:
            viewed = None
        if obj.get("weight_class") is not None:
            weight_class = from_str(obj.get("weight_class"))
        else:
            weight_class = None
        if obj.get("length_class") is not None:
            length_class = from_str(obj.get("length_class"))
        else:
            length_class = None
        if obj.get("reward") is not None:
            reward = from_str(obj.get("reward"))
        else:
            reward = None
        if obj.get("points") is not None:
            points = int(from_str(obj.get("points")))
        else:
            points = None
        if obj.get("keyword") is not None:
            keyword = from_list(Keyword.from_dict, obj.get("keyword"))
        else:
            keyword = []
        if obj.get("shipping") is not None:
            shipping = int(from_str(obj.get("shipping")))
        else:
            shipping = None
        if obj.get("category") is not None:
            category = from_list(lambda x: from_list(
                ProductDescription.from_dict, x), obj.get("category"))
        else:
            category = [[]]
        if obj.get("quantity") is not None:
            quantity = int(from_str(obj.get("quantity")))
        else:
            quantity = None
        if obj.get("reviews") is not None:
            reviews = Reviews.from_dict(obj.get("reviews"))
        else:
            reviews = None
        if obj.get("product_relateds") is not None:
            product_relateds = from_list(lambda x: int(
                from_str(x)), obj.get("product_relateds"))
        else:
            product_relateds = []
        if obj.get("filters") is not None:
            filters = from_list(lambda x: int(from_str(x)), obj.get("filters"))
        else:
            filters = []
        if obj.get("currency_id") is not None:
            currency_id = int(from_str(obj.get("currency_id")))
        else:
            currency_id = None
        if obj.get("currency_code") is not None:
            currency_code = from_str(obj.get("currency_code"))
        else:
            currency_code = None
        if obj.get("currency_value") is not None:
            currency_value = from_str(obj.get("currency_value"))
        else:
            currency_value = None
        return OpenCartProduct(id, manufacturer, sku, model, image, images, original_image, original_images, price, tax_value, price_formated, rating, product_description, product_attributes, special, discounts, options, minimum, upc, ean, jan, isbn, mpn, location, stock_status, manufacturer_id, tax_class_id, date_available, weight, weight_class_id, length, width, height, length_class_id, subtract, sort_order, status, stock_status_id, date_added, date_modified, viewed, weight_class, length_class, reward, points, keyword, shipping, category, quantity, reviews, product_relateds, filters, currency_id, currency_code, currency_value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_str(str(self.id))
        if self.manufacturer is not None:
            result["manufacturer"] = from_str(self.manufacturer)
        if self.sku is not None:
            result["sku"] = from_str(self.sku)
        if self.model is not None:
            result["model"] = from_str(self.model)
        if self.image is not None:
            result["image"] = from_str(self.image)
        if self.images is not None:
            result["images"] = from_list(from_str, self.images)
        if self.original_image is not None:
            result["original_image"] = from_str(self.original_image)
        if self.original_images is not None:
            result["original_images"] = from_list(
                from_str, self.original_images)
        if self.price is not None:
            result["price"] = from_str(self.price)
        if self.tax_value is not None:
            result["tax_value"] = from_int(self.tax_value)
        if self.price_formated is not None:
            result["price_formated"] = from_str(self.price_formated)
        if self.rating is not None:
            result["rating"] = from_int(self.rating)
        if self.product_description is not None:
            result["product_description"] = from_list(lambda x: to_class(
                ProductDescription, x), self.product_description)
        if self.product_attributes is not None:
            result["product_attributes"] = to_class(
                ProductAttributes, self.product_attributes)
        if self.special is not None:
            result["special"] = from_list(
                lambda x: to_class(Special, x), self.special)
        if self.discounts is not None:
            result["discounts"] = from_list(lambda x: x, self.discounts)
        if self.options is not None:
            result["options"] = from_list(lambda x: x, self.options)
        if self.minimum is not None:
            result["minimum"] = from_str(str(self.minimum))
        if self.upc is not None:
            result["upc"] = from_str(self.upc)
        if self.ean is not None:
            result["ean"] = from_str(self.ean)
        if self.jan is not None:
            result["jan"] = from_str(self.jan)
        if self.isbn is not None:
            result["isbn"] = from_str(self.isbn)
        if self.mpn is not None:
            result["mpn"] = from_str(self.mpn)
        if self.location is not None:
            result["location"] = from_str(self.location)
        if self.stock_status is not None:
            result["stock_status"] = from_str(self.stock_status)
        if self.manufacturer_id is not None:
            result["manufacturer_id"] = from_str(str(self.manufacturer_id))
        if self.tax_class_id is not None:
            result["tax_class_id"] = from_str(str(self.tax_class_id))
        if self.date_available is not None:
            result["date_available"] = self.date_available.isoformat()
        if self.weight is not None:
            result["weight"] = from_str(self.weight)
        if self.weight_class_id is not None:
            result["weight_class_id"] = from_str(str(self.weight_class_id))
        if self.length is not None:
            result["length"] = from_str(self.length)
        if self.weight is not None:
            result["width"] = from_str(self.width)
        if self.height is not None:
            result["height"] = from_str(self.height)
        if self.length_class_id is not None:
            result["length_class_id"] = from_str(str(self.length_class_id))
        if self.subtract is not None:
            result["subtract"] = from_str(str(self.subtract))
        if self.sort_order is not None:
            result["sort_order"] = from_str(str(self.sort_order))
        if self.status is not None:
            result["status"] = from_str(str(self.status))
        if self.stock_status_id is not None:
            result["stock_status_id"] = from_str(str(self.stock_status_id))
        if self.date_added is not None:
            result["date_added"] = self.date_added.isoformat()
        if self.date_modified is not None:
            result["date_modified"] = self.date_modified.isoformat()
        if self.viewed is not None:
            result["viewed"] = from_str(str(self.viewed))
        if self.weight_class is not None:
            result["weight_class"] = from_str(self.weight_class)
        if self.length_class is not None:
            result["length_class"] = from_str(self.length_class)
        if self.reward is not None:
            result["reward"] = from_str(self.reward)
        if self.points is not None:
            result["points"] = from_str(str(self.points))
        if self.keyword is not None:
            result["keyword"] = from_list(
                lambda x: to_class(Keyword, x), self.keyword)
        if self.shipping is not None:
            result["shipping"] = from_str(str(self.shipping))
        if self.category is not None:
            result["category"] = from_list(lambda x: from_list(
                lambda x: to_class(ProductDescription, x), x), self.category)
        if self.quantity is not None:
            result["quantity"] = from_str(str(self.quantity))
        if self.reviews is not None:
            result["reviews"] = to_class(Reviews, self.reviews)
        if self.product_relateds is not None:
            result["product_relateds"] = from_list(lambda x: from_str(
                (lambda x: str(x))(x)), self.product_relateds)
        if self.filters is not None:
            result["filters"] = from_list(lambda x: from_str(
                (lambda x: str(x))(x)), self.filters)
        if self.currency_id is not None:
            result["currency_id"] = from_str(str(self.currency_id))
        if self.currency_code is not None:
            result["currency_code"] = from_str(self.currency_code)
        if self.currency_value is not None:
            result["currency_value"] = from_str(self.currency_value)
        return result

    def to_shopify_product(self):
        return ShopifyProduct(
            id=f"gid://shopify/Product/{self.id}",
            title=self.product_description[0].name,
            body_html=self.product_description[0].description,
            vendor=self.manufacturer,
            description_html=self.product_description[0].meta_description,
            images=[
                ShopifyProductImage(src=self.original_image, id=f"gid://shopify/ProductImage/{self.id}2",
                                    alt_text=f"{self.product_description[0].name} image"),
                *[ShopifyProductImage(src=image, id=f"gid://shopify/ProductImage/{random.randint(0, 10000000)}", alt_text=f"{self.product_description[0].name} image") for image in self.original_images]
            ],
            tags=self.keyword[0].the_1.split("-"),
            variants=[
                Variant(
                    id=f"gid://shopify/ProductVariant/{self.id}0",
                    product_id=f"gid://shopify/Product/{self.id}3",
                    sku=self.sku,
                    price=self.price,
                    requires_shipping=False,
                    weight=float(self.weight),
                    weight_unit="KILOGRAMS",
                    title=self.product_description[0].name,
                    barcode=f"{self.id}",
                    inventory_management="NOT_MANAGED",
                    image_src=self.original_image,
                    taxable=False,
                    tax_code="None",
                    compare_at_price="0",
                    image_id=f"gid://shopify/MediaImage/{self.id}1",
                )
            ],
            # options=[],
            product_type="",
            collections_to_join=[]
        )

    def to_shipify_multi_vendor_product(self) -> ShopifyMultiVendorProduct:
        return ShopifyMultiVendorProduct(
            seller_id=evaluate_seller_id(self.manufacturer),
            product_name=self.product_description[0].name,
            product_description=self.product_description[0].meta_description,
            product_meta_info=self.product_description[0].meta_description,
            images=[
                MvmImage(
                    image_url=self.original_image,
                    image_alt=f"{self.product_description[0].name} image",
                    position="0",
                    image_attachment=""
                ),
                *[MvmImage(image_url=image.replace(" ", "+"), image_alt=f"{self.product_description[0].name} image", position="1", image_attachment="") for image in self.original_images]
            ],
            variants=[
                MvmVariant(
                    price=self.price,
                    sku=None,
                    require_shipping=0,
                    weight=float(self.weight),
                    track_inventory=0,
                    handling_charges="0",
                    barcode=None,
                    inventory_locations=[],
                    inventory_policy=None,
                    charge_taxes=0,
                    # compare_at_price=f"{float(self.price)+1}",
                    compare_at_price=None,
                    dimension=None,
                    quantity=self.quantity,
                )
            ],
            collections=[],
            options=[
                MvmOption(name="Title", values="Default Title")
            ],
            product_tag=','.join(cat.name for cat in self.category[0]),
            expiry_date=None,
            handle=None,
            product_type=None,
            product_policy=None,
            product_url=None,
            type=1,
            shipping_id=None
        )


def OpenCartProduct_from_dict(s: Any) -> OpenCartProduct:
    return OpenCartProduct.from_dict(s)


def OpenCartProduct_to_dict(x: OpenCartProduct) -> Any:
    return to_class(OpenCartProduct, x)
