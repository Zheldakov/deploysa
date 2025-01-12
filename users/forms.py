from django import forms
from .models import User

from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

from users.validators import validate_password


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


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


class UserForm(StyleFromMixin, forms.ModelForm):
    """ Форма пользователя."""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'phone', 'telegram', 'avatar', 'role', 'is_active',)


class UserCreateForm(StyleFromMixin, UserCreationForm):
    """ Форма для создания нового пользователя."""

    class Meta:
        # Поля модели User
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'phone', 'telegram', 'role',)


class UserPasswordChangeForm(StyleFromMixin, PasswordChangeForm):
    """ Форма для смены пароля."""

    def clean_new_password2(self):
        # Проверка соответствия паролей
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        validate_password(password1)
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        password_validation.validate_password(password2, self.user)
        return password2
