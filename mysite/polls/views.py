# WHEN CHANGED:
# add urls of the views at ./urls.py
# https://docs.djangoproject.com/ko/3.1/intro/tutorial03/#writing-more-views
from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def result(request, question_id):
    response = "The result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s" % question_id)

