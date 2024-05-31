from django.db import models
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    specifications = RichTextField(blank=True)

    def __str__(self):
        return self.title
    

