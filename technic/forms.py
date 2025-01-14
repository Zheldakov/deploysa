from django import forms
from .models import Department, TypeTechnic
from users.forms import StyleFromMixin


class DepartmentForm(StyleFromMixin, forms.ModelForm):
    """ Форма подразделения."""

    class Meta:
        model = Department
        fields = '__all__'

class TypeTechnicForm(StyleFromMixin, forms.ModelForm):
    """ Форма типа техники"""

    class Meta:
        model = TypeTechnic
        fields = '__all__'