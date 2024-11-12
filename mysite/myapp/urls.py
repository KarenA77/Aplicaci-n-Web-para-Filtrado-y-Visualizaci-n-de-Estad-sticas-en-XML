from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('documentacion', views.documentacion),
    path('estudiante', views.estudiante ),
]