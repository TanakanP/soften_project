from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    address = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'address', 'email', 'password1', 'password2', )

class EditForm(UserChangeForm):
    address = forms.CharField(max_length=30, required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'address',)
        exclude = ('password',)

    def clean_password(self):
        return ""
