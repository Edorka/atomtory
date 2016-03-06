import unittest
from werkzeug.exceptions import BadRequest
from .test_client import TestClient
from app import create_app
from resources.models import db
from resources.models.items import TypeOfItem


class TestAPI(unittest.TestCase):

    def setUp(self):
        from settings import TestConfig
        self.app = create_app(TestConfig)
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.drop_all()
        db.create_all()
        db.session.commit()
        self.client = TestClient(self.app, '', '')
        self.catalog = self._get_catalog()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def _get_catalog(self, version='v1'):
        rv, json = self.client.get('/')
        return json['versions'][version]

    def test_add_items(self):
        testType = TypeOfItem()
        testType.from_dict({'id': 1, 'label': 'testing type'})
        db.session.add(testType)
        db.session.commit()
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'label': 'test one', 'type_id': testType.id})
        self.assertTrue(rv.status_code == 201)

    def test_add_items_insufficent(self):
        testType = TypeOfItem()
        testType.from_dict({'id': 1, 'label': 'testing type'})
        db.session.add(testType)
        db.session.commit()
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'label': '', 'type_id': testType.id})
        self.assertTrue(rv.status_code == 422)

    def _create_test_items(self):
        # create several items
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'label': 'test two', 'type_id': 1})
        print 'rv', rv, 'json', json
        self.assertTrue(rv.status_code == 201)
        one_url = json['Location']
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'name': 'two'})
        self.assertTrue(rv.status_code == 201)
        two_url = rv.headers['Location']
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'name': 'three'})
        self.assertTrue(rv.status_code == 201)
        three_url = rv.headers['Location']
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'name': 'four'})
        self.assertTrue(rv.status_code == 201)
        four_url = rv.headers['Location']
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'name': 'five'})
        self.assertTrue(rv.status_code == 201)
        five_url = rv.headers['Location']

        return [one_url, two_url, three_url, four_url, five_url]
