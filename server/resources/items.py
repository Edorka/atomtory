from .models.items import TypeOfItem, Item
from flask import jsonify, request, abort
from . import api
from .models import db

@api.route('/types/', methods=['GET'])
def get_item_types():
    result = TypeOfItem.query.all()
    return jsonify(items = [ item.to_dict() for item in result ] )


@api.route('/items/', methods=['GET'])
def get_items_list():
    result = Item.query.all()
    return jsonify(items = [ item.to_dict() for item in result ] )


@api.route('/items/', methods=['POST'])
def add_to_items_list():
    new_record = Item()
    try:
        attrs = request.get_json(force=True)
        new_record.from_dict(attrs)
        db.session.add(new_record)
        db.session.commit()
        return jsonify(new_record.to_dict())
    except Exception, e:
        print e
        return abort(500)
