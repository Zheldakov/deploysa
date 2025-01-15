from django import forms
from .models import Department, TypeTechnic, Technic
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


class TechnicForm(StyleFromMixin, forms.ModelForm):
    """ Форма типа техники"""

    class Meta:
        model = Technic
        fields = '__all__'
