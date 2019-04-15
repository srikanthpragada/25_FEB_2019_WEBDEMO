from django import forms


class InterestForm(forms.Form):
    amount = forms.IntegerField(min_value=1000, label="Deposit Amount")
    rate = forms.FloatField(min_value=1, max_value=50, label="Interest Rate")
