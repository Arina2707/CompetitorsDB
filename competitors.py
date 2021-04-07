from mongoengine import *


class Technology(EmbeddedDocument):
    sphere = IntField(required=True)
    tech = IntField(required=True)
    conference_presence = BooleanField()


class FirstProduct(EmbeddedDocument):
    energy = FloatField(required=True)
    wavelength = FloatField(required=True)


class SecondProduct(EmbeddedDocument):
    energy = FloatField(required=True)
    wavelength = FloatField(required=True)


class ThirdProductTech(EmbeddedDocument):
    energy = FloatField(required=True)
    wavelength = FloatField(required=True)


class ThirdProduct(EmbeddedDocument):
    avg_delivery = IntField(required=True)
    avg_price = IntField(required=True)
    technical = EmbeddedDocumentField(ThirdProductTech)


class Product(EmbeddedDocument):
    first_product = EmbeddedDocumentField(FirstProduct)
    second_product = EmbeddedDocumentField(SecondProduct)
    third_product = EmbeddedDocumentField(ThirdProduct)


class OrgValues(EmbeddedDocument):
    place = StringField(required=True)
    shares = StringField(required=True)
    cb_rank = FloatField()


class Competitor(Document):
    url = StringField(unique=True, required=True)
    competitor_name = StringField()
    technology = EmbeddedDocumentField(Technology)
    product = EmbeddedDocumentField(Product)
    org_vals = EmbeddedDocumentField(OrgValues)