# -*- coding: utf-8 -*-
import datetime
from flask import url_for
from . import db
from sqlalchemy.orm import validates

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

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

    @validates('label')
    def validate_name(self, key, value):
        assert value != ''
        return value

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
        if 'expires_at' in data:
            try:
                expiration_str = data.get('expires_at')
                expiration =  datetime.datetime.strptime(expiration_str, DATE_FORMAT)
                self.expires_at = expiration
            except:
                pass

        elif 'decay' in data:
            try:
                decay = data.get('decay')
                decay_time = datetime.timedelta(seconds=decay)
                self.expires_at = self.created_at + decay_time
            except OverflowError:
                self.expires_at = None

    def get_url(self):
        return url_for('api.get_item', item_id=self.id,
                       _external=True)

    def __repr__(self):
        return '<Item %r>' % self.id

