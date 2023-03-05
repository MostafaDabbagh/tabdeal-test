from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SaleOrderSerializer


class ChargeSellView(APIView):

    def post(self, request):
        ser_sale_order = SaleOrderSerializer(data=request.POST)
        if ser_sale_order.is_valid():
            ser_sale_order.save()
            return Response(data=ser_sale_order.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_sale_order.errors, status=status.HTTP_400_BAD_REQUEST)


