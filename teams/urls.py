from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('<int:pk>/', views.team_detail, name='team_detail'),
    path('<int:pk>/email/', views.email_team, name='email_team'),
    path('<int:pk>/schedule/', views.schedule_team_meeting, name='schedule_team_meeting'),
    path('<int:pk>/dependencies/', views.dependencies_view, name='team_dependencies'),
]
