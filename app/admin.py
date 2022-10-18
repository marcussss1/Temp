from django.contrib import admin
from app.models import Tag
from app.models import Question

# Register your models here.
admin.site.register(Tag)
admin.site.register(Question)
