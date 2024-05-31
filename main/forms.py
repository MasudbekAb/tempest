# forms.py
from django import forms

class SendLetter(forms.Form):
    first_name = forms.CharField(label='Your firstname', max_length=100)
    last_name = forms.CharField(label='Your lastname', max_length=100)
    email = forms.EmailField(label='Your email address', max_length=100)
    subject = forms.CharField(label='Your subject of this message', max_length=100)
    message = forms.CharField(label='Your message about us', max_length=1000)
