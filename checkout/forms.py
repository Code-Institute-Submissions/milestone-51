from django import forms
from .models import Order

# Checkout form fields


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'street_address1',
                  'street_address2', 'town_or_city', 'postcode', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Make placeholders, delete auto-generated
        labels and autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
