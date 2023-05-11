
from django import forms

class iban(forms.Form):
    iban = forms.CharField(label="iban", max_length=100)
