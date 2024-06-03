from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    email = forms.EmailField(max_length=254, required=True, label='Email')
    subject = forms.CharField(max_length=100, required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
