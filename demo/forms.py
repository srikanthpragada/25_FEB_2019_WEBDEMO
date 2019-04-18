from django import forms
from django.forms import ModelForm

from .models import Book


class InterestForm(forms.Form):
    amount = forms.IntegerField(min_value=1000, label="Deposit Amount")
    rate = forms.FloatField(min_value=1, max_value=50, label="Interest Rate")


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']
