
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
    ]

    payment_type = forms.ChoiceField(choices=PAYMENT_CHOICES)

    class Meta:
        model = Order
        fields = ['delivery_address', 'payment_type']
