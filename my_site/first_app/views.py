from django.shortcuts import render
from django.http.response import HttpResponse

def simple_view(request):
    return HttpResponse("SIMPLE VIEW")

# Create your views here.
def add_view(request, num1, num2):
    result = num1 + num2
    return HttpResponse(f"{num1} + {num2} = {str(result)}")
