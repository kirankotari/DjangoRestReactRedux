import json
from urllib.request import urlopen

from django.conf import settings
from django.core.management import BaseCommand

from backendapp.models import Currency, Rate


class Command(BaseCommand):
    help = 'daily command to update exchange rates'

    def handle(self, *args, **options):

        url = 'https://openexchangerates.org/api/latest.json?app_id={key}'.format(key=settings.API_EXCHANGE_KEY)
        data = json.loads(urlopen(url).read())

        base, _created = Currency.objects.update_or_create(code='USD', defaults={'name': 'United States Dollar'})
        for code in settings.CODES:
            target, _created = Currency.objects.update_or_create(code=code)
            rate = data['rates'][code]
            Rate.objects.update_or_create(source=base, target=target, defaults={'rate': rate})