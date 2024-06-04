from decimal import Decimal
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User




class Aproduct(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ForeignKey("main.Media", on_delete=models.CASCADE, related_name="product_image")
    specifications = RichTextField(blank=True)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Discount %')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Aproduct, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Products(models.Model):
    short = models.CharField(max_length=200, blank=True)
    title = models.ForeignKey(Aproduct, on_delete=models.CASCADE, related_name="products_title")
    price = models.FloatField()  # Изменено на FloatField, так как у вас используется тип поля Float для цены
    image = models.ForeignKey("main.Media", on_delete=models.CASCADE, related_name="products_image")

    def __str__(self):
        return self.title.title

class Comment(models.Model):
    product = models.ForeignKey(Aproduct, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.title}'
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Aproduct, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.product.title}'


