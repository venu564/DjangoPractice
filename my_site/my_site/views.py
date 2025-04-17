from django.shortcuts import render
def custom_error_page_view(request,exception):
    return render(request,'custom_error_page.html',status=404)