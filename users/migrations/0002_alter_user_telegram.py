# Generated by Django 5.0.10 on 2025-01-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Telegram'),
        ),
    ]
