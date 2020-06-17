from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField

class Teste(Document):
    name = StringField(unique=True)
