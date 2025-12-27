Информационная система регионального аэропорта (Django)

Запуск:
python -m venv venv
venv\Scripts\activate (Windows) | source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
