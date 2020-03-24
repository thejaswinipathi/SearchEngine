from django.test import TestCase
from rest_framework.test import RequestsClient
import json
from book import scripts


class BookFetchTestCase(TestCase):

    def setUp(self):
        scripts.populate_data_test()

    def test_task_one_api_test_one(self):
        client = RequestsClient()
        content = {
            "query": "thejaswini pathi",
            "k": 3,
        }
        response = client.post('http://127.0.0.1:8000/book/getInfo/', content)
        data = json.loads(response.text)
        self.assertEqual(len(data), 0)

    def test_task_one_api_test_two(self):
        client = RequestsClient()
        content = {
            "query": "meditation",
            "k":3
        }
        response = client.post('http://127.0.0.1:8000/book/getInfo/', content)
        data = json.loads(response.text)
        self.assertEqual(len(data), 1)

    def test_task_one_api_test_three(self):
        client = RequestsClient()
        content = {
            "queries": ["my life change", "i love coding"],
            "k":3
        }
        response = client.post('http://127.0.0.1:8000/book/getInfoList/', json = content)
        data = json.loads(response.text)
        self.assertEqual(len(data), 2)
