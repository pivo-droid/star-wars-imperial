from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('character/<int:pk>/', views.character_detail, name='character_detail'),
    path('ship/<int:pk>/', views.ship_detail, name='ship_detail'),
]
