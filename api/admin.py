from django.contrib import admin
from .models import programmer
from .models import students
# Register your models here.
admin.site.register(programmer)
admin.site.register(students)