"""Команда создания базы данных Django (DjangoDB)"""
from django.core.management import BaseCommand
import pyodbc
from config.settings import DATABASE, USER, PASSWORD, HOST, DRIVER, PAD_DATABASE


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Старт создания БД")
        ConnectionString = f'''
            DRIVER={DRIVER};
            SERVER={HOST};
            DATABASE={PAD_DATABASE};
            UID={USER};
            PWD={PASSWORD}'''

        try:
            conn = pyodbc.connect(ConnectionString)
            conn.autocommit = True
            conn.execute(fr"CREATE DATABASE {DATABASE}")
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            print(f"Создана база данных {DATABASE}")
