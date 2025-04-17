from django.urls import path
from . import views

app_name = 'new_app'

urlpatterns = [
    path('',views.example_view,name='example'),
    path('thankyou/', views.logout_view, name='thankyou'),
    path('faculty/',views.faculty_view,name='faculty')
]