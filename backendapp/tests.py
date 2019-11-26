from django.test import TestCase
from itertools import combinations_with_replacement
from django.conf import settings
from django.core.management import call_command
from rest_framework.test import APIClient


class CurrencyTestCase(TestCase):
    def setUp(self):
        call_command('update_rates')
        self.client = APIClient()

    def test_all_rates(self):

        for base, rate in combinations_with_replacement(settings.CURRENCY_CODES, 2):
            response = self.client.get('/rates', data={
                'amount': 1, 'base': base, 'rate': rate
            })
            assert response.status_code == 200

    def test_non_existing_rates(self):

        FAKE_CURRENCY_CODES = ['KZT', 'GHGHHG']
        for base, rate in combinations_with_replacement(FAKE_CURRENCY_CODES, 2):
            response = self.client.get('/rates', data={
                'amount': 1, 'base': base, 'rate': rate
            })
            assert response.status_code == 400

    def test_big_amount(self):
        amount = 1000000000
        for base, rate in combinations_with_replacement(settings.CURRENCY_CODES, 2):
            response = self.client.get('/rates', data={
                'amount': amount, 'base': base, 'rate': rate
            })
            assert response.status_code == 400

    def test_nan_amount(self):
        amount = 'string'
        for base, rate in combinations_with_replacement(settings.CURRENCY_CODES, 2):
            response = self.client.get('/rates', data={
                'amount': amount, 'base': base, 'rate': rate
            })
            assert response.status_code == 400

    def test_negative_amount(self):
        amount = -10
        for base, rate in combinations_with_replacement(settings.CURRENCY_CODES, 2):
            response = self.client.get('/rates', data={
                'amount': amount, 'base': base, 'rate': rate
            })
            assert response.status_code == 400

    def test_zero_amount(self):
        amount = 0
        for base, rate in combinations_with_replacement(settings.CURRENCY_CODES, 2):
            response = self.client.get('/rates', data={
                'amount': amount, 'base': base, 'rate': rate
            })
            assert response.status_code == 200

    def test_wrong_parameters(self):
        response = self.client.get('/rates')
        assert response.status_code == 400

    def test_same_base_target(self):

        SAME_CODES = [(i, i) for i in settings.CURRENCY_CODES]

        for base, rate in SAME_CODES:
            response = self.client.get('/rates', data={
                'amount': 1, 'base': base, 'rate': rate
            })
            self.assertEqual(response.data['result'], 1)