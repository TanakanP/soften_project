from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
PRODUCT_SIZE_CHOICES = [(j*0.1, str(j*0.1)) for j in range(60,140,5)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(required = False,
                                    choices=PRODUCT_QUANTITY_CHOICES,
                                    widget=forms.TextInput(attrs={'id' : 'productquantity'}),)
    update = forms.BooleanField(required = False,
                                initial=False,
                                widget=forms.HiddenInput)
    size = forms.TypedChoiceField(choices=PRODUCT_SIZE_CHOICES,
                                    coerce=float,
                                    widget=forms.Select(attrs={'id' : 'productsize'}))
