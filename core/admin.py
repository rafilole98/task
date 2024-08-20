from django.contrib import admin
from .models import Job,Person,PersonJobDetail
# Register your models here.
admin.site.register(Job)
admin.site.register(Person)
admin.site.register(PersonJobDetail)