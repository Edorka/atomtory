from .models.items import TypeOfItem, Item
from flask import jsonify
from . import api


@api.route('/items/', methods=['GET'])
def get_items_list():
    result = Item.query.all()
    return jsonify(items = [ item.to_dict() for item in result ] )


