from django.contrib import admin
from .models import Book,BookInstance,Language,Author,Genre

# Register your models here.
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
