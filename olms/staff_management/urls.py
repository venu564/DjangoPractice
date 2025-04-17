from django.urls import path
from . import views

app_name='staff_management'

urlpatterns = [
    path('',views.home_view,name='home'),
    path('add/',views.add_staff, name='add'),
    path('delete/',views.delete_staff, name='delete'),
    path('view_staff/',views.view_staff, name='view'),
    path('apply/',views.apply_view, name='apply'),
    path('create_leave/',views.create_leave, name='create_leave'),
]
