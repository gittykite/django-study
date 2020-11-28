# WHEN CHANGED:
# make migrataions & reflect to DB
# $ python manage.py makemigrations polls
# $ python manage.py migrate

# check sql creating polls DB scheme
# $ python manage.py sqlmigrate polls 0001
# https://docs.djangoproject.com/ko/3.1/intro/tutorial02/#activating-models
import datetime

from django.db import models
from django.utils import timezone 


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # setting readable field name

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text    

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

