from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='name')

    def get_price_for_filial(self, filial_id):
        try:
            filial_price = FilialPrice.objects.get(product_id=self.id, filial_id=filial_id)
            return filial_price.price
        except FilialPrice.DoesNotExist:
            return None


class Filial(models.Model):
    name = models.CharField(verbose_name='name')
    region = models.IntegerField(verbose_name='region')


class Characteristic(models.Model):
    self_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(verbose_name='name')
    product_id = models.ManyToManyField(Product)


class FilialPrice(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    filial_id = models.ForeignKey(Filial, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='price')