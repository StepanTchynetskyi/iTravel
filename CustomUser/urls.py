from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.CustomUserView.as_view(), name='home'),
]