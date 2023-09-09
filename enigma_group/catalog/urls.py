from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, FilialViewSet, CharacteristicViewSet, FilialPriceViewSet, CatalogViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'filials', FilialViewSet)
router.register(r'characteristics', CharacteristicViewSet)
router.register(r'filial_prices', FilialPriceViewSet)
router.register(r'catalog', CatalogViewSet, basename='catalog')

urlpatterns = [
    path('', include(router.urls)),
]