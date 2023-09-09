from rest_framework import serializers
from .models import Product, Filial, Characteristic, FilialPrice


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = '__all__'


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class FilialPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilialPrice
        fields = '__all__'

