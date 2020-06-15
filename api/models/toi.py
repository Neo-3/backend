from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField

class Toi(Document):
    tariffGroup = StringField(max_length=2, required=True, unique=True)


class Teste(Document):
    name = StringField(unique=True)
