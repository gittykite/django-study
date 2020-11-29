# WHEN CHANGED:
# add urls of the views at ./urls.py
# https://docs.djangoproject.com/ko/3.1/intro/tutorial03/#writing-more-views
from django.http import HttpResponse

from .models import Question


def index(request):
    # get 5 latest questions from DB 
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # display question list (ver.hard-coding)
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def result(request, question_id):
    response = "The result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s" % question_id)

