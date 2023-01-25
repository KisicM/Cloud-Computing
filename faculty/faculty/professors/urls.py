from .views import views
from django.urls import path


urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('', views.all_students_view, name='professor-list')
]