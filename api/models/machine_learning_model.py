from mongoengine import Document
from mongoengine import IntField, StringField, ReferenceField, ListField, IntField, EmbeddedDocument, EmbeddedDocumentField, ImageField, FileField

class Model(Document):
    name = StringField()
    created_at = IntField()
    model_file = FileField()