from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="index" ),
    path('about/', views.about , name="about" ),
    path('privacy-policy/', views.privacy , name="privacy"),
    path('real-time/', views.realtime, name="realtime"),   
]
