release: python manage.py makemigrations && python manage.py migrate
web: gunicorn main.wsgi:application