from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_students_view, name='student-list'),
    path('register/', views.registration_view, name='student-register'),
]