from django.contrib import admin

from .models import Question

# add Question model to admin page
admin.site.register(Question)