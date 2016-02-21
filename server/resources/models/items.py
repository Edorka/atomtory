# -*- coding: utf-8 -*-
import datetime
from . import db


class TypeOfItem(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.UnicodeText(20))

    def to_dict(self):
        return {
            'id': self.id,
            'label': self.label
        }

    def from_dict(self, data):
        if 'id' in data:
            self.id = data.get('id')
        self.label = unicode(data.get('label'), "utf-8")

    def __repr__(self):
        return '<Type %r>' % self.id


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.UnicodeText(50))
    created_at = db.Column(db.Date, default=datetime.datetime.now)
    expires_at = db.Column(db.Date)
    type_id = db.Column(db.Integer,
                        db.ForeignKey('types.id'))
    of_type = db.relationship('TypeOfItem',
                           foreign_keys=[type_id],
                              backref=db.backref('products', lazy='dynamic'))

    def to_dict(self):
        return {
            'id': self.id,
            'label': self.label,
            'type': self.of_type.to_dict() if self.of_type else None,
            'created_at': str(self.created_at),
            'expires_at': str(self.expires_at)
        }

    def from_dict(self, data):
        self.id = data.get('id')
        self.label = data.get('label')
        self.type_id = data.get('type_id')
        self.created_at = datetime.datetime.now()
        decay = data.get('decay', None)
        if decay:
            try:
                decay_time = datetime.timedelta(seconds=decay)
                self.expires_at = self.created_at + decay_time
            except OverflowError:
                self.expires_at = None


    def __repr__(self):
        return '<Item %r>' % self.id

