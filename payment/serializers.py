from rest_framework import serializers
from .models import SaleOrder


class SaleOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleOrder
        fields = '__all__'

