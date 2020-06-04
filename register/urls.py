from django.urls import path
from . import views

urlpatterns = [
    path('', views.client),
    path('partners', views.partner),
]