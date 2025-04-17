from django.db import models

# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 20)


    def __str__(self):
        return f'{self.first_name} teaches the subject {self.subject}'