from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Faculty, Leaves, LeaveAccount
from .forms import ApplyLeave, CreateLeaveAccount

# Create your views here.

def home_view(request):
    return render(request,'index.html')

def add_staff(request):
    if request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        staff_id = int(request.POST['staff_id'])
        department = request.POST['department']
        age = int(request.POST['age'])

        Faculty.objects.create(fname = fname, lname = lname, age = age, gender = gender, department = department, staff_id = staff_id)
        return redirect(reverse('staff_management:view'))
    else:
         return render(request,'staff_management/staff_add.html')

def delete_staff(request):

    if request.POST:
        staff_id = request.POST['staff_id']
        faculty_QS = Faculty.objects.filter(staff_id = staff_id).all()
        for faculty in faculty_QS:
            faculty.delete()
        return redirect(reverse('staff_management:view'))
    else:
         return render(request,'staff_management/staff_delete.html')

def view_staff(request):
    staff_qs = Faculty.objects.all()
    staff = {'faculty': staff_qs}
    return render(request,'staff_management/staff_view.html', context=staff)

def apply_view(request):
    form = ApplyLeave(request.POST)
    if request.POST:
         if form.is_valid():
            print(form.cleaned_data['leave_type'])
            leave_details = form.cleaned_data
            Leaves.objects.create(leave_type = leave_details['leave_type'], from_date = leave_details['from_date'], to_date = leave_details['to_date'], comments = leave_details['comments'])
            return redirect(reverse('staff_management:home'))
    else:
        form = ApplyLeave()
        return render(request,'staff_management/apply_leave.html',context={'form':form})
    
def create_leave(request):
    form = CreateLeaveAccount(request.POST)
    if request.POST:       
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('staff_management:home'))
    else:
        form = CreateLeaveAccount()
        return render(request,'staff_management/create_leave.html', context={'form':form})
