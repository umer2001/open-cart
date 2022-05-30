# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = open_cart_customer_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast
from dateutil import parser
from models.shopify.shopify_customer import Metafield, ShopifyAddress, ShopifyCustomer

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
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


class OpenCartAddress:
    address_id: int
    customer_id: int
    firstname: str
    lastname: str
    company: str
    address_1: str
    address_2: str
    postcode: str
    city: str
    zone_id: int
    zone: str
    zone_code: str
    country_id: int
    country: str
    iso_code_2: str
    iso_code_3: str
    address_format: str
    custom_field: None

    def __init__(self, address_id: int, customer_id: int, firstname: str, lastname: str, company: str, address_1: str, address_2: str, postcode: str, city: str, zone_id: int, zone: str, zone_code: str, country_id: int, country: str, iso_code_2: str, iso_code_3: str, address_format: str, custom_field: None) -> None:
        self.address_id = address_id
        self.customer_id = customer_id
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address_1 = address_1
        self.address_2 = address_2
        self.postcode = postcode
        self.city = city
        self.zone_id = zone_id
        self.zone = zone
        self.zone_code = zone_code
        self.country_id = country_id
        self.country = country
        self.iso_code_2 = iso_code_2
        self.iso_code_3 = iso_code_3
        self.address_format = address_format
        self.custom_field = custom_field

    @staticmethod
    def from_dict(obj: Any) -> 'OpenCartAddress':
        assert isinstance(obj, dict)
        address_id = int(from_str(obj.get("address_id")))
        customer_id = int(from_str(obj.get("customer_id")))
        firstname = from_str(obj.get("firstname"))
        lastname = from_str(obj.get("lastname"))
        company = from_str(obj.get("company"))
        address_1 = from_str(obj.get("address_1"))
        address_2 = from_str(obj.get("address_2"))
        postcode = from_str(obj.get("postcode"))
        city = from_str(obj.get("city"))
        zone_id = int(from_str(obj.get("zone_id")))
        zone = from_str(obj.get("zone"))
        zone_code = from_str(obj.get("zone_code"))
        country_id = int(from_str(obj.get("country_id")))
        country = from_str(obj.get("country"))
        iso_code_2 = from_str(obj.get("iso_code_2"))
        iso_code_3 = from_str(obj.get("iso_code_3"))
        address_format = from_str(obj.get("address_format"))
        custom_field = []
        return OpenCartAddress(address_id, customer_id, firstname, lastname, company, address_1, address_2, postcode, city, zone_id, zone, zone_code, country_id, country, iso_code_2, iso_code_3, address_format, custom_field)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.address_id is not None:
            result["address_id"] = from_str(str(self.address_id))
        if self.customer_id is not None:
            result["customer_id"] = from_str(str(self.customer_id))
        if self.firstname is not None:
            result["firstname"] = from_str(self.firstname)
        if self.lastname is not None:
            result["lastname"] = from_str(self.lastname)
        if self.company is not None:
            result["company"] = from_str(self.company)
        if self.address_1 is not None:
            result["address_1"] = from_str(self.address_1)
        if self.address_2 is not None:
            result["address_2"] = from_str(self.address_2)
        if self.postcode is not None:
            result["postcode"] = from_str(self.postcode)
        if self.city is not None:
            result["city"] = from_str(self.city)
        if self.zone_id is not None:
            result["zone_id"] = from_str(str(self.zone_id))
        if self.zone is not None:
            result["zone"] = from_str(self.zone)
        if self.zone_code is not None:
            result["zone_code"] = from_str(self.zone_code)
        if self.country_id is not None:
            result["country_id"] = from_str(str(self.country_id))
        if self.country is not None:
            result["country"] = from_str(self.country)
        if self.iso_code_2 is not None:
            result["iso_code_2"] = from_str(self.iso_code_2)
        if self.iso_code_3 is not None:
            result["iso_code_3"] = from_str(self.iso_code_3)
        if self.address_format is not None:
            result["address_format"] = from_str(self.address_format)
        if self.custom_field is not None:
            result["custom_field"] = from_none(self.custom_field)
        return result


class OpenCartCustomer:
    customer_id: int
    customer_group_id: int
    name: str
    email: str
    newsletter: int
    status: int
    approved: str
    safe: int
    ip: str
    reward_points: int
    account_custom_field: None
    custom_fields: List[Any]
    addresses: List[OpenCartAddress]
    date_added: str

    def __init__(self, customer_id: int, customer_group_id: int, name: str, email: str, newsletter: int, status: int, approved: str, safe: int, ip: str, reward_points: int, account_custom_field: None, custom_fields: List[Any], addresses: List[OpenCartAddress], date_added: str) -> None:
        self.customer_id = customer_id
        self.customer_group_id = customer_group_id
        self.name = name
        self.email = email
        self.newsletter = newsletter
        self.status = status
        self.approved = approved
        self.safe = safe
        self.ip = ip
        self.reward_points = reward_points
        self.account_custom_field = account_custom_field
        self.custom_fields = custom_fields
        self.addresses = addresses
        self.date_added = date_added

    @staticmethod
    def from_dict(obj: Any) -> 'OpenCartCustomer':
        assert isinstance(obj, dict)
        if obj.get("customer_id") is not None:
            customer_id = int(from_str(obj.get("customer_id")))
        else:
            customer_id = None
        if obj.get("customer_group_id") is not None:
            customer_group_id = int(from_str(obj.get("customer_group_id")))
        else:
            customer_group_id = None
        if obj.get("name") is not None:
            name = from_str(obj.get("name"))
        else:
            name = None
        if obj.get("email") is not None:
            email = from_str(obj.get("email"))
        else:
            email = None
        if obj.get("newsletter") is not None:
            newsletter = int(from_str(obj.get("newsletter")))
        else:
            newsletter = None
        if obj.get("status") is not None:
            status = int(from_str(obj.get("status")))
        else:
            status = None
        if obj.get("approved") is not None:
            approved = from_str(obj.get("approved"))
        else:
            approved = None
        if obj.get("safe") is not None:
            safe = int(from_str(obj.get("safe")))
        else:
            safe = None
        if obj.get("ip") is not None:
            ip = from_str(obj.get("ip"))
        else:
            ip = None
        if obj.get("reward_points") is not None:
            reward_points = from_int(obj.get("reward_points"))
        else:
            reward_points = None
        if obj.get("account_custom_field") is not None:
            # account_custom_field = from_none(obj.get("account_custom_field"))
            account_custom_field = []
        else:
            account_custom_field = None
        if obj.get("custom_fields") is not None:
            custom_fields = from_list(lambda x: x, obj.get("custom_fields"))
        else:
            custom_fields = []
        if obj.get("addresses") is not None:
            addresses = from_list(
                OpenCartAddress.from_dict, obj.get("addresses"))
        else:
            addresses = []
        if obj.get("date_added") is not None:
            date_added = from_str(obj.get("date_added"))
        else:
            date_added = None
        return OpenCartCustomer(customer_id, customer_group_id, name, email, newsletter, status, approved, safe, ip, reward_points, account_custom_field, custom_fields, addresses, date_added)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.customer_id is not None:
            result["customer_id"] = from_str(str(self.customer_id))
        if self.customer_group_id is not None:
            result["customer_group_id"] = from_str(str(self.customer_group_id))
        if self.name is not None:
            result["name"] = from_str(self.name)
        if self.email is not None:
            result["email"] = from_str(self.email)
        if self.newsletter is not None:
            result["newsletter"] = from_str(str(self.newsletter))
        if self.status is not None:
            result["status"] = from_str(str(self.status))
        if self.approved is not None:
            result["approved"] = from_str(self.approved)
        if self.safe is not None:
            result["safe"] = from_str(str(self.safe))
        if self.ip is not None:
            result["ip"] = from_str(self.ip)
        if self.reward_points is not None:
            result["reward_points"] = from_int(self.reward_points)
        if self.account_custom_field is not None:
            result["account_custom_field"] = from_none(
                self.account_custom_field)
        if self.custom_fields is not None:
            result["custom_fields"] = from_list(
                lambda x: x, self.custom_fields)
        if self.addresses is not None:
            result["addresses"] = from_list(
                lambda x: to_class(OpenCartAddress, x), self.addresses)
        if self.date_added is not None:
            result["date_added"] = from_str(self.date_added)
        return result

    def to_shopify_customer(self) -> ShopifyCustomer:
        if self.date_added == "30/11/-0001":
            date = parser.parse("30/11/2001")
        else:
            date = parser.parse(self.date_added)

        return ShopifyCustomer(
            id=None,
            # id=f"gid://shopify/Customer/{self.customer_id}",
            first_name=self.name.split(" ")[0],
            last_name=self.name.split(" ")[1],
            email=self.email,
            accepts_marketing=self.newsletter == 1,
            addresses=[
                ShopifyAddress(
                    # id=f"gid://shopify/MailingAddress/{adres.address_id}?model_name=CustomerOpenCartAddress",
                    id=None,
                    first_name=adres.firstname,
                    last_name=adres.lastname,
                    address1=adres.address_1,
                    address2=adres.address_2,
                    city=adres.city,
                    country=adres.country,
                    company=adres.company,
                    country_code=None,
                    province=adres.zone,
                    province_code=adres.zone_code,
                    zip=adres.postcode,
                    phone=None,
                ) for adres in self.addresses
            ],
            metafields=[
                Metafield(
                    # id="gid://shopify/Metafield/444",
                    id=None,
                    key="customer_ip",
                    value=self.ip,
                    description="Customer IP",
                    namespace="customer_ip",
                    type="single_line_text_field",
                ),
                Metafield(
                    # id="gid://shopify/Metafield/111",
                    id=None,
                    key="customer_date_added",
                    value=date.isoformat(),
                    description="Customer Date Added",
                    namespace="customer_date_added",
                    type="date",
                )
            ],
            locale=None,
            tags=[],
            note=None,
            phone=None,
            accepts_marketing_updated_at=None,
            tax_exempt=None,
            tax_exemptions=None,
            marketing_opt_in_level=None,
            private_metafields=[],
            sms_marketing_consent=None,
        )


def open_cart_customer_from_dict(s: Any) -> OpenCartCustomer:
    return OpenCartCustomer.from_dict(s)


def open_cart_customer_to_dict(x: OpenCartCustomer) -> Any:
    return to_class(OpenCartCustomer, x)
