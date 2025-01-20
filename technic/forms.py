from django import forms
from .models import Department, TypeTechnic, Technic, Service


class DepartmentForm(forms.ModelForm):
    """ Форма подразделения."""

    class Meta:
        model = Department
        fields = '__all__'

        widgets = {
            'description': forms.Textarea(attrs={
                'cols': 65, 'rows': 5,
                'class': 'text_article_form'}),
        }


class TypeTechnicForm(forms.ModelForm):
    """ Форма типа техники"""

    class Meta:
        model = TypeTechnic
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'cols': 65, 'rows': 5,
                'class': 'text_article_form'}),
        }


class TechnicForm(forms.ModelForm):
    """ Форма типа техники"""

    class Meta:
        model = Technic
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    """ Форма для тех. Обслуживания"""

    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'cols': 65, 'rows': 5,
                'class': 'text_article_form'})
        }