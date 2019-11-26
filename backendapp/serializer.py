from django.contrib.auth.models import User
from rest_framework import serializers

from django.conf import settings


class RateSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=17, decimal_places=8, coerce_to_string=False, min_value=0)
    base = serializers.CharField()
    rate = serializers.CharField()

    def validate_base(self, value):
        if value not in settings.CODES:
            codes = ', '.join(settings.CODES)
            raise serializers.ValidationError('This field must be one of - {codes}'.format(codes=codes))
        return value

    def validate_rate(self, value):
        if value not in settings.CODES:
            codes = ', '.join(settings.CODES)
            raise serializers.ValidationError('This field must be one of - {codes}'.format(codes=codes))
        return value