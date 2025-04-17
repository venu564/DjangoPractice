from django.urls import path
from . import views

urlpatterns = [
    path('first_app/',views.simple_view),
    path('<int:num1>/<int:num2>',views.add_view)
]