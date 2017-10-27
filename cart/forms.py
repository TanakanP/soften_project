from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
PRODUCT_SIZE_CHOICES = [(j*0.1, str(j*0.1)) for j in range(60,140,5)]

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(required = True,
                                    max_value = 200,
                                    min_value = 1)
    update = forms.BooleanField(required = False,
                                initial=False,
                                widget=forms.HiddenInput)
    size = forms.TypedChoiceField(choices=PRODUCT_SIZE_CHOICES,
                                    coerce=float)
