from mongoengine import *


class Reviews(EmbeddedDocument):
    text = StringField(required=True)
    tonality = FloatField(required=True)
    score = IntField()


class Rank(EmbeddedDocument):
    overall_rank = IntField(required=True)
    reach_rank = IntField(required=True)
    rank_per_million = IntField(required=True)


class Views(EmbeddedDocument):
    pv_rank = IntField(required=True)
    pv_per_user = IntField(required=True)


class Customers(EmbeddedDocument):
    mentions_num = IntField(required=True)
    subscribers = ListField()
    rank = EmbeddedDocumentField(Rank)
    views = EmbeddedDocumentField(Views)


class CompetitorsCustomers(Document):
    url = ReferenceField('Competitor', dbref=False, reverse_delete_rule=0, required=True)
    customers = EmbeddedDocumentField(Customers)
    reviews = EmbeddedDocumentListField(Reviews)
