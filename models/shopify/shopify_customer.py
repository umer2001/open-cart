from typing import Any, List, TypeVar, Type, cast, Callable


# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = shopify_customer_from_dict(json.loads(json_string))


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


class ShopifyAddress:
    address1: str
    address2: str
    city: str
    company: str
    country: str
    country_code: str
    first_name: str
    id: str
    last_name: str
    phone: str
    province: str
    province_code: str
    zip: str

    def __init__(self, address1: str, address2: str, city: str, company: str, country: str, country_code: str, first_name: str, id: str, last_name: str, phone: str, province: str, province_code: str, zip: str) -> None:
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.company = company
        self.country = country
        self.country_code = country_code
        self.first_name = first_name
        self.id = id
        self.last_name = last_name
        self.phone = phone
        self.province = province
        self.province_code = province_code
        self.zip = zip

    @staticmethod
    def from_dict(obj: Any) -> 'ShopifyAddress':
        assert isinstance(obj, dict)
        if obj.get("address1") is not None:
            address1 = from_str(obj.get("address1"))
        else:
            address1 = None
        if obj.get("address2") is not None:
            address2 = from_str(obj.get("address2"))
        else:
            address2 = None
        if obj.get("city") is not None:
            city = from_str(obj.get("city"))
        else:
            city = None
        if obj.get("company") is not None:
            company = from_str(obj.get("company"))
        else:
            company = None
        if obj.get("country") is not None:
            country = from_str(obj.get("country"))
        else:
            country = None
        if obj.get("countryCode") is not None:
            country_code = from_str(obj.get("countryCode"))
        else:
            country_code = None
        if obj.get("firstName") is not None:
            first_name = from_str(obj.get("firstName"))
        else:
            first_name = None
        if obj.get("id") is not None:
            id = from_str(obj.get("id"))
        else:
            id = None
        if obj.get("lastName") is not None:
            last_name = from_str(obj.get("lastName"))
        else:
            last_name = None
        if obj.get("phone") is not None:
            phone = from_str(obj.get("phone"))
        else:
            phone = None
        if obj.get("province") is not None:
            province = from_str(obj.get("province"))
        else:
            province = None
        if obj.get("provinceCode") is not None:
            province_code = from_str(obj.get("provinceCode"))
        else:
            province_code = None
        if obj.get("zip") is not None:
            zip = from_str(obj.get("zip"))
        else:
            zip = None
        return ShopifyAddress(address1, address2, city, company, country, country_code, first_name, id, last_name, phone, province, province_code, zip)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.address1 is not None:
            result["address1"] = from_str(self.address1)
        if self.address2 is not None:
            result["address2"] = from_str(self.address2)
        if self.city is not None:
            result["city"] = from_str(self.city)
        if self.company is not None:
            result["company"] = from_str(self.company)
        if self.country is not None:
            result["country"] = from_str(self.country)
        if self.country_code is not None:
            result["countryCode"] = from_str(self.country_code)
        if self.first_name is not None:
            result["firstName"] = from_str(self.first_name)
        if self.id is not None:
            result["id"] = from_str(self.id)
        if self.last_name is not None:
            result["lastName"] = from_str(self.last_name)
        if self.phone is not None:
            result["phone"] = from_str(self.phone)
        if self.province is not None:
            result["province"] = from_str(self.province)
        if self.province_code is not None:
            result["provinceCode"] = from_str(self.province_code)
        if self.zip is not None:
            result["zip"] = from_str(self.zip)
        return result


class Metafield:
    description: str
    id: str
    key: str
    namespace: str
    type: str
    value: str

    def __init__(self, description: str, id: str, key: str, namespace: str, type: str, value: str) -> None:
        self.description = description
        self.id = id
        self.key = key
        self.namespace = namespace
        self.type = type
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'Metafield':
        assert isinstance(obj, dict)
        if obj.get("description") is not None:
            description = from_str(obj.get("description"))
        else:
            description = None
        if obj.get("id") is not None:
            id = from_str(obj.get("id"))
        else:
            id = None
        if obj.get("key") is not None:
            key = from_str(obj.get("key"))
        else:
            key = None
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
        return Metafield(description, id, key, namespace, type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_str(self.description)
        if self.id is not None:
            result["id"] = from_str(self.id)
        if self.key is not None:
            result["key"] = from_str(self.key)
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
        if obj.get("value") is not None:
            value = from_str(obj.get("value"))
        if obj.get("valueType") is not None:
            value_type = from_str(obj.get("valueType"))
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
        if obj.get("namespace") is not None:
            namespace = from_str(obj.get("namespace"))
        if obj.get("owner") is not None:
            owner = from_str(obj.get("owner"))
        if obj.get("valueInput") is not None:
            value_input = ValueInput.from_dict(obj.get("valueInput"))
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


class SMSMarketingConsent:
    consent_updated_at: str
    marketing_opt_in_level: str
    marketing_state: str

    def __init__(self, consent_updated_at: str, marketing_opt_in_level: str, marketing_state: str) -> None:
        self.consent_updated_at = consent_updated_at
        self.marketing_opt_in_level = marketing_opt_in_level
        self.marketing_state = marketing_state

    @staticmethod
    def from_dict(obj: Any) -> 'SMSMarketingConsent':
        assert isinstance(obj, dict)
        if obj.get("consentUpdatedAt") is not None:
            consent_updated_at = from_str(obj.get("consentUpdatedAt"))
        if obj.get("marketingOptInLevel") is not None:
            marketing_opt_in_level = from_str(obj.get("marketingOptInLevel"))
        if obj.get("marketingState") is not None:
            marketing_state = from_str(obj.get("marketingState"))
        return SMSMarketingConsent(consent_updated_at, marketing_opt_in_level, marketing_state)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.consent_updated_at is not None:
            result["consentUpdatedAt"] = from_str(self.consent_updated_at)
        if self.marketing_opt_in_level is not None:
            result["marketingOptInLevel"] = from_str(
                self.marketing_opt_in_level)
        if self.marketing_state is not None:
            result["marketingState"] = from_str(self.marketing_state)
        return result


class ShopifyCustomer:
    accepts_marketing: bool
    accepts_marketing_updated_at: str
    addresses: List[ShopifyAddress]
    email: str
    first_name: str
    id: str
    last_name: str
    locale: str
    marketing_opt_in_level: str
    metafields: List[Metafield]
    note: str
    phone: str
    private_metafields: List[PrivateMetafield]
    sms_marketing_consent: SMSMarketingConsent
    tags: List[str]
    tax_exempt: bool
    tax_exemptions: List[str]

    def __init__(self, accepts_marketing: bool, accepts_marketing_updated_at: str, addresses: List[ShopifyAddress], email: str, first_name: str, id: str, last_name: str, locale: str, marketing_opt_in_level: str, metafields: List[Metafield], note: str, phone: str, private_metafields: List[PrivateMetafield], sms_marketing_consent: SMSMarketingConsent, tags: List[str], tax_exempt: bool, tax_exemptions: List[str]) -> None:
        self.accepts_marketing = accepts_marketing
        self.accepts_marketing_updated_at = accepts_marketing_updated_at
        self.addresses = addresses
        self.email = email
        self.first_name = first_name
        self.id = id
        self.last_name = last_name
        self.locale = locale
        self.marketing_opt_in_level = marketing_opt_in_level
        self.metafields = metafields
        self.note = note
        self.phone = phone
        self.private_metafields = private_metafields
        self.sms_marketing_consent = sms_marketing_consent
        self.tags = tags
        self.tax_exempt = tax_exempt
        self.tax_exemptions = tax_exemptions

    @staticmethod
    def from_dict(obj: Any) -> 'ShopifyCustomer':
        assert isinstance(obj, dict)
        if obj.get("acceptsMarketing") is not None:
            accepts_marketing = from_bool(obj.get("acceptsMarketing"))
        else:
            accepts_marketing = None
        if obj.get("acceptsMarketingUpdatedAt") is not None:
            accepts_marketing_updated_at = from_str(
                obj.get("acceptsMarketingUpdatedAt"))
        else:
            accepts_marketing_updated_at = None
        if obj.get("addresses") is not None:
            addresses = from_list(
                ShopifyAddress.from_dict, obj.get("addresses"))
        else:
            addresses = None
        if obj.get("email") is not None:
            email = from_str(obj.get("email"))
        else:
            email = None
        if obj.get("firstName") is not None:
            first_name = from_str(obj.get("firstName"))
        else:
            first_name = None
        if obj.get("id") is not None:
            id = from_str(obj.get("id"))
        else:
            id = None
        if obj.get("lastName") is not None:
            last_name = from_str(obj.get("lastName"))
        else:
            last_name = None
        if obj.get("locale") is not None:
            locale = from_str(obj.get("locale"))
        else:
            locale = None
        if obj.get("marketingOptInLevel") is not None:
            marketing_opt_in_level = from_str(obj.get("marketingOptInLevel"))
        else:
            marketing_opt_in_level = None
        if obj.get("metafields") is not None:
            metafields = from_list(Metafield.from_dict, obj.get("metafields"))
        else:
            metafields = []
        if obj.get("note") is not None:
            note = from_str(obj.get("note"))
        else:
            note = None
        if obj.get("phone") is not None:
            phone = from_str(obj.get("phone"))
        else:
            phone = None
        if obj.get("privateMetafields") is not None:
            private_metafields = from_list(
                PrivateMetafield.from_dict, obj.get("privateMetafields"))
        else:
            private_metafields = []
        if obj.get("smsMarketingConsent") is not None:
            sms_marketing_consent = SMSMarketingConsent.from_dict(
                obj.get("smsMarketingConsent"))
        else:
            sms_marketing_consent = None
        if obj.get("tags") is not None:
            tags = from_list(from_str, obj.get("tags"))
        else:
            tags = []
        if obj.get("taxExempt") is not None:
            tax_exempt = from_bool(obj.get("taxExempt"))
        else:
            tax_exempt = None
        if obj.get("taxExemptions") is not None:
            tax_exemptions = from_list(from_str, obj.get("taxExemptions"))
        else:
            tax_exemptions = []
        return ShopifyCustomer(accepts_marketing, accepts_marketing_updated_at, addresses, email, first_name, id, last_name, locale, marketing_opt_in_level, metafields, note, phone, private_metafields, sms_marketing_consent, tags, tax_exempt, tax_exemptions)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_str(self.id)
        if self.email is not None:
            result["email"] = from_str(self.email)
        if self.phone is not None:
            result["phone"] = from_str(self.phone)
        if self.first_name is not None:
            result["firstName"] = from_str(self.first_name)
        if self.last_name is not None:
            result["lastName"] = from_str(self.last_name)
        if self.locale is not None:
            result["locale"] = from_str(self.locale)
        if self.addresses is not None:
            result["addresses"] = from_list(
                lambda x: to_class(ShopifyAddress, x), self.addresses)
        if self.accepts_marketing is not None:
            result["acceptsMarketing"] = from_bool(self.accepts_marketing)
        if self.marketing_opt_in_level is not None:
            result["marketingOptInLevel"] = from_str(
                self.marketing_opt_in_level)
        if self.accepts_marketing_updated_at is not None:
            result["acceptsMarketingUpdatedAt"] = from_str(
                self.accepts_marketing_updated_at)
        if self.metafields is not None:
            result["metafields"] = from_list(
                lambda x: to_class(Metafield, x), self.metafields)
        if self.private_metafields is not None:
            result["privateMetafields"] = from_list(
                lambda x: to_class(PrivateMetafield, x), self.private_metafields)
        if self.sms_marketing_consent is not None:
            result["smsMarketingConsent"] = to_class(
                SMSMarketingConsent, self.sms_marketing_consent)
        if self.note is not None:
            result["note"] = from_str(self.note)
        if self.tags is not None:
            result["tags"] = from_list(from_str, self.tags)
        if self.tax_exempt is not None:
            result["taxExempt"] = from_bool(self.tax_exempt)
        if self.tax_exemptions is not None:
            result["taxExemptions"] = from_list(from_str, self.tax_exemptions)
        return result


def shopify_customer_from_dict(s: Any) -> ShopifyCustomer:
    return ShopifyCustomer.from_dict(s)


def shopify_customer_to_dict(x: ShopifyCustomer) -> Any:
    return to_class(ShopifyCustomer, x)
