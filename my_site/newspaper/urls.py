from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_num>/',views.page_num_view),
    path('<str:topic>/',views.news_paper),
    path('',views.welcome_view),
]

