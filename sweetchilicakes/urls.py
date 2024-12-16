from django.urls import path
from . import views

urlpatterns = [
    path('', views.CakeShowcase.as_view(), name='cakes.')
]