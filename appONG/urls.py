from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('OqueONG', views.OqueONG, name='OqueONG'),
    path('OqueFaz', views.OqueFaz, name='OqueFaz'),
    path('DoacoesONG', views.DoacoesONG, name='DoacoesONG')
]