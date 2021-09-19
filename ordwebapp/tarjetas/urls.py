"""urls de la app tarjetas"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('populate/', views.populate, name='populate'),
    path('cards/', views.cards, name='cards'),
    path('sidedown/', views.sidedown, name='sidedown'),
    path('writit/', views.writit, name='writit'),
]
