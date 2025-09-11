from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('add/', views.add_song, name='add'),
    path('edit/<int:id>/', views.edit_song, name='edit'),
    path('delete/<int:id>/', views.delete_song, name='delete'),
    path('info/<int:id>/', views.song_info, name='info'),
]
