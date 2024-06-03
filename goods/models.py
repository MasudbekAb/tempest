from decimal import Decimal
from django.db import models
from ckeditor.fields import RichTextField
# from main.models import Media


class Aproduct(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ForeignKey("main.Media", on_delete=models.CASCADE, related_name="product_image")
    specifications = RichTextField(blank=True)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Discount %')

    def __str__(self):
        return self.title

class products(models.Model):
    short = models.CharField(max_length=200, blank=True)
    title = models.ForeignKey(Aproduct, on_delete=models.CASCADE, related_name="products_title")
    price = models.ForeignKey(Aproduct, on_delete=models.CASCADE, related_name="product_price")
    image = models.ForeignKey("main.Media", on_delete=models.CASCADE, related_name="products_image")

    def __str__(self):
        return self.title.title
