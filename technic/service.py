import requests
import os
import re
from dotenv import load_dotenv

import time
import json

load_dotenv()
GLONASSSOFT_LOGIN = os.getenv('GLONASSSOFT_LOGIN')
GLONASSSOFT_PASSWORD = os.getenv('GLONASSSOFT_PASSWORD')


class Glonasssoft:
    """Класс для работы с ГЛОНАССсофтом"""

    data_glonass = []

    def __init__(self, number_get_technic):
        self.number_get_technic = number_get_technic

    def in_json(self, data, file_name):
        # метод создания файла json
        data_json = json.dumps(data, ensure_ascii=False, indent=1)
        with open(f"json/{file_name}.json", "wt", encoding='utf-8') as file:
            file.write(data_json)

    def post_auth(self):
        # Запрос для получения токена авторизации, принимает login и пароль объекта
        params = {"login": GLONASSSOFT_LOGIN, "password": GLONASSSOFT_PASSWORD}
        indicator = True
        while indicator == True or indicator == 429:
            time.sleep(1)
            print(f"Старт запроса авториpзации. Код:{indicator}")
            token = requests.post("https://hosting.glonasssoft.ru/api/v3/auth/login", json=params)
            indicator = token.status_code
            print("Запрос авторизации:", token.status_code)
        return token.json()

    def get_find(self):
        # Все объекты в системе
        headers = {'Content-Type': 'application/json',
                   'X-Auth': self.post_auth()['AuthId']}
        params = {"vehicleId": None,  # 84350, ID ТС(int, опционально)
                  "name": None,  # Имя ТС(string, опционально)
                  #   "imei": None,         # "710179307", // IMEI(string, опционально)
                  #   "sim": None,          # "938112", // Номер телефона(string, опционально)
                  #   "deviceTypeId": None, # 5, ID типа устройства(short, опционально)
                  #   "parentId": None,     # ID клиента(Guid, опционально)
                  #   "unitId": None,       # "b33548c3-73c3-40e4-8b78-81470ae744ed", ID подразделения(Guid, опционально)
                  #   "customFields": None  # значение любого из произвольных полей ТС
                  }
        indicator = True
        while indicator == True or indicator == 429:
            time.sleep(1)
            print(f"Старт запроса получения объектов в системе. Код:{indicator}")
            data_technic = requests.post(
                'https://hosting.glonasssoft.ru/api/v3/vehicles/find', headers=headers, json=params)
            indicator = data_technic.status_code
            print("Запрос данных по всей техники. Код:", data_technic.status_code)
        return data_technic.json()

    def get_name_id(self):
        # метод делает запрос техники и возвращает словарь по значению {гос.номер:{neme:"Имя","vehicleId":"ИД"}

        list_technic = self.get_find()
        name_id = {}
        new_name_id = {}
        for dict in list_technic:
            name_id[dict["name"]] = dict["vehicleId"]
        for key, value in name_id.items():
            num_tractor = re.findall('[0-9]{4}[а-яА-Я]{2}[0-9]{1,3}', key)
            num_car = re.findall('[а-яА-Я][0-9]{3}[а-яА-Я]{2}[0-9]{1,3}', key)
            if num_car != []:
                new_name_id[num_car[0].lower()] = {"name": key, "vehicleId": value, "type": "автомобиль"}
            if num_tractor != []:
                new_name_id[num_tractor[0].lower()] = {"name": key, "vehicleId": value, "type": "с/х техника"}
        print("Формирование словаря гос. номер - ID")
        return new_name_id

    def get_id_technic(self):
        # метод возвращает ID техники из name_id
        vehicleId = self.get_name_id()
        if self.number_get_technic in vehicleId:
            return vehicleId[self.number_get_technic]['vehicleId']
        else:
            return None

    def get_technic(self, id_technic):
        # Запрос для получения данных по объекту, принемает id объекта

        headers = {'X-Auth': self.post_auth()['AuthId']}
        indicator = True
        while indicator == True or indicator == 429:
            time.sleep(1)
            print(f"Старт запроса данных по объекту. Код:{indicator}")
            technic = requests.get(
                f'https://hosting.glonasssoft.ru/api/v3/vehicles/{id_technic}', headers=headers)
            indicator = technic.status_code
            print("Запрос данных по объекту. Код:", technic.status_code)
        return technic

    @staticmethod
    def time_r(data_time):
        # метод преобразует время в нормальный формат
        format_time = data_time.replace("T", " ").replace("Z", "")
        list_data_time = format_time.split(" ")
        list_data = list_data_time[0].split("-")
        list_time = list_data_time[1].split(":")
        return f"{list_data[2]}-{list_data[1]}-{list_data[0]} {int(list_time[0]) + 3}:{list_time[1]}"

    def get_lastdata(self, id_technic):
        # метод делает запрос на последнее сообщение по ID трекера
        headers = {'Content-Type': 'application/json',
                   'X-Auth': self.post_auth()['AuthId']}
        params = json.dumps([id_technic])
        indicator = True
        while indicator == True or indicator == 429:
            time.sleep(1)
            print(f"Старт запроса получения последних данных. Код:{indicator}")
            lastdata = requests.post(
                'https://hosting.glonasssoft.ru/api/v3/vehicles/getlastdata', headers=headers, data=params)
            indicator = lastdata.status_code
            print("Запрос последнего сообщения по ID:", lastdata.status_code)
        return lastdata.json()

    @staticmethod
    def get_fild(last_message):
        # Функция переберает все геозоны и находит самое первое с/х поле
        import re
        re_fild = re.compile('^[А-Я]{3}-[А-Я]{2,3}-[0-9]{3}-[0-9]{2}$')
        if last_message[0]['geozones'] != []:
            for i in last_message[0]['geozones']:
                if re_fild.match(i['name']):
                    return f"Поле: {i['name']}"
                return ""
        return ""


def get_info(num_technic):
    # Функция дает информацию на сайт по последнему местоположению техники
    technic = Glonasssoft(num_technic)
    id_technic = technic.get_id_technic()
    print("получено ID: ", id_technic)
    # проверка на наличие ID базе
    if id_technic == None:
        return None
    else:
        # проверка на наличие сообщений от объекта
        last_message = technic.get_lastdata(id_technic)
        if last_message[0]['receiveTime'] == None:
            return "данных нет"
        else:
            technic_info = {
                "glonass_technic": last_message[0]["vehicleNumber"],
                "glonass_data": technic.time_r(last_message[0]["recordTime"]),
                "glonass_address": last_message[0]['address'],
                "glonass_speed": last_message[0]['speed'],
                "glonass_geozone": technic.get_fild(last_message),
            }
            return technic_info
