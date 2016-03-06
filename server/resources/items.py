from .models.items import TypeOfItem, Item
from flask import jsonify, request, make_response
from flask.ext.restful import abort
import datetime
from . import api
from .models import db


@api.route('/types/', methods=['GET'])
def get_item_types_list():
    result = TypeOfItem.query.all()
    return jsonify(items = [ item.to_dict() for item in result ] )


@api.route('/items/<itemId>/', methods=['DELETE'])
def retrieve_item(itemId):
    item = Item.query.filter_by(id=itemId).first()
    if not item:
        abort (404, message='item not found')
    outdated = False
    if item.expires_at:
        outdated = item.expires_at < datetime.datetime.now().date()
    try:
        db.session.delete(item)
    except Exception, e:
        return make_response(jsonify(message='not possible to delete:'+e.message), 410)
    if not outdated:
        return jsonify({'message': 'item succesfully retrieved'})
    else:
        return make_response(jsonify(message='Cant retrieve: resource oudated'), 410)


@api.route('/items/', methods=['GET'])
def get_items_list():
    result = Item.query.all()
    return jsonify(items = [ item.to_dict() for item in result ] )



@api.route('/items/<item_id>/', methods=['GET'])
def get_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    return jsonify(item.to_dict())


@api.route('/items/', methods=['POST'])
def add_to_items_list():
    new_record = Item()
    try:
        attrs = request.get_json(force=True)
        new_record.from_dict(attrs)
        db.session.add(new_record)
        db.session.commit()
        return make_response(jsonify(Location=new_record.get_url()), 201)
    except Exception, e:
        return make_response(jsonify(message='Cant create: '+ e.message), 422)



