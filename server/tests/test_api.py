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

    def test_list_item_types(self):
        testType = TypeOfItem()
        testType.from_dict({'id': 1, 'label': 'testing type'})
        db.session.add(testType)
        db.session.commit()
        rv, json = self.client.get(self.catalog['types_url'])
        self.assertTrue(rv.status_code == 200)
        #self.assertTrue(len(json.get('items')) == 1)
        #self.assertTrue(testType.__repr__ == '<Type 1>')


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
        self.assertTrue(rv.status_code == 201)
        one_url = json['Location']
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'label': 'two'})
        self.assertTrue(rv.status_code == 201)
        two_url = json['Location']
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'label': 'three'})
        self.assertTrue(rv.status_code == 201)
        three_url = json['Location']
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'label': 'four'})
        self.assertTrue(rv.status_code == 201)
        four_url = json['Location']
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'label': 'five'})
        self.assertTrue(rv.status_code == 201)
        five_url = json['Location']
        return [one_url, two_url, three_url, four_url, five_url]

    def test_list_items(self):
        urls = self._create_test_items();
        rv, json = self.client.get(self.catalog['items_url'])
        self.assertTrue(rv.status_code == 200)
        for item in json['items']:
            self.assertTrue(item['self_url'] in urls)
            print item['self_url']
            irv, ijson = self.client.get(item['self_url'])
            self.assertTrue(irv.status_code == 200)

    def test_delete_items(self):
        import datetime
        now = datetime.datetime.now()
        expired_date = now - datetime.timedelta(hours=24, seconds=15)
        rv, json = self.client.post(self.catalog['items_url'],
                                    data={'label': 'inmediate expire',
                                          'type_id': 1,
                                          'expires_at': expired_date.isoformat()})
        self.assertTrue(rv.status_code == 201)
        rv, json = self.client.delete(json['Location'])
        self.assertTrue(rv.status_code == 410)


