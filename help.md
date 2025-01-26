Инструкция по настройке Django-проекта с Gunicorn и PostgreSQL

1. Установка необходимых пакетов

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv -y

2. Создание виртуального окружения и активация

mkdir app
cd app
python3 -m venv venv
source venv/bin/activate

3. Настройка конфигурации Django

Откройте файл settings.py и измените параметры:

ALLOWED_HOSTS = [  
    'localhost',  
    '127.0.0.1',  
    '192.168.1.74',  
    'app.ictd.ru'  
]  

CSRF_TRUSTED_ORIGINS = [  
    'http://127.0.0.1',  
    '192.168.1.74',  
    'http://localhost',  
    'https://app.ictd.ru',  
]

4. Копирование проекта на сервер

cd /Users/rm2k/Documents/Programming/Pycharm/diploma_django_project
rsync -avz --exclude=".venv" --exclude=".idea" --exclude=".git"  . sb:app

5. Установка зависимостей проекта

pip install -r requirements.txt
pip install django gunicorn psycopg2-binary

6. Настройка Gunicorn

Создайте сервис для Gunicorn:

sudo nano /etc/systemd/system/gunicorn.service

Добавьте следующую конфигурацию:

[Unit]
Description=Gunicorn instance to serve Django project
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/home/rm2k/app
ExecStart=/home/rm2k/app/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:80 config.wsgi:application

[Install]
WantedBy=multi-user.target

7. Запуск и управление Gunicorn

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn

8. Установка PostgreSQL

sudo apt update && sudo apt install postgresql postgresql-contrib -y

9. Создание базы данных и пользователя

sudo -u postgres psql

Внутри PostgreSQL выполните команды:

CREATE USER ictduser WITH PASSWORD '12345';
CREATE DATABASE ictd_database OWNER ictduser;
CREATE DATABASE user_data OWNER ictduser;

10. Выполнение миграций Django

python manage.py migrate

Теперь проект должен быть развернут и готов к использованию.