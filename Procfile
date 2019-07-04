web: gunicorn workoutApp.wsgi --log-file -
release: python manage.py makemigrations rep && python manage.py makemigrations set && python manage.py makemigrations workout && python manage.py migrate
