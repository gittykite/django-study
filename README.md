# django-study

### setup conda & django
cd D:\1912tensor\pet-django

conda create -n pet python=3.7

conda activate pet-django

conda install django


### create & test django site
django-admin startproject mysite

cd ./mysite

python manage.py runserver
> http://127.0.0.1:8000/

### create polls app
python manage.py startapp polls
