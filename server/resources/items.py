from .models.items import TypeOfItem, Item
from flask import jsonify, request, make_response
from flask.ext.restful import abort
import datetime
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
    if not item:
        abort (404, message='item not found')
    outdated = item.expire_date > datetime.now()
    try:
        db.session.delete(item)
    except Exception, e:
        print e
        abort(501, message=e.message)
    if not outdated:
        return jsonify({'message': 'item succesfully retroeved'})
    else:
        response = jsonify({'message': 'resource outdated'})
        response.status_code = 410
        return response


@api.route('/items/', methods=['GET'])
def get_items_list():
    result = Item.query.all()
    return jsonify(items = [ item.to_dict() for item in result ] )



@api.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = itemItem.query.filter_by(id=itemId).first()
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
        print 'error', e
        abort(422, message='cant create')



