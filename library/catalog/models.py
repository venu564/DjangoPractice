from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}'
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author, max_length=100)
    summary = models.CharField(max_length=50)
    isbn = models.CharField(max_length=100, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    

import uuid
class BookInstance(models.Model):
    id = uuid.getnode
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=10)
    due_back = models.DateField()
    choice = (
        ('m', 'mainteance'),
        ('l', 'lender')
    )
    borrower = models.CharField(max_length=1, choices=choice)
    
