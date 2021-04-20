from mongoengine import *


class Reviews(EmbeddedDocument):
    text = StringField()
    tonality_score = FloatField(required=True)
    positive_percent = FloatField(required=True)


class Rank(EmbeddedDocument):
    overall_rank = FloatField(required=True)
    reach_rank = FloatField(required=True)
    rank_per_million = FloatField(required=True)


class Views(EmbeddedDocument):
    pv_rank = IntField(required=True)
    pv_per_user = IntField(required=True)


class Customers(EmbeddedDocument):
    mentions_num = IntField(required=True)
    rank = EmbeddedDocumentField(Rank)
    views = EmbeddedDocumentField(Views)


class CompetitorsCustomers(Document):
    url = ReferenceField('Competitors', dbref=False, required=True, reverse_delete_rule=CASCADE)
    customers = EmbeddedDocumentField(Customers)
    reviews = EmbeddedDocumentListField(Reviews)
