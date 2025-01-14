from django.db import models

# настройка полей, чтобы возможно было заполнить поля пустыми
NULLABLE = {'blank': True, 'null': True}


class TypeTechnic(models.Model):
    """Тип техники"""
    name = models.CharField(max_length=100, verbose_name='Тип', **NULLABLE)  # `Имя типа техники
    description = models.CharField(max_length=150, verbose_name='Описание', **NULLABLE)  # Описание

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип техники'
        verbose_name_plural = 'Типы техники'


class Department(models.Model):
    """Подразделение техники"""
    name = models.CharField(max_length=100, verbose_name='Подразделение', **NULLABLE)  # Имя подразделения
    description = models.CharField(max_length=150, verbose_name='Описание', **NULLABLE)  # Описание

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Technic(models.Model):
    """Техника"""
    name = models.CharField(max_length=250, verbose_name='Наименование', **NULLABLE)  # Наименование техники
    type = models.ForeignKey(TypeTechnic, on_delete=models.CASCADE, verbose_name='Тип')  # Тип техники
    photo = models.ImageField(upload_to='technic/', verbose_name='Изображение', **NULLABLE)  # Фотография техники
    number = models.CharField(max_length=8, verbose_name='Гос. номер', **NULLABLE)  # Государственный номер
    invnumber = models.IntegerField(verbose_name="Инвентарный номер", **NULLABLE)  # Инвентарный номер
    imei = models.IntegerField(verbose_name='IMEI', **NULLABLE)  # номер IMEI
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name='Подразделение')  # Подразделение техники

    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return f'{self.name} ({self.number})'  # техника в формате "Наименование техники (гос.Номер)"

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'


class Service(models.Model):
    """Техническое обслуживание"""
    technic = models.ForeignKey(Technic, on_delete=models.CASCADE)  # Техника на которой проведен сервис
    work = models.CharField(max_length=100, verbose_name='Работа')  # Проведенная работа
    date = models.DateField(**NULLABLE, verbose_name='Дата выполнения')  # Дата проведения работы
    description = models.CharField(max_length=250, verbose_name='Описание работ', **NULLABLE)  # Описание работы

    def __str__(self) -> str:
        return f'{self.technic} - {self.work}'

    class Meta:
        verbose_name = 'Тех. обслуживание'
        verbose_name_plural = 'Тех. обслуживания'
