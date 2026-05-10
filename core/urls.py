from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'), 
<<<<<<< HEAD
    path('notifications/', views.notifications_view, name='notifications'),
]
=======
    path('notifications/', views.notifications_views, name='notifications'),
]
>>>>>>> 1bbd6c5 (Initial project setup)
