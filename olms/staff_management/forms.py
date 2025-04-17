from django import forms
from django.forms import ModelForm
from .models import LeaveAccount

class ApplyLeave(forms.Form):
    CHOICES= (('Casual','CASUAL'),('Earned','EARNED'),('Sick','SICK'),)
    leave_type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    from_date = forms.DateField(widget =forms.DateInput(attrs={'type':'date'}), label = 'From Date')
    to_date = forms.DateField(widget =forms.DateInput(attrs={'type':'date'}), label = 'To Date')
    comments = forms.CharField(widget=forms.Textarea,label='Comments')

class CreateLeaveAccount(forms.ModelForm):
    class Meta:
        model = LeaveAccount
        fields = ['staff_id','cl_avail','el_avail','sl_avail']

