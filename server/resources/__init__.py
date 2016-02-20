from flask import Blueprint, url_for

api = Blueprint('api', __name__ , url_prefix='api')

def get_catalog():
    return {
        'items_url': url_for('api.get_items_list', _external=True)
    }

from . import items
assert items
