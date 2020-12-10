from rest_framework import serializers
from stocks.models import Stock


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ("id", "title", 'stock_count')
