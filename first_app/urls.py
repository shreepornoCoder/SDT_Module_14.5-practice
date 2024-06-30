from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.contact),
    path('model_form/', views.model_form),
]
