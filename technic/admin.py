from django.contrib import admin
from technic.models import Technic, Department, TypeTechnic, Service


@admin.register(TypeTechnic)
class TypeTechnicAdmin(admin.ModelAdmin):
    """Отображение в админ панели типа техники"""
    list_display = ('pk', 'name')  # показываем поля в списке модели
    ordering = ('pk', 'name')  # сортировка по первому полю id и имени


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Отображение в админ панели подразделения"""
    list_display = ('pk', 'name')  # показываем поля в списке модели
    ordering = ('pk', 'name')  # сортировка по первому полю id и имени


@admin.register(Technic)
class TechnicAdmin(admin.ModelAdmin):
    """Отображение в админ панели техники"""
    list_display = ('name', 'number', 'type', 'imei', 'invnumber')  # показываем поля в списке модели
    list_filter = ('type',)  # фильтрация по полю type
    ordering = ('name',)  # сортировка по имени

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Отображение в админ панели сервисных работ на технике"""
    list_display = ('technic','work','date','description')  # показываем поля в списке модели