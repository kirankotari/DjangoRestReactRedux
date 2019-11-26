from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics
from decimal import Decimal
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rate
from .serializer import RateSerializer


def convert(amount, base, rate):
    source = Rate.objects.get(target__code=base.value)
    target = Rate.objects.get(target__code=rate.value)
    return ((amount.value / source.rate) * target.rate).quantize(Decimal("0.00000001"))


class RatesViewSet(APIView):
    """
    Currency conversion.
    """

    def get(self, request):
        serializer = RateSerializer(data=request.query_params)

        if serializer.is_valid():
            result = convert(serializer['amount'], serializer['base'], serializer['rate'])
            return Response({'result': result})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)