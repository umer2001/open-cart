# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = mvm_order_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Property:
    property: str
    property_value: str

    def __init__(self, property: str, property_value: str) -> None:
        self.property = property
        self.property_value = property_value

    @staticmethod
    def from_dict(obj: Any) -> 'Property':
        assert isinstance(obj, dict)
        property = from_str(obj.get("property"))
        property_value = from_str(obj.get("property_value"))
        return Property(property, property_value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["property"] = from_str(self.property)
        result["property_value"] = from_str(self.property_value)
        return result


class LineItem:
    custom_type: bool
    product_id: int
    variant_id: int
    price: str
    quantity: int
    requires_shipping: bool
    properties: List[Property]

    def __init__(self, custom_type: bool, product_id: int, variant_id: int, price: str, quantity: int, requires_shipping: bool, properties: List[Property]) -> None:
        self.custom_type = custom_type
        self.product_id = product_id
        self.variant_id = variant_id
        self.price = price
        self.quantity = quantity
        self.requires_shipping = requires_shipping
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'LineItem':
        assert isinstance(obj, dict)
        custom_type = from_bool(obj.get("custom_type"))
        product_id = int(from_str(obj.get("product_id")))
        variant_id = int(from_str(obj.get("variant_id")))
        price = from_str(obj.get("price"))
        quantity = int(from_str(obj.get("quantity")))
        requires_shipping = from_bool(obj.get("requires_shipping"))
        properties = from_list(Property.from_dict, obj.get("properties"))
        return LineItem(custom_type, product_id, variant_id, price, quantity, requires_shipping, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["custom_type"] = from_bool(self.custom_type)
        result["product_id"] = from_str(str(self.product_id))
        result["variant_id"] = from_str(str(self.variant_id))
        result["price"] = from_str(self.price)
        result["quantity"] = from_str(str(self.quantity))
        result["requires_shipping"] = from_bool(self.requires_shipping)
        result["properties"] = from_list(
            lambda x: to_class(Property, x), self.properties)
        return result


class ShopifyMultiVendorOrder:
    line_items: List[LineItem]
    tax_exempt: bool
    note: str
    customer_email: str
    shipping_line_title: str
    shipping_line_price: int

    def __init__(self, line_items: List[LineItem], tax_exempt: bool, note: str, customer_email: str, shipping_line_title: str, shipping_line_price: int) -> None:
        self.line_items = line_items
        self.tax_exempt = tax_exempt
        self.note = note
        self.customer_email = customer_email
        self.shipping_line_title = shipping_line_title
        self.shipping_line_price = shipping_line_price

    @staticmethod
    def from_dict(obj: Any) -> 'ShopifyMultiVendorOrder':
        assert isinstance(obj, dict)
        line_items = from_list(LineItem.from_dict, obj.get("line_items"))
        tax_exempt = from_bool(obj.get("tax_exempt"))
        note = from_str(obj.get("note"))
        customer_email = from_str(obj.get("customer_email"))
        shipping_line_title = from_str(obj.get("shipping_line_title"))
        shipping_line_price = int(from_str(obj.get("shipping_line_price")))
        return ShopifyMultiVendorOrder(line_items, tax_exempt, note, customer_email, shipping_line_title, shipping_line_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["line_items"] = from_list(
            lambda x: to_class(LineItem, x), self.line_items)
        result["tax_exempt"] = from_bool(self.tax_exempt)
        result["note"] = from_str(self.note)
        result["customer_email"] = from_str(self.customer_email)
        result["shipping_line_title"] = from_str(self.shipping_line_title)
        result["shipping_line_price"] = from_str(str(self.shipping_line_price))
        return result


def mvm_order_from_dict(s: Any) -> ShopifyMultiVendorOrder:
    return ShopifyMultiVendorOrder.from_dict(s)


def mvm_order_to_dict(x: ShopifyMultiVendorOrder) -> Any:
    return to_class(ShopifyMultiVendorOrder, x)
