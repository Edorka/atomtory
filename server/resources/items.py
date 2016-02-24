from .models.items import TypeOfItem, Item
from flask import jsonify, request
from flask.ext.restful import abort
from . import api
from .models import db


@api.route('/types/', methods=['GET'])
def get_item_types():
    print 'listing'
    result = TypeOfItem.query.all()
    return jsonify(items = [ item.to_dict() for item in result ] )


@api.route('/items/<itemId>/', methods=['DELETE'])
def retrieve_item(itemId):
    item = Item.query.filter_by(id=itemId).first()
    print item
    if not item:
        print item
        abort (404, message='item not found')
    try:
        db.session.delete(item)
        return jsonify({'message': 'item succesfully retroeved'})
    except Exception, e:
        abort(500, message=e.message)


@api.route('/items/', methods=['GET'])
def get_items_list():
    print 'listing items'
    result = Item.query.all()
    return jsonify(items = [ item.to_dict() for item in result ] )


@api.route('/items/', methods=['POST'])
def add_to_items_list():
    print 'new'
    new_record = Item()
    try:
        attrs = request.get_json(force=True)
        new_record.from_dict(attrs)
        db.session.add(new_record)
        db.session.commit()
        return jsonify(new_record.to_dict())
    except Exception, e:
        print e
        abort(500, message=e.message)


