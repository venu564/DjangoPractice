from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = "Name")
    message = forms.CharField(widget=forms.Textarea(attrs = {'rows' : '5', 'cols': '20'}), label = "Message")