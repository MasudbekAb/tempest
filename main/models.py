from email.mime import image
from os import name
from django.db import models
from goods.models import Product
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _("Image")
        VIDEO = 'video', _("Video")
        DOCUMENT = 'document', _("document")
        GIF = 'gif', _("Gif")
        OTHER = 'other', _("Other")

    file = models.FileField(upload_to='media/',
                            verbose_name=_("File"),
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi',
                                                                                   'mov', 'gif', 'webp', 'pdf', 'doc',
                                                                                   'docx', 'mpeg'])])
    file_type = models.CharField(max_length=10, verbose_name=_("File Type"),
                                 choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        # E:\Azamat Python\1 month\1 lesson\main.py
        element = r"""[\]"""
        return f'Id: {self.id}|Name: {self.file.name.split(element)[-1]}'

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'avi', 'mov', 'mpeg']:
                raise ValidationError(_("Invalid Video File"))



class Carousel(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='carousel_image')
    price = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carousel_price')
    title = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carousel_title')
    short_desc = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.title.name
    

class Short_products(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='sh_product_image')
    title = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sh_title')
    price = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sh_price')


    def __str__(self):
        return self.title
    

#TODO: code foreign key for comments



class Nums(models.Model):
    creativity = models.IntegerField()
    clients = User.objects.count()
    products = Product.objects.count()
    hours = models.IntegerField()

    def __str__(self):
        return 'Nums'


class Footer(models.Model):
    content = models.TextField()

    def __str__(self):
        return 'Footer'


class Pluses(models.Model):
    card = models.CharField(max_length=200)
    money = models.CharField(max_length=200)
    delivery = models.CharField(max_length=200)

    def __str__(self):
        return 'Pluses'



class Info(models.Model):
    history = models.TextField()
    mission = models.TextField()
    image = models.ForeignKey(Media,on_delete=models.CASCADE,related_name='about_image')

    def __str__(self):
        return 'Info'
    

class TeamInfo(models.Model):
    desc = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return 'TeamInfo'
    

class Team(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='team_image')
    profession = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return 'Team'
    

class Services(models.Model):
    card = models.CharField(max_length=200)
    money = models.CharField(max_length=200)
    delivery = models.CharField(max_length=200)
    warranty = models.CharField(max_length=200)
    branded = models.CharField(max_length=200)
    afoordable = models.CharField(max_length=200)

    def __str__(self):
        return 'Services'

class ContactInfo(models.Model):
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)



