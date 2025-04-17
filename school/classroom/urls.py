from django.shortcuts import redirect
from django.urls import reverse, path
from .views import (WelcomeView, ThankYouView, ContactFormView, TeacherCreateView, 
                    TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView )

app_name = 'classroom'

urlpatterns = [
    path('',WelcomeView.as_view() ,name='home'),
    path('thank_you/',ThankYouView.as_view(), name = 'thank_you'),
    path('contact/',ContactFormView.as_view(), name= 'contact'),
    path('create/',TeacherCreateView.as_view(), name = 'create'),
    path('teachers/',TeacherListView.as_view(), name ='list'),
    path('teacher_detail/<int:pk>',TeacherDetailView.as_view(), name='details'),
    path('update/<int:pk>', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TeacherDeleteView.as_view(), name = 'delete')
]
