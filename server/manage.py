#!/usr/bin/env python
from flask.ext.script import Manager
from app import create_app
from resources.models import db


manager = Manager(create_app)

@manager.command
def importdb(target=None, filename=None):
    if target == 'items':
        print 'loading initial dataset'
        from resources.models.chargers.items import load
        load(db)

@manager.command
def createdb():
    db.create_all()

if __name__ == '__main__':
    manager.run()
