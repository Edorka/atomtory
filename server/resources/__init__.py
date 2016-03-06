from flask import Blueprint, url_for

api = Blueprint('api', __name__ , url_prefix='api')

def get_catalog():
    return {
        'types_url': url_for('api.get_item_types_list', _external=True),
        'items_url': url_for('api.get_items_list', _external=True)
    }

from . import items
assert items
