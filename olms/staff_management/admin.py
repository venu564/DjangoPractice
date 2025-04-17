from django.contrib import admin
from .models import Faculty, Leaves, LeaveAccount

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Leaves)
admin.site.register(LeaveAccount)