from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField, EmbeddedDocument, EmbeddedDocumentField, ImageField


class Seal(EmbeddedDocument):
    medition_box = ListField(IntField())
    meter_cover_kwh = IntField()
    meter_cover_kwah = IntField()
    terminal_box_cover = IntField()
    demand_port = IntField()
    measuarement_key = IntField()
    compartment_tcs_tps = ListField(IntField())


class Case(EmbeddedDocument):
    description = StringField()
    image = ImageField()


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
    # Dados da ligação
    tariff_group = StringField(max_length=2, )
    measurement_type = StringField()
    number_elements = IntField()
    supply_type = IntField()

    # Dados da transformacao
    found_metter = EmbeddedDocumentField(Eletric_meter)
    installed_metter = EmbeddedDocumentField(Eletric_meter)
    comments = StringField()

    # Análise da visita técnica
    technical_visit = EmbeddedDocumentField(Case)

    # Normalização
    normalization = EmbeddedDocumentField(Case)
    found_seal = EmbeddedDocument(Seal)
    installed_seal = EmbeddedDocument(Seal)
