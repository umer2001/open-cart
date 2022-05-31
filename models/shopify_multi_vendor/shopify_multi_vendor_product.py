# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = mvm_product_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class MvmImage:
    image_url: str
    image_alt: str
    position: int
    image_attachment: str

    def __init__(self, image_url: str, image_alt: str, position: int, image_attachment: str) -> None:
        self.image_url = image_url
        self.image_alt = image_alt
        self.position = position
        self.image_attachment = image_attachment

    @staticmethod
    def from_dict(obj: Any) -> 'MvmImage':
        assert isinstance(obj, dict)
        image_url = from_str(obj.get("image_url"))
        image_alt = from_str(obj.get("image_alt"))
        position = int(from_str(obj.get("position")))
        image_attachment = from_str(obj.get("image_attachment"))
        return MvmImage(image_url, image_alt, position, image_attachment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_url"] = from_str(self.image_url)
        result["image_alt"] = from_str(self.image_alt)
        result["position"] = from_str(str(self.position))
        result["image_attachment"] = from_str(self.image_attachment)
        return result


class MvmOption:
    name: str
    values: str

    def __init__(self, name: str, values: str) -> None:
        self.name = name
        self.values = values

    @staticmethod
    def from_dict(obj: Any) -> 'MvmOption':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        values = from_str(obj.get("values"))
        return MvmOption(name, values)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["values"] = from_str(self.values)
        return result


class MvmInventoryLocation:
    location_id: int
    variant_quantity: int

    def __init__(self, location_id: int, variant_quantity: int) -> None:
        self.location_id = location_id
        self.variant_quantity = variant_quantity

    @staticmethod
    def from_dict(obj: Any) -> 'MvmInventoryLocation':
        assert isinstance(obj, dict)
        location_id = int(from_str(obj.get("location_id")))
        variant_quantity = int(from_str(obj.get("variant_quantity")))
        return MvmInventoryLocation(location_id, variant_quantity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["location_id"] = from_str(str(self.location_id))
        result["variant_quantity"] = from_str(str(self.variant_quantity))
        return result


class MvmVariant:
    sku: str
    barcode: int
    weight: int
    dimension: str
    price: str
    compare_at_price: str
    handling_charges: str
    charge_taxes: int
    require_shipping: int
    track_inventory: int
    quantity: int
    inventory_policy: int
    inventory_locations: List[MvmInventoryLocation]

    def __init__(self, sku: str, barcode: int, weight: int, dimension: str, price: str, compare_at_price: str, handling_charges: str, charge_taxes: int, require_shipping: int, track_inventory: int, quantity: int, inventory_policy: int, inventory_locations: List[MvmInventoryLocation]) -> None:
        self.sku = sku
        self.barcode = barcode
        self.weight = weight
        self.dimension = dimension
        self.price = price
        self.compare_at_price = compare_at_price
        self.handling_charges = handling_charges
        self.charge_taxes = charge_taxes
        self.require_shipping = require_shipping
        self.track_inventory = track_inventory
        self.quantity = quantity
        self.inventory_policy = inventory_policy
        self.inventory_locations = inventory_locations

    @staticmethod
    def from_dict(obj: Any) -> 'MvmVariant':
        assert isinstance(obj, dict)
        sku = from_str(obj.get("sku"))
        barcode = int(from_str(obj.get("barcode")))
        weight = int(from_str(obj.get("weight")))
        dimension = from_str(obj.get("dimension"))
        price = from_str(obj.get("price"))
        compare_at_price = from_str(obj.get("compare_at_price"))
        handling_charges = from_str(obj.get("handling_charges"))
        charge_taxes = from_int(obj.get("charge_taxes"))
        require_shipping = int(from_str(obj.get("require_shipping")))
        track_inventory = int(from_str(obj.get("track_inventory")))
        quantity = int(from_str(obj.get("quantity")))
        inventory_policy = int(from_str(obj.get("inventory_policy")))
        inventory_locations = from_list(
            MvmInventoryLocation.from_dict, obj.get("inventory_locations"))
        return MvmVariant(sku, barcode, weight, dimension, price, compare_at_price, handling_charges, charge_taxes, require_shipping, track_inventory, quantity, inventory_policy, inventory_locations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sku"] = from_str(self.sku)
        result["barcode"] = from_str(str(self.barcode))
        result["weight"] = from_str(str(self.weight))
        result["dimension"] = from_str(self.dimension)
        result["price"] = from_str(self.price)
        result["compare_at_price"] = from_str(self.compare_at_price)
        result["handling_charges"] = from_str(self.handling_charges)
        result["charge_taxes"] = from_int(self.charge_taxes)
        result["require_shipping"] = from_str(str(self.require_shipping))
        result["track_inventory"] = from_str(str(self.track_inventory))
        result["quantity"] = from_str(str(self.quantity))
        result["inventory_policy"] = from_str(str(self.inventory_policy))
        result["inventory_locations"] = from_list(
            lambda x: to_class(MvmInventoryLocation, x), self.inventory_locations)
        return result


class ShopifyMultiVendorProduct:
    seller_id: int
    type: int
    product_name: str
    product_type: str
    product_tag: str
    product_description: str
    handle: str
    product_meta_info: str
    product_policy: str
    product_url: str
    expiry_date: str
    shipping_id: int
    variants: List[MvmVariant]
    options: List[MvmOption]
    images: List[MvmImage]
    collections: List[int]

    def __init__(self, seller_id: int, type: int, product_name: str, product_type: str, product_tag: str, product_description: str, handle: str, product_meta_info: str, product_policy: str, product_url: str, expiry_date: str, shipping_id: int, variants: List[MvmVariant], options: List[MvmOption], images: List[MvmImage], collections: List[int]) -> None:
        self.seller_id = seller_id
        self.type = type
        self.product_name = product_name
        self.product_type = product_type
        self.product_tag = product_tag
        self.product_description = product_description
        self.handle = handle
        self.product_meta_info = product_meta_info
        self.product_policy = product_policy
        self.product_url = product_url
        self.expiry_date = expiry_date
        self.shipping_id = shipping_id
        self.variants = variants
        self.options = options
        self.images = images
        self.collections = collections

    @staticmethod
    def from_dict(obj: Any) -> 'ShopifyMultiVendorProduct':
        assert isinstance(obj, dict)
        seller_id = int(from_str(obj.get("seller_id")))
        type = int(from_str(obj.get("type")))
        product_name = from_str(obj.get("product_name"))
        product_type = from_str(obj.get("product_type"))
        product_tag = from_str(obj.get("product_tag"))
        product_description = from_str(obj.get("product_description"))
        handle = from_str(obj.get("handle"))
        product_meta_info = from_str(obj.get("product_meta_info"))
        product_policy = from_str(obj.get("product_policy"))
        product_url = from_str(obj.get("product_url"))
        expiry_date = from_str(obj.get("expiry_date"))
        shipping_id = int(from_str(obj.get("shipping_id")))
        variants = from_list(MvmVariant.from_dict, obj.get("variants"))
        options = from_list(MvmOption.from_dict, obj.get("options"))
        images = from_list(MvmImage.from_dict, obj.get("images"))
        collections = from_list(lambda x: int(
            from_str(x)), obj.get("collections"))
        return ShopifyMultiVendorProduct(seller_id, type, product_name, product_type, product_tag, product_description, handle, product_meta_info, product_policy, product_url, expiry_date, shipping_id, variants, options, images, collections)

    def to_dict(self) -> dict:
        result: dict = {}
        result["seller_id"] = from_str(str(self.seller_id))
        result["type"] = from_str(str(self.type))
        result["product_name"] = from_str(self.product_name)
        result["product_type"] = from_str(self.product_type)
        result["product_tag"] = from_str(self.product_tag)
        result["product_description"] = from_str(self.product_description)
        result["handle"] = from_str(self.handle)
        result["product_meta_info"] = from_str(self.product_meta_info)
        result["product_policy"] = from_str(self.product_policy)
        result["product_url"] = from_str(self.product_url)
        result["expiry_date"] = from_str(self.expiry_date)
        result["shipping_id"] = from_str(str(self.shipping_id))
        result["variants"] = from_list(
            lambda x: to_class(MvmVariant, x), self.variants)
        result["options"] = from_list(
            lambda x: to_class(MvmOption, x), self.options)
        result["images"] = from_list(
            lambda x: to_class(MvmImage, x), self.images)
        result["collections"] = from_list(lambda x: from_str(
            (lambda x: str(x))(x)), self.collections)
        return result


def mvm_product_from_dict(s: Any) -> ShopifyMultiVendorProduct:
    return ShopifyMultiVendorProduct.from_dict(s)


def mvm_product_to_dict(x: ShopifyMultiVendorProduct) -> Any:
    return to_class(ShopifyMultiVendorProduct, x)
