from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product, Filial, Characteristic, FilialPrice
from .serializers import ProductSerializer, FilialSerializer, CharacteristicSerializer, FilialPriceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class CharacteristicViewSet(viewsets.ModelViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer


class FilialPriceViewSet(viewsets.ModelViewSet):
    queryset = FilialPrice.objects.all()
    serializer_class = FilialPriceSerializer


class CatalogViewSet(viewsets.ViewSet):

    def list(self, request):
        filial_id = request.query_params.get('filial')
        products = Product.objects.all()

        data = []
        for product in products:
            try:
                filial_price = FilialPrice.objects.get(product_id=product.id, filial_id=filial_id)
                price = filial_price.price
            except FilialPrice.DoesNotExist:
                price = None

            serializer = ProductSerializer(product)
            data.append({
                'product_data': serializer.data,
                'price': price,
            })

        return Response(data)

    def retrieve(self, request, pk=None):
        filial_id = request.query_params.get('filial')
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)

        try:
            filial_price = FilialPrice.objects.get(product_id=product.id, filial_id=filial_id)
            price = filial_price.price
        except FilialPrice.DoesNotExist:
            price = None

        serializer = ProductSerializer(product)

        return Response({
            'product_data': serializer.data,
            'price': price,
        })

    @action(detail=True, methods=['get'])
    def price(self, request, pk=None):
        filial_id = request.query_params.get('filial')
        filial_price = FilialPrice.objects.get(product_id=pk, filial_id=filial_id)
        serializer = FilialPriceSerializer(filial_price)

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def characteristic(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        characteristics = Characteristic.objects.filter(product_id=pk)
        serializer = CharacteristicSerializer(characteristics, many=True)

        return Response(serializer.data)