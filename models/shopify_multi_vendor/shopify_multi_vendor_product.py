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
        if obj.get("sku") is not None:
            sku = from_str(obj.get("sku"))
        else:
            sku = None
        if obj.get("barcode") is not None:
            barcode = int(from_str(obj.get("barcode")))
        else:
            barcode = None
        if obj.get("weight") is not None:
            weight = float(from_str(obj.get("weight")))
        else:
            weight = None
        if obj.get("dimension") is not None:
            dimension = from_str(obj.get("dimension"))
        else:
            dimension = None
        if obj.get("price") is not None:
            price = from_str(obj.get("price"))
        else:
            price = None
        if obj.get("compare_at_price") is not None:
            compare_at_price = from_str(obj.get("compare_at_price"))
        else:
            compare_at_price = None
        if obj.get("handling_charges") is not None:
            handling_charges = from_str(obj.get("handling_charges"))
        else:
            handling_charges = None
        if obj.get("charge_taxes") is not None:
            charge_taxes = from_int(obj.get("charge_taxes"))
        else:
            charge_taxes = None
        if obj.get("require_shipping") is not None:
            require_shipping = int(from_str(obj.get("require_shipping")))
        else:
            require_shipping = None
        if obj.get("track_inventory") is not None:
            track_inventory = int(from_str(obj.get("track_inventory")))
        else:
            track_inventory = None
        if obj.get("quantity") is not None:
            quantity = int(from_str(obj.get("quantity")))
        else:
            quantity = None
        if obj.get("inventory_policy") is not None:
            inventory_policy = int(from_str(obj.get("inventory_policy")))
        else:
            inventory_policy = None
        if obj.get("inventory_locations") is not None:
            inventory_locations = from_list(
                MvmInventoryLocation.from_dict, obj.get("inventory_locations"))
        else:
            inventory_locations = []
        return MvmVariant(sku, barcode, weight, dimension, price, compare_at_price, handling_charges, charge_taxes, require_shipping, track_inventory, quantity, inventory_policy, inventory_locations)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.sku is not None:
            result["sku"] = from_str(self.sku)
        if self.barcode is not None:
            result["barcode"] = from_str(str(self.barcode))
        if self.weight is not None:
            result["weight"] = from_str(str(self.weight))
        if self.dimension is not None:
            result["dimension"] = from_str(self.dimension)
        if self.price is not None:
            result["price"] = from_str(self.price)
        if self.compare_at_price is not None:
            result["compare_at_price"] = from_str(self.compare_at_price)
        if self.handling_charges is not None:
            result["handling_charges"] = from_str(self.handling_charges)
        if self.charge_taxes is not None:
            result["charge_taxes"] = from_int(self.charge_taxes)
        if self.require_shipping is not None:
            result["require_shipping"] = from_str(str(self.require_shipping))
        if self.track_inventory is not None:
            result["track_inventory"] = from_str(str(self.track_inventory))
        if self.quantity is not None:
            result["quantity"] = from_str(str(self.quantity))
        if self.inventory_policy is not None:
            result["inventory_policy"] = from_str(str(self.inventory_policy))
        if self.inventory_locations is not None:
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
        if obj.get("seller_id") is not None:
            seller_id = int(from_str(obj.get("seller_id")))
        else:
            seller_id = None
        if obj.get("type") is not None:
            type = int(from_str(obj.get("type")))
        else:
            type = None
        if obj.get("product_name") is not None:
            product_name = from_str(obj.get("product_name"))
        else:
            product_name = None
        if obj.get("product_type") is not None:
            product_type = from_str(obj.get("product_type"))
        else:
            product_type = None
        if obj.get("product_tag") is not None:
            product_tag = from_str(obj.get("product_tag"))
        else:
            product_tag = None
        if obj.get("product_description") is not None:
            product_description = from_str(obj.get("product_description"))
        else:
            product_description = None
        if obj.get("handle") is not None:
            handle = from_str(obj.get("handle"))
        else:
            handle = None
        if obj.get("product_meta_info") is not None:
            product_meta_info = from_str(obj.get("product_meta_info"))
        else:
            product_meta_info = None
        if obj.get("product_policy") is not None:
            product_policy = from_str(obj.get("product_policy"))
        else:
            product_policy = None
        if obj.get("product_url") is not None:
            product_url = from_str(obj.get("product_url"))
        else:
            product_url = None
        if obj.get("expiry_date") is not None:
            expiry_date = from_str(obj.get("expiry_date"))
        else:
            expiry_date = None
        if obj.get("shipping_id") is not None:
            shipping_id = int(from_str(obj.get("shipping_id")))
        else:
            shipping_id = None
        if obj.get("variants") is not None:
            variants = from_list(MvmVariant.from_dict, obj.get("variants"))
        else:
            variants = []
        if obj.get("options") is not None:
            options = from_list(MvmOption.from_dict, obj.get("options"))
        else:
            options = []
        if obj.get("images") is not None:
            images = from_list(MvmImage.from_dict, obj.get("images"))
        else:
            images = []
        if obj.get("collections") is not None:
            collections = from_list(lambda x: int(
                from_str(x)), obj.get("collections"))
        else:
            collections = []
        return ShopifyMultiVendorProduct(seller_id, type, product_name, product_type, product_tag, product_description, handle, product_meta_info, product_policy, product_url, expiry_date, shipping_id, variants, options, images, collections)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.seller_id is not None:
            result["seller_id"] = from_str(str(self.seller_id))
        if self.type is not None:
            result["type"] = from_str(str(self.type))
        if self.product_name is not None:
            result["product_name"] = from_str(self.product_name)
        if self.product_type is not None:
            result["product_type"] = from_str(self.product_type)
        if self.product_tag is not None:
            result["product_tag"] = from_str(self.product_tag)
        if self.product_description is not None:
            result["product_description"] = from_str(self.product_description)
        if self.handle is not None:
            result["handle"] = from_str(self.handle)
        if self.product_meta_info is not None:
            result["product_meta_info"] = from_str(self.product_meta_info)
        if self.product_policy is not None:
            result["product_policy"] = from_str(self.product_policy)
        if self.product_url is not None:
            result["product_url"] = from_str(self.product_url)
        if self.expiry_date is not None:
            result["expiry_date"] = from_str(self.expiry_date)
        if self.shipping_id is not None:
            result["shipping_id"] = from_str(str(self.shipping_id))
        if self.variants is not None:
            result["variants"] = from_list(
                lambda x: to_class(MvmVariant, x), self.variants)
        if self.options is not None:
            result["options"] = from_list(
                lambda x: to_class(MvmOption, x), self.options)
        if self.images is not None:
            result["images"] = from_list(
                lambda x: to_class(MvmImage, x), self.images)
        if self.collections is not None:
            result["collections"] = from_list(lambda x: from_str(
                (lambda x: str(x))(x)), self.collections)
        return result


def mvm_product_from_dict(s: Any) -> ShopifyMultiVendorProduct:
    return ShopifyMultiVendorProduct.from_dict(s)


def mvm_product_to_dict(x: ShopifyMultiVendorProduct) -> Any:
    return to_class(ShopifyMultiVendorProduct, x)
