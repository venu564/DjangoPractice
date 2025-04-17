from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.core.exceptions import ValidationError

def gender_validation(value):
    if not value in ('m','f','M','F'):
        return ValidationError(f'Invalid Gender {value}')

# Create your models here.
class Faculty(models.Model):
    fname = models.CharField(max_length=30)
    staff_id = models.IntegerField()
    department = models.CharField(max_length=30)
    age = models.IntegerField(default = 30, validators=[MinValueValidator(25),MaxValueValidator(65)])
    gender = models.CharField(max_length=1,validators=[gender_validation],null=True)

    def __str__(self):
        return f"Welcome Mr. {self.fname} from {self.department} department. You are {self.age}{self.gender} years old as per the records"
