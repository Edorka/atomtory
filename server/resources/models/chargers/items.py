# -*- coding: utf-8 -*-
from ..items import TypeOfItem, Item
DAYS = 60 * 60 * 24
YEARS = DAYS * 365
json_items = [
    {'label':'Uranio-235', 'decay': None},
    {'label':'Uranio-238', 'decay': None},
    {'label':'Potasio-40', 'decay': None},
    {'label':'Rubidio-87', 'decay': None},
    {'label':'Calcio-41', 'decay': None},
    {'label':'Carbono-14', 'decay': 5760 * YEARS},
    {'label':'Radio-22', 'decay': 61620 * YEARS},
    {'label':'Cesio-137', 'decay': 30.07 * YEARS},
    {'label':'Bismuto-207', 'decay': 31.55 * YEARS},
    {'label':'Estroncio-90', 'decay': 28.90 * YEARS},
    {'label':'Cobalto-60', 'decay': 5.271 * YEARS},
    {'label':'Cadmio-109', 'decay': 462.6 * DAYS},
    {'label':'Yodo-131', 'decay': 8.02 * DAYS},
    {'label':'Radón-222', 'decay': 3.82 * DAYS},
    {'label':'Oxígeno-15', 'decay': 122}
]

def load(db):
    db.create_all()
    radio_type = TypeOfItem()
    radio_type.from_dict({'label': 'Radio-Isótopo'})
    db.session.add(radio_type)
    db.session.commit()
    print "adding %i items" % len(json_items)
    for item in json_items:
        new_record = Item()
        new_record.from_dict(item)
        new_record.of_type = radio_type
        db.session.add(new_record)
        print new_record.to_dict()
    db.session.commit()
