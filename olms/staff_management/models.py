from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Faculty(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    staff_id = models.IntegerField()
    gender = models.CharField(max_length=1)
    department = models.CharField(max_length=10)
    age=models.IntegerField(validators=[MaxValueValidator(70),MinValueValidator(25)])

    def __str__(self):
        return f"Welcome Mr.{self.fname} {self.lname} from {self.department}"
    

class Leaves(models.Model):
    leave_type = models.CharField(max_length=10)
    from_date = models.DateField()
    to_date = models.DateField()
    comments = models.CharField(max_length=1000)


class LeaveAccount(models.Model):
    staff_id = models.CharField(max_length=50)
    cl_avail = models.IntegerField()
    cl_used = models.IntegerField(null=True)
    el_avail = models.IntegerField()
    el_used = models.IntegerField(null=True)
    sl_avail = models.IntegerField()
    sl_used = models.IntegerField(null=True)

