from unittest import TestCase

import requests


class FillCellTestCase(TestCase):

    def test_Route(self):
        response = requests.get('http://localhost:5000/fill_cell')
        self.assertEqual(response.status_code, 200)
