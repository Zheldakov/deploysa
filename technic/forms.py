from django import forms
from .models import Department, TypeTechnic, Technic, Service
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

class ServiceForm(StyleFromMixin, forms.ModelForm):
    """ Форма для тех. Обслуживания"""

    class Meta:
        model = Service
        fields = '__all__'
