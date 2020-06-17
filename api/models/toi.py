from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField, EmbeddedDocument, EmbeddedDocumentField


class Electric_current(EmbeddedDocument):
    max_value = IntField()
    min_value = IntField()


class Eletric_meter(EmbeddedDocument):
    value = IntField()
    producer = StringField()
    year = StringField(max_length=4)
    series_number = StringField()
    property_number = StringField()
    tension = IntField()
    electric_currenturrent = EmbeddedDocumentField(Electric_current)
    const = IntField()
    read = IntField()
    meter_type = IntField()


class Toi(Document):
    # Dados da ligacao
    tariff_group = StringField(max_length=2, )
    measurement_type = StringField()
    number_elements = IntField()
    supply_type = IntField()

    # Dados da transformacao
    found_metter = EmbeddedDocumentField(Eletric_meter)
    installed_metter = EmbeddedDocumentField(Eletric_meter)
    comments = StringField()
