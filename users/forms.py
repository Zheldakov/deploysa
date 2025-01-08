from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm



# class StyleFromMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'

class UserLoginForm(forms.Form):
    """ Форма для авторизации пользователя."""
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
       'placeholder': 'Пароль'
    }))
#

# class UserLoginForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', 'password')
#         widgets = {
#             'email': forms.TextInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': " Password"
#             }),
#         }


# class UserLoginForm(AuthenticationForm):
#     email = forms.EmailField(
#         max_length=150,
#         label='Имя пользователя',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите имя пользователя'
#         })
#     )
#     password = forms.CharField(
#         max_length=128,
#         label='Пароль',
#         widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Введите пароль'
#         })
#         )
#
#     class Meta:
#         model = User
#         fields = ['email', 'password']

