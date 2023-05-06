from django.urls import path
from . import views

urlpatterns = [
    path('hello/' , views.Hello),
    path('sign/' , views.Sigin)
]