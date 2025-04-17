from django.shortcuts import render
from . import models

# Create your views here.
def example_view(request):
    usr = {'fname': 'John', 'lname' : 'Victor', 
             'addr':{'city':'Hyderabad','country':'India'}, 'contact':['9000000000','7000000'] }
    return render(request, 'new_app/example.html', context = usr)

def logout_view(request):
    return render(request,'new_app/thankyou.html')

def faculty_view(request):
    faculty = models.Faculty.objects.all()
    staff = {'faculty':faculty}
    return render(request,'new_app/Faculty.html',context = staff)