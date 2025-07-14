
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.update_task, name='update_task'), 
    path('toggle/<int:pk>/', views.toggle_done, name='toggle_done'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
